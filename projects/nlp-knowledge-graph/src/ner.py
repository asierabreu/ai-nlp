"""Named Entity Recognition utilities."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

import spacy


@dataclass
class Entity:
    """Represents an extracted entity."""

    text: str
    label: str
    start: int
    end: int
    sentence: str = ""


def load_nlp_model(model_name: str = "en_core_web_sm") -> spacy.Language:
    """Load a spaCy NLP model."""
    return spacy.load(model_name)


def extract_entities(text: str, model_name: str = "en_core_web_sm") -> List[Entity]:
    """Extract named entities from the given text.

    Args:
        text: Input text to process.
        model_name: spaCy model to use for NER.

    Returns:
        List of Entity objects found in the text.
    """
    nlp = load_nlp_model(model_name)
    doc = nlp(text)

    entities: List[Entity] = []
    for ent in doc.ents:
        sentence = ent.sent.text.strip()
        entities.append(
            Entity(
                text=ent.text,
                label=ent.label_,
                start=ent.start_char,
                end=ent.end_char,
                sentence=sentence,
            )
        )

    return entities
