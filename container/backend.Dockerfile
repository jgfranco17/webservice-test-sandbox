# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim AS setup

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

FROM setup AS app

WORKDIR /server

COPY README.md pyproject.toml uv.lock* ./
COPY backend ./backend
RUN uv sync --locked --all-extras

ENV SANBOX_SERVER_PORT=8080
EXPOSE 8080

COPY app.py ./app.py

CMD ["uv", "run", "python", "app.py"]

HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 \
    CMD [ "curl", "--fail", "-s", "localhost:8080/healthz" ]
