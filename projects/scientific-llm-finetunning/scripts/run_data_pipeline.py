from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.data.pipeline import run_data_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run dataset ingestion/clean/tokenization/versioning pipeline")
    parser.add_argument("--input", required=True, help="Input path or API URL")
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument("--source-type", default="jsonl", choices=["jsonl", "text", "api"])
    parser.add_argument("--tokenizer", default="gpt2")
    parser.add_argument("--custom-tokenizer", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = run_data_pipeline(
        input_path_or_url=args.input,
        output_dir=args.output,
        source_type=args.source_type,
        tokenizer_name=args.tokenizer,
        custom_tokenizer=args.custom_tokenizer,
    )
    print(result)


if __name__ == "__main__":
    main()
