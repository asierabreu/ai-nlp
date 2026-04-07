"""Dataset loading helpers shared across projects."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Dict, List


def load_jsonl(path: str | Path) -> List[Dict[str, Any]]:
    """Load a JSONL file into a list of dictionaries.

    Args:
        path: Path to the .jsonl file.

    Returns:
        List of parsed JSON objects.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def load_csv(path: str | Path, delimiter: str = ",") -> List[Dict[str, str]]:
    """Load a CSV file into a list of dictionaries.

    Args:
        path: Path to the .csv file.
        delimiter: Column delimiter character.

    Returns:
        List of row dictionaries (keys are column headers).
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader)
