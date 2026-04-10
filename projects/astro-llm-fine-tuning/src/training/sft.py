from __future__ import annotations

from src.training.common import run_causal_lm_training


def run_sft(config_path: str) -> None:
    run_causal_lm_training(config_path=config_path, task_name="sft")
