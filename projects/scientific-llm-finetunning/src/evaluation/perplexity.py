from __future__ import annotations

import math


def perplexity_from_losses(losses: list[float]) -> float:
    if not losses:
        raise ValueError("losses must not be empty")
    avg_loss = sum(losses) / len(losses)
    return math.exp(avg_loss)
