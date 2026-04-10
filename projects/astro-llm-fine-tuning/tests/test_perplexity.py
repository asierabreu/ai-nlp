from __future__ import annotations

import math

from src.evaluation.perplexity import perplexity_from_losses


def test_perplexity_from_losses() -> None:
    losses = [1.0, 1.0]
    assert math.isclose(perplexity_from_losses(losses), math.e, rel_tol=1e-6)
