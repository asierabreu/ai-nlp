"""Data ingestion adapters for JSONL files, raw text corpora, and HTTP APIs.

Functions in this module normalize different source formats into lists of
dictionary records so later pipeline stages can operate on a consistent shape.
It supports line-delimited JSON datasets, paragraph-style text segmentation,
and JSON payload retrieval with basic response validation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import requests


def ingest_jsonl(path: str | Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def ingest_text(path: str | Path) -> list[dict[str, str]]:
    text = Path(path).read_text(encoding="utf-8")
    chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
    return [{"text": chunk} for chunk in chunks]


def ingest_api(url: str, timeout: int = 30) -> list[dict[str, Any]]:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    if isinstance(payload, list):
        return [dict(item) for item in payload]
    if isinstance(payload, dict):
        return [payload]
    raise ValueError("Unsupported API payload type")
