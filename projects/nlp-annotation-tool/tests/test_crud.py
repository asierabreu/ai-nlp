"""Tests for annotation tool models."""

from backend.models import Annotation, Document


def test_document_to_jsonl():
    doc = Document(
        id="doc1",
        text="Apple was founded by Steve Jobs.",
        annotations=[Annotation(text="Apple", start=0, end=5, label="ORG")],
    )
    data = doc.to_jsonl()
    assert data["id"] == "doc1"
    assert len(data["entities"]) == 1
    assert data["entities"][0]["label"] == "ORG"


def test_document_to_jsonl_empty():
    doc = Document(id="doc2", text="No entities here.")
    data = doc.to_jsonl()
    assert data["entities"] == []
