"""Supervised fine-tuning entrypoint built on the shared training pipeline.

The `run_sft` wrapper marks the task type as `sft` and forwards configuration
handling and training execution to the common causal language-model routine.
"""

from __future__ import annotations

from src.training.common import run_causal_lm_training


def run_sft(config_path: str) -> None:
    run_causal_lm_training(config_path=config_path, task_name="sft")
