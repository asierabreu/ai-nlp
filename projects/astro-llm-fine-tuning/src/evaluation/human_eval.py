"""Export utilities for human-in-the-loop evaluation templates.

This module converts prediction/reference rows into a structured schema that
includes rubric fields for fluency, factuality, and domain accuracy scoring.
The resulting JSON artifact is intended for manual review workflows and audit
trails.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def export_human_eval_sheet(rows: list[dict[str, Any]], output_path: str) -> None:
    formatted = []
    for row in rows:
        formatted.append(
            {
                "prompt": row.get("prompt", ""),
                "prediction": row.get("prediction", ""),
                "reference": row.get("reference", ""),
                "fluency": None,
                "factuality": None,
                "domain_accuracy": None,
                "notes": "",
            }
        )
    Path(output_path).write_text(json.dumps(formatted, indent=2), encoding="utf-8")
