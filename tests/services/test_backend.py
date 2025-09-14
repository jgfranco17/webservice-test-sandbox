import time

import pytest
from fastapi.testclient import TestClient


class TestCorePatterns:
    """Basic testing patterns and examples."""

    def test_simple_get_request(self, backend_client: TestClient):
        """Example: Simple GET request test."""
        response = backend_client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()

    def test_response_structure(self, backend_client: TestClient):
        """Example: Testing response structure and content."""
        response = backend_client.get("/healthz")
        assert response.json() == {"status": "healthy"}

    def test_multiple_endpoints(self, backend_client: TestClient):
        """Example: Testing multiple endpoints in one test."""
        endpoints = ["/", "/healthz", "/service-info"]

        for endpoint in endpoints:
            response = backend_client.get(endpoint)
            assert response.status_code == 200
            assert isinstance(response.json(), dict)

    @pytest.mark.parametrize(
        "endpoint,expected_status",
        [
            ("/", 200),
            ("/healthz", 200),
            ("/service-info", 200),
            ("/non-existent", 404),
        ],
    )
    def test_endpoint_status_codes(self, backend_client, endpoint, expected_status):
        """Example: Parametrized test for multiple endpoints."""
        response = backend_client.get(endpoint)
        assert response.status_code == expected_status

    @pytest.mark.parametrize(
        "endpoint,expected_key",
        [
            ("/", "message"),
            ("/healthz", "status"),
            ("/service-info", "name"),
        ],
    )
    def test_endpoint_response_keys(self, backend_client, endpoint, expected_key):
        """Example: Parametrized test for response keys."""
        response = backend_client.get(endpoint)
        assert response.status_code == 200
        assert expected_key in response.json()


class TestErrorHandling:
    """Examples of testing error scenarios."""

    def test_404_error(self, backend_client: TestClient):
        """Example: Testing 404 error handling."""
        response = backend_client.get("/non-existent-endpoint")
        assert response.status_code == 404

    def test_invalid_method(self, backend_client: TestClient):
        """Example: Testing invalid HTTP method."""
        # This would typically return 405 Method Not Allowed
        # but FastAPI might handle it differently
        response = backend_client.post("/")
        # The actual status code depends on FastAPI's behavior
        assert response.status_code in [405, 422]


class TestPerformance:
    """Examples of performance testing."""

    MAX_RESPONSE_TIME_MS = 1000

    def test_response_time(self, backend_client: TestClient):
        """Example: Testing response time."""
        start_time = time.time()
        response = backend_client.get("/healthz")
        end_time = time.time()

        response_time = (end_time - start_time) / 1000

        assert response.status_code == 200
        assert response_time < self.MAX_RESPONSE_TIME_MS
