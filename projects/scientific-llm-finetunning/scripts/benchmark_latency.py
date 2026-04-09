from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.inference.benchmark import benchmark_latency


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark generation latency")
    parser.add_argument("--backend", default="hf", choices=["hf", "vllm"])
    parser.add_argument("--model", default="gpt2")
    parser.add_argument("--prompt", default="Explain protein folding in one paragraph.")
    parser.add_argument("--runs", type=int, default=10)
    args = parser.parse_args()

    results = benchmark_latency(args.model, args.prompt, runs=args.runs, backend=args.backend)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
