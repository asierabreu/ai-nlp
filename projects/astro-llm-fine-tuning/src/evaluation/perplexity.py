"""Perplexity computation helpers for language-model evaluation.

The module implements a compact utility that transforms a sequence of loss
values into perplexity using the exponential of mean loss, with input validation
to prevent silent misuse on empty samples.
"""

from __future__ import annotations

import math


def perplexity_from_losses(losses: list[float]) -> float:
    if not losses:
        raise ValueError("losses must not be empty")
    avg_loss = sum(losses) / len(losses)
    return math.exp(avg_loss)
