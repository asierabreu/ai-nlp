from __future__ import annotations

import re
from typing import Any


_WS_RE = re.compile(r"\s+")


def normalize_text(text: str) -> str:
    cleaned = text.replace("\x00", " ").strip().lower()
    return _WS_RE.sub(" ", cleaned)


def clean_records(records: list[dict[str, Any]], text_key: str = "text") -> list[dict[str, Any]]:
    cleaned_records: list[dict[str, Any]] = []
    for record in records:
        copy = dict(record)
        value = copy.get(text_key)
        if isinstance(value, str):
            copy[text_key] = normalize_text(value)
        cleaned_records.append(copy)
    return cleaned_records
