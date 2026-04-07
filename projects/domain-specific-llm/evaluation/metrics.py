"""Domain-specific evaluation metrics."""

from __future__ import annotations

from typing import List


def exact_match(predictions: List[str], references: List[str]) -> float:
    """Compute exact match accuracy.

    Args:
        predictions: List of model-generated strings.
        references: List of ground-truth strings.

    Returns:
        Exact match score in [0, 1].
    """
    if not predictions or len(predictions) != len(references):
        raise ValueError("predictions and references must be non-empty and equal length")
    matches = sum(p.strip() == r.strip() for p, r in zip(predictions, references))
    return matches / len(predictions)


def token_f1(prediction: str, reference: str) -> float:
    """Compute token-level F1 between a prediction and reference.

    Args:
        prediction: Model-generated answer.
        reference: Ground-truth answer.

    Returns:
        F1 score in [0, 1].
    """
    pred_tokens = prediction.lower().split()
    ref_tokens = reference.lower().split()

    if not pred_tokens or not ref_tokens:
        return 0.0

    common = set(pred_tokens) & set(ref_tokens)
    if not common:
        return 0.0

    precision = len(common) / len(pred_tokens)
    recall = len(common) / len(ref_tokens)
    return 2 * precision * recall / (precision + recall)
