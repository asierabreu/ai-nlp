"""Tests for domain-specific evaluation metrics."""

import pytest

from evaluation.metrics import exact_match, token_f1


def test_exact_match_perfect():
    preds = ["The answer is 42", "Paris"]
    refs = ["The answer is 42", "Paris"]
    assert exact_match(preds, refs) == 1.0


def test_exact_match_none():
    preds = ["wrong", "incorrect"]
    refs = ["correct", "right"]
    assert exact_match(preds, refs) == 0.0


def test_exact_match_partial():
    preds = ["yes", "no"]
    refs = ["yes", "yes"]
    assert exact_match(preds, refs) == 0.5


def test_exact_match_invalid():
    with pytest.raises(ValueError):
        exact_match([], [])


def test_token_f1_perfect():
    assert token_f1("hello world", "hello world") == 1.0


def test_token_f1_no_overlap():
    assert token_f1("foo bar", "baz qux") == 0.0


def test_token_f1_partial():
    score = token_f1("the cat sat", "the dog sat")
    assert 0.0 < score < 1.0
