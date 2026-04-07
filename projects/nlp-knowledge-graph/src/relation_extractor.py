"""Relation extraction between named entities."""

from __future__ import annotations

from typing import List, Tuple

from .ner import Entity


Relation = Tuple[str, str, str]  # (subject, predicate, object)


def extract_relations(
    text: str,
    entities: List[Entity],
) -> List[Relation]:
    """Extract relationships between entities using co-occurrence heuristics.

    This is a placeholder implementation using sentence-level co-occurrence.
    For production use, replace with a proper relation extraction model
    (e.g., a fine-tuned BERT/RoBERTa model).

    Args:
        text: Original input text.
        entities: List of entities extracted from the text.

    Returns:
        List of (subject, predicate, object) relation tuples.
    """
    relations: List[Relation] = []
    # Group entities by sentence
    sentence_entities: dict[str, List[Entity]] = {}
    for ent in entities:
        sentence_entities.setdefault(ent.sentence, []).append(ent)

    # Co-occurrence within the same sentence
    for sentence, ents in sentence_entities.items():
        for i, ent_a in enumerate(ents):
            for ent_b in ents[i + 1 :]:
                relations.append((ent_a.text, "co-occurs-with", ent_b.text))

    return relations
