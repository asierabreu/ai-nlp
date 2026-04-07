"""Tests for the text2kg pipeline."""

import pytest

from backend.pipeline import extract_graph


def test_extract_graph_returns_structure():
    result = extract_graph("Apple was founded by Steve Jobs.")
    assert "entities" in result
    assert "relations" in result
    assert isinstance(result["entities"], list)
    assert isinstance(result["relations"], list)


def test_extract_graph_empty_text():
    result = extract_graph("")
    assert result["entities"] == []
    assert result["relations"] == []
