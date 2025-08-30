from typing import Iterator

import pytest
from fastapi.testclient import TestClient
from requests import Session

from backend.service import app


@pytest.fixture
def client() -> TestClient:
    """Create a direct client to run against the app."""
    return TestClient(app)


@pytest.fixture
def service_url() -> str:
    """Get the address of the running webservice."""
    return "http://localhost:8080"


@pytest.fixture
def service_client(service_url: str) -> Iterator[Session]:
    """
    Fixture that provides a configured requests.Session
    pointing to the FastAPI service.
    """
    session = Session()
    session.headers.update({"Accept": "application/json"})
    yield session
