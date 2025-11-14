from typing import Final

import pytest
from requests import Session

from tests.testutils.conditions import integration_test

BASE_V0_ENDPOINT: Final[str] = "api/v0/simple"


@integration_test("TC-0003")
def test_addition_success(service_url: str, service_client: Session) -> None:
    """Test the addition endpoint."""
    number_list = [1, 2, 3, 4, 5]
    response = service_client.post(
        f"{service_url}/{BASE_V0_ENDPOINT}/add", json={"numbers": number_list}
    )
    assert response.status_code == 200
    assert response.json()["sum"] == 15


@integration_test("TC-0004")
@pytest.mark.slow
def test_delay_success(service_url: str, service_client: Session) -> None:
    """Test the delay endpoint."""
    delay_seconds = 3
    response = service_client.get(
        f"{service_url}/{BASE_V0_ENDPOINT}/delay?seconds={delay_seconds}"
    )
    assert response.status_code == 200
