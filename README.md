# Webservice Test Sandbox

This is a simple web service to run tests against.

## Requirements

- [Just](https://just.systems/man/en/) (script runner)
- [Docker with Compose plugin](https://docs.docker.com/compose/install/) (for containerization)
- [UV package manager](https://docs.astral.sh/uv/getting-started/installation/) (for Python development)

## Setup

The following steps will get you up and running with the project.
To get started, clone the repository to your local machine.

```bash
git clone https://github.com/jgfranco17/webservice-test-sandbox.git
```

## Backend Development

1. Install dependencies

   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

2. Run the backend application

   ```bash
   just run
   ```

## Containerization

The project can run in a containerized environment using Docker Compose.

```bash
docker compose build
docker compose up
```
