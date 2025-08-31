from typing import Iterator

import pytest
from fastapi.testclient import TestClient
from requests import Session

from backend.service import app
from tests.testutils.client import ServiceClient


@pytest.fixture
def client() -> TestClient:
    """Create a direct client to run against the app."""
    return TestClient(app)


@pytest.fixture
def service_url() -> str:
    """Get the address of the running webservice."""
    return "http://localhost:8080"


@pytest.fixture
def service_client(service_url: str) -> Iterator[ServiceClient]:
    """
    Fixture that provides a configured requests.Session
    pointing to the FastAPI service.
    """
    client = ServiceClient(service_url)
    yield client
