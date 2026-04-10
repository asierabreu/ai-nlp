from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from src.data.pipeline import run_data_pipeline
from src.evaluation.qa_benchmark import evaluate_qa_predictions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run end-to-end smoke test for scientific LLM stack")
    parser.add_argument("--input", default="data/raw/sample_scientific_qa.jsonl")
    parser.add_argument("--output", default="data/processed/smoke")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    pipeline_result = run_data_pipeline(
        input_path_or_url=args.input,
        output_dir=args.output,
        source_type="jsonl",
        custom_tokenizer=True,
    )

    os.environ["INFERENCE_BACKEND"] = "mock"
    os.environ["MODEL_NAME"] = "scientific-mock"
    from src.serving.api import app

    client = TestClient(app)
    response = client.post(
        "/generate",
        json={
            "prompt": "Explain CRISPR in one sentence.",
            "max_tokens": 64,
            "temperature": 0.0,
            "stream": False,
        },
    )
    response.raise_for_status()
    generated = response.json()["text"]

    rows = [
        {
            "prediction": generated,
            "reference": "crispr is a gene-editing technology.",
        }
    ]
    qa_metrics = evaluate_qa_predictions(rows)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "pipeline_records": pipeline_result["records"],
        "dataset_manifest": pipeline_result["manifest"],
        "generate_status": response.status_code,
        "generate_preview": generated[:120],
        "qa_metrics": qa_metrics,
    }
    (output_dir / "smoke_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
