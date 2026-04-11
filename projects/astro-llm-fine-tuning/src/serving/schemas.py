"""Pydantic request and response schemas for text-generation endpoints.

The schema definitions enforce input constraints such as token limits and
temperature bounds while documenting the public API contract. Response models
standardize output fields returned by synchronous generation requests.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1)
    max_tokens: int = Field(default=128, ge=1, le=4096)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    stream: bool = False


class GenerateResponse(BaseModel):
    text: str
    model: str
    backend: str
