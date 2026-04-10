from __future__ import annotations

import logging
import os
import time
from typing import AsyncIterator

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, StreamingResponse

from src.inference.engine import InferenceEngine
from src.monitoring.logging import configure_structured_logging
from src.monitoring.metrics import REQUEST_COUNT, REQUEST_LATENCY, metrics_payload
from src.serving.schemas import GenerateRequest, GenerateResponse

configure_structured_logging()
logger = logging.getLogger(__name__)

MODEL_NAME = os.getenv("MODEL_NAME", "gpt2")
BACKEND = os.getenv("INFERENCE_BACKEND", "hf")

app = FastAPI(title="Scientific LLM Finetunning API", version="0.1.0")
_engine: InferenceEngine | None = None


def get_engine() -> InferenceEngine:
    global _engine
    if _engine is None:
        _engine = InferenceEngine(model_name=MODEL_NAME, backend=BACKEND)
    return _engine


@app.get("/health")
async def health() -> dict[str, str]:
    backend = _engine.backend if _engine else BACKEND
    return {"status": "ok", "model": MODEL_NAME, "backend": backend}


@app.get("/metrics")
async def metrics() -> Response:
    payload, content_type = metrics_payload()
    return Response(content=payload, media_type=content_type)


@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    engine = get_engine()
    REQUEST_COUNT.inc()
    start = time.perf_counter()

    if request.stream:
        async def token_stream() -> AsyncIterator[str]:
            for token in engine.stream(request.prompt, max_tokens=request.max_tokens):
                yield token

        return StreamingResponse(token_stream(), media_type="text/plain")

    try:
        text = engine.generate(
            prompt=request.prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
        )
        return GenerateResponse(text=text, model=MODEL_NAME, backend=engine.backend)
    except Exception as exc:
        logger.exception("generation_failed")
        return JSONResponse(status_code=500, content={"error": str(exc)})
    finally:
        REQUEST_LATENCY.observe(time.perf_counter() - start)
