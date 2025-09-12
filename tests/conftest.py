import pytest
import requests
from testutils.client import TestClient


@pytest.fixture(scope="session")
def backend_client():
    """Create a test client for the backend API."""
    return TestClient(base_url="http://localhost:8080")


@pytest.fixture(scope="session")
def frontend_client():
    """Create a test client for the frontend application."""
    return TestClient(base_url="http://localhost:3000")


@pytest.fixture(scope="session")
def backend_available(backend_client):
    """Check if the backend is available and skip tests if not."""
    try:
        response = backend_client.get("/healthz", timeout=5)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass

    pytest.skip("Backend not available. Start the backend with: python -m backend.main")


@pytest.fixture(scope="session")
def frontend_available(frontend_client):
    """Check if the frontend is available and skip tests if not."""
    try:
        response = frontend_client.get("/", timeout=5)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        pass

    pytest.skip("Frontend not available. Start the frontend with: npm run dev")
