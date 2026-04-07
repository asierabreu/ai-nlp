"""Database models for the annotation tool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Annotation:
    """Represents a single span annotation."""

    text: str
    start: int
    end: int
    label: str
    doc_id: str = ""


@dataclass
class Document:
    """Represents an annotated document."""

    id: str
    text: str
    annotations: List[Annotation] = field(default_factory=list)

    def to_jsonl(self) -> dict:
        """Export document to JSONL-compatible dict."""
        return {
            "id": self.id,
            "text": self.text,
            "entities": [
                {"start": a.start, "end": a.end, "label": a.label}
                for a in self.annotations
            ],
        }

    def to_conll(self) -> str:
        """Export document in CoNLL-2003 token format."""
        tokens = self.text.split()
        lines = []
        char_idx = 0
        span_map: dict[int, Annotation] = {}
        for ann in self.annotations:
            span_map[ann.start] = ann

        for token in tokens:
            token_start = self.text.find(token, char_idx)
            label = "O"
            for ann_start, ann in span_map.items():
                if ann_start == token_start:
                    label = f"B-{ann.label}"
                elif ann_start < token_start < ann.end:
                    label = f"I-{ann.label}"
            lines.append(f"{token}\t{label}")
            char_idx = token_start + len(token)

        return "\n".join(lines)
