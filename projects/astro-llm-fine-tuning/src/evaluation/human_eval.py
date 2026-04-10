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
