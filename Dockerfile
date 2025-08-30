# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
  --no-install-recommends \
  curl \
  build-essential \
  git \
  && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

COPY README.md pyproject.toml uv.lock* ./
COPY backend ./backend
RUN uv sync --locked --all-extras

ENV SANBOX_SERVER_PORT=8080
EXPOSE 8080

CMD ["uv", "run", "python", "app.py"]
