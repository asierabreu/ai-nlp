"""Text preprocessing utilities shared across projects."""

from __future__ import annotations

import re
import unicodedata
from typing import List


def clean_text(text: str) -> str:
    """Clean and normalise input text.

    - Strip leading/trailing whitespace
    - Collapse multiple spaces
    - Normalise unicode to NFC form

    Args:
        text: Raw input string.

    Returns:
        Cleaned string.
    """
    text = unicodedata.normalize("NFC", text)
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def tokenize(text: str, lower: bool = False) -> List[str]:
    """Simple whitespace tokeniser.

    Args:
        text: Input string.
        lower: If True, lowercase all tokens.

    Returns:
        List of tokens.
    """
    tokens = text.split()
    if lower:
        tokens = [t.lower() for t in tokens]
    return tokens


def truncate(text: str, max_chars: int = 512) -> str:
    """Truncate text to at most *max_chars* characters, preserving whole words.

    Args:
        text: Input string.
        max_chars: Maximum character length.

    Returns:
        Truncated string (may be shorter than max_chars).
    """
    if len(text) <= max_chars:
        return text
    truncated = text[:max_chars]
    # Back off to the last space to avoid cutting a word
    last_space = truncated.rfind(" ")
    if last_space > 0:
        truncated = truncated[:last_space]
    return truncated
