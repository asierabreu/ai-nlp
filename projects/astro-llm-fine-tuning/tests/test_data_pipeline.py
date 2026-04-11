from __future__ import annotations

import json
from pathlib import Path

from src.data.pipeline import run_data_pipeline


def test_run_data_pipeline_with_custom_tokenizer(tmp_path: Path) -> None:
    source = tmp_path / "input.jsonl"
    source.write_text(json.dumps({"text": "A scientific sentence."}) + "\n", encoding="utf-8")

    output_dir = tmp_path / "out"
    result = run_data_pipeline(
        input_path_or_url=str(source),
        output_dir=str(output_dir),
        source_type="jsonl",
        custom_tokenizer=True,
    )

    assert result["records"] == 1
    version_dir = output_dir / "version"
    assert version_dir.exists(), "Version directory should exist"
    digest_short = result["manifest"]["digest_short"]
    assert (output_dir / f"dataset_{digest_short}.jsonl").exists(), f"Dataset file with hash suffix should exist"
    assert (version_dir / f"manifest_{digest_short}.json").exists(), f"Manifest file with hash suffix should exist"
