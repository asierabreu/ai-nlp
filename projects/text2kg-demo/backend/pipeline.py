"""Core text-to-knowledge-graph pipeline."""

from __future__ import annotations

from typing import Any, Dict, List

import spacy


_nlp = None


def _get_nlp() -> spacy.Language:
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp


def extract_graph(text: str) -> Dict[str, List[Any]]:
    """Run the full text-to-KG pipeline on the input text.

    Args:
        text: Raw input text.

    Returns:
        Dictionary with 'entities' and 'relations' lists.
    """
    nlp = _get_nlp()
    doc = nlp(text)

    entities = [
        {"text": ent.text, "label": ent.label_}
        for ent in doc.ents
    ]

    # Simple co-occurrence relations within sentences
    relations: List[Dict[str, str]] = []
    for sent in doc.sents:
        sent_ents = [e for e in doc.ents if e.sent == sent]
        for i, a in enumerate(sent_ents):
            for b in sent_ents[i + 1 :]:
                relations.append(
                    {
                        "subject": a.text,
                        "predicate": "co-occurs-with",
                        "object": b.text,
                    }
                )

    return {"entities": entities, "relations": relations}
