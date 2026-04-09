from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.training.pretrain import run_pretraining


def main() -> None:
    parser = argparse.ArgumentParser(description="Run pretraining")
    parser.add_argument("--config", default="configs/training_pretrain.yaml")
    args = parser.parse_args()
    run_pretraining(args.config)


if __name__ == "__main__":
    main()
