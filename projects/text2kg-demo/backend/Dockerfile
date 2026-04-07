# syntax=docker/dockerfile:1

FROM python:3.10-slim

WORKDIR /app

# Install system dependencies required by spaCy / PyTorch, plus curl for health checks
RUN apt-get update && apt-get install -y --no-install-recommends \
      gcc \
      g++ \
      build-essential \
      curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from the project-level requirements file.
# The build context is set to the project root (projects/text2kg-demo) so
# that requirements.txt is accessible here.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY backend/ ./backend/

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
