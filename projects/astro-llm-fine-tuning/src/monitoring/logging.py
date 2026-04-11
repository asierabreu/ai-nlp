"""Structured logging configuration for service and training processes.

`configure_structured_logging` installs a JSON formatter on the root logger,
replacing previous handlers to ensure consistent machine-readable output. This
supports log aggregation systems and improves observability in containerized
deployments.
"""

from __future__ import annotations

import logging
from pythonjsonlogger import jsonlogger


def configure_structured_logging() -> None:
    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(logging.INFO)
