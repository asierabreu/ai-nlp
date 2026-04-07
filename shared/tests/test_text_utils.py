"""Tests for shared text utilities."""

import pytest

from utils.text import clean_text, tokenize, truncate


def test_clean_text_strips_whitespace():
    assert clean_text("  hello  ") == "hello"


def test_clean_text_collapses_spaces():
    assert clean_text("hello   world") == "hello world"


def test_clean_text_empty():
    assert clean_text("") == ""


def test_tokenize_basic():
    assert tokenize("hello world") == ["hello", "world"]


def test_tokenize_lower():
    assert tokenize("Hello World", lower=True) == ["hello", "world"]


def test_truncate_short():
    text = "hello"
    assert truncate(text, max_chars=100) == "hello"


def test_truncate_long():
    text = "the quick brown fox jumped over the lazy dog"
    result = truncate(text, max_chars=15)
    assert len(result) <= 15
    # Should not cut in the middle of a word; backs off to last space
    assert result == "the quick"
