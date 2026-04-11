"""Prometheus metric definitions and payload generation for serving endpoints.

The module declares shared counters and histograms used by the API layer to
track request volume and latency. It also provides a helper that exports the
latest registry snapshot with the content type expected by Prometheus scrapers.
"""

from __future__ import annotations

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

REQUEST_COUNT = Counter("scientific_llm_requests_total", "Total number of generation requests")
REQUEST_LATENCY = Histogram("scientific_llm_request_latency_seconds", "Generation request latency")


def metrics_payload() -> tuple[bytes, str]:
    return generate_latest(), CONTENT_TYPE_LATEST
