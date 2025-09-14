from tests.testutils.client import InternalClient
from tests.testutils.conditions import integration_test


@integration_test("TC-0001")
def test_root(live_backend_client: InternalClient) -> None:
    """Test the root endpoint."""
    response = live_backend_client.get("/")
    assert response.status_code == 200


@integration_test("TC-0002")
def test_health_check(live_backend_client: InternalClient) -> None:
    """Test the root endpoint."""
    response = live_backend_client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
