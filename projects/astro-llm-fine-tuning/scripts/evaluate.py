from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.evaluation.qa_benchmark import evaluate_qa_predictions


def _read_jsonl(path: str) -> list[dict]:
    rows: list[dict] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate QA predictions")
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--references", required=False)
    args = parser.parse_args()

    rows = _read_jsonl(args.predictions)
    metrics = evaluate_qa_predictions(rows)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
