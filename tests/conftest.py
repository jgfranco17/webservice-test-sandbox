import pytest
from fastapi.testclient import TestClient

from backend.service import app
from tests.testutils.client import InternalClient
from tests.testutils.config import BACKEND_SERVICE_URL


@pytest.fixture
def backend_client() -> TestClient:
    """Create a test client for the backend API."""
    return TestClient(app)


@pytest.fixture(scope="session")
def live_backend_client() -> InternalClient:
    """Create a test client for the live instance of the backend."""
    return InternalClient(BACKEND_SERVICE_URL)
