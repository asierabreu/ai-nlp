"""End-to-end dataset preparation pipeline for training and evaluation.

The pipeline orchestrates source ingestion, text normalization, tokenization,
and dataset versioning in a single callable flow. It writes both a hashed
manifest and a JSONL artifact so downstream training jobs can reproduce exactly
which processed records were used.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.data.cleaning import clean_records
from src.data.ingestion import ingest_api, ingest_jsonl, ingest_text
from src.data.tokenization import get_tokenizer, tokenize_records
from src.data.versioning import write_version_manifest


def run_data_pipeline(
    input_path_or_url: str,
    output_dir: str,
    source_type: str,
    tokenizer_name: str = "gpt2",
    custom_tokenizer: bool = False,
) -> dict[str, Any]:
    if source_type == "jsonl":
        records = ingest_jsonl(input_path_or_url)
    elif source_type == "text":
        records = ingest_text(input_path_or_url)
    elif source_type == "api":
        records = ingest_api(input_path_or_url)
    else:
        raise ValueError("source_type must be one of: jsonl, text, api")

    cleaned = clean_records(records)
    tokenizer = get_tokenizer(tokenizer_name=tokenizer_name, custom=custom_tokenizer)
    tokenized = tokenize_records(cleaned, tokenizer)

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    manifest = write_version_manifest(tokenized, output, source=input_path_or_url)
    digest_short = manifest["digest_short"]
    
    dataset_path = output / f"dataset_{digest_short}.jsonl"
    dataset_path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=True) for row in tokenized),
        encoding="utf-8",
    )

    return {"records": len(tokenized), "manifest": manifest, "dataset_path": str(dataset_path)}
