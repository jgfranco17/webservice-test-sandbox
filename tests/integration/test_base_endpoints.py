import pytest
from requests import Session

from tests.testutils.conditions import integration_test


@integration_test("TC-0001")
def test_root(service_url: str, service_client: Session) -> None:
    """Test the root endpoint."""
    response = service_client.get(f"{service_url}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sandbox API!"}


@integration_test("TC-0002")
def test_health_check(service_url: str, service_client: Session) -> None:
    """Test the root endpoint."""
    response = service_client.get(f"{service_url}/healthz")
    assert response.status_code == 200
    json_output = response.json()
    assert json_output["status"] == "healthy"
