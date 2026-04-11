"""Pretraining entrypoint for causal language-model training.

The module exposes a thin wrapper that labels the run as `pretrain` and
delegates full execution to the shared training implementation. This keeps CLI
and script integrations simple while reusing the common training stack.
"""

from __future__ import annotations

from src.training.common import run_causal_lm_training


def run_pretraining(config_path: str) -> None:
    run_causal_lm_training(config_path=config_path, task_name="pretrain")
