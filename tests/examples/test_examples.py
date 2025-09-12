"""
Example test patterns for the Webservice Test Sandbox.
These examples demonstrate various testing techniques and patterns.
"""

import time

import pytest
from testutils.client import TestClient


class TestBasicPatterns:
    """Basic testing patterns and examples."""

    def test_simple_get_request(self, backend_client):
        """Example: Simple GET request test."""
        response = backend_client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()

    def test_response_structure(self, backend_client):
        """Example: Testing response structure and content."""
        response = backend_client.get("/healthz")
        data = response.json()

        # Test response structure
        assert isinstance(data, dict)
        assert "status" in data

        # Test specific values
        assert data["status"] == "healthy"

    def test_multiple_endpoints(self, backend_client):
        """Example: Testing multiple endpoints in one test."""
        endpoints = ["/", "/healthz", "/service-info"]

        for endpoint in endpoints:
            response = backend_client.get(endpoint)
            assert response.status_code == 200
            assert isinstance(response.json(), dict)


class TestErrorHandling:
    """Examples of testing error scenarios."""

    def test_404_error(self, backend_client):
        """Example: Testing 404 error handling."""
        response = backend_client.get("/non-existent-endpoint")
        assert response.status_code == 404

        # Test error response structure
        data = response.json()
        assert "message" in data
        assert "request_info" in data

    def test_invalid_method(self, backend_client):
        """Example: Testing invalid HTTP method."""
        # This would typically return 405 Method Not Allowed
        # but FastAPI might handle it differently
        response = backend_client.post("/")
        # The actual status code depends on FastAPI's behavior
        assert response.status_code in [405, 422]


class TestPerformance:
    """Examples of performance testing."""

    def test_response_time(self, backend_client):
        """Example: Testing response time."""
        start_time = time.time()
        response = backend_client.get("/healthz")
        end_time = time.time()

        response_time = end_time - start_time

        assert response.status_code == 200
        assert response_time < 1.0  # Should respond within 1 second

    def test_concurrent_requests(self, backend_client):
        """Example: Testing concurrent requests."""
        import concurrent.futures

        def make_request():
            return backend_client.get("/healthz")

        # Make 10 concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(10)]
            results = [future.result() for future in futures]

        # All requests should succeed
        for response in results:
            assert response.status_code == 200
            assert response.json()["status"] == "healthy"


class TestDataValidation:
    """Examples of data validation testing."""

    def test_service_info_data_types(self, backend_client):
        """Example: Testing data types in response."""
        response = backend_client.get("/service-info")
        data = response.json()

        # Test data types
        assert isinstance(data["name"], str)
        assert isinstance(data["description"], str)
        assert isinstance(data["uptime_seconds"], (int, float))

        # Test value ranges
        assert data["uptime_seconds"] >= 0
        assert len(data["name"]) > 0
        assert len(data["description"]) > 0

    def test_health_check_consistency(self, backend_client):
        """Example: Testing response consistency."""
        # Make multiple requests to ensure consistency
        for _ in range(5):
            response = backend_client.get("/healthz")
            assert response.status_code == 200
            assert response.json()["status"] == "healthy"


class TestIntegration:
    """Examples of integration testing."""

    def test_frontend_backend_integration(self, frontend_client, backend_client):
        """Example: Testing frontend-backend integration."""
        # Test backend directly
        backend_response = backend_client.get("/healthz")
        assert backend_response.status_code == 200

        # Test frontend proxy
        frontend_response = frontend_client.get("/api/healthz")
        assert frontend_response.status_code == 200

        # Compare responses
        assert backend_response.json() == frontend_response.json()

    def test_api_proxy_consistency(self, frontend_client, backend_client):
        """Example: Testing API proxy consistency."""
        endpoints = ["/", "/healthz", "/service-info"]

        for endpoint in endpoints:
            # Test backend directly
            backend_response = backend_client.get(endpoint)

            # Test through frontend proxy
            frontend_response = frontend_client.get(f"/api{endpoint}")

            # Responses should be identical
            assert backend_response.status_code == frontend_response.status_code
            assert backend_response.json() == frontend_response.json()


class TestParametrized:
    """Examples of parametrized testing."""

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


class TestFixtures:
    """Examples of using fixtures effectively."""

    def test_with_custom_fixture(self, backend_client):
        """Example: Using custom fixtures."""
        # This test uses the backend_client fixture from conftest.py
        response = backend_client.get("/healthz")
        assert response.status_code == 200

    def test_multiple_clients(self, backend_client, frontend_client):
        """Example: Using multiple fixtures."""
        # Test both clients
        backend_response = backend_client.get("/")
        frontend_response = frontend_client.get("/api/")

        assert backend_response.status_code == 200
        assert frontend_response.status_code == 200
