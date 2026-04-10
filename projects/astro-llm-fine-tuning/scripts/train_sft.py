from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.training.sft import run_sft


def main() -> None:
    parser = argparse.ArgumentParser(description="Run supervised fine-tuning")
    parser.add_argument("--config", default="configs/training_sft.yaml")
    args = parser.parse_args()
    run_sft(args.config)


if __name__ == "__main__":
    main()
