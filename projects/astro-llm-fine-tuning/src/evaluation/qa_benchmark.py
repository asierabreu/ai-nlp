from __future__ import annotations

from typing import Any


def exact_match_score(prediction: str, reference: str) -> float:
    return float(prediction.strip().lower() == reference.strip().lower())


def evaluate_qa_predictions(rows: list[dict[str, Any]]) -> dict[str, float]:
    if not rows:
        return {"exact_match": 0.0}
    scores = [exact_match_score(str(r["prediction"]), str(r["reference"])) for r in rows]
    return {"exact_match": sum(scores) / len(scores)}
