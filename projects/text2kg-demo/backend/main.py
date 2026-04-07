"""FastAPI application for the Text-to-Knowledge-Graph demo."""

from __future__ import annotations

from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .pipeline import extract_graph

app = FastAPI(
    title="Text-to-Knowledge-Graph API",
    description="Extract knowledge graphs from text using NLP and LLMs.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextInput(BaseModel):
    text: str


class EntityOut(BaseModel):
    text: str
    label: str


class RelationOut(BaseModel):
    subject: str
    predicate: str
    object: str


class GraphOut(BaseModel):
    entities: List[EntityOut]
    relations: List[RelationOut]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/extract", response_model=GraphOut)
def extract(payload: TextInput) -> GraphOut:
    """Extract a knowledge graph from the provided text."""
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="text must not be empty")

    result = extract_graph(payload.text)
    return GraphOut(
        entities=[EntityOut(**e) for e in result["entities"]],
        relations=[RelationOut(**r) for r in result["relations"]],
    )
