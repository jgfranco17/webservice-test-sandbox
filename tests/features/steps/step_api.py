from behave import *  # type: ignore
from requests.exceptions import ConnectionError

from tests.shared.stubs import TestContext


@given("the server is running")
def step_check_service(context: TestContext):
    """Ensure the server is running."""
    try:
        response = context.client.make_simple_request("GET", "/healthz")
    except ConnectionError as e:
        raise AssertionError("Could not connect to the server") from e
    assert response.ok, f"Server returned HTTP {response.status_code}"


@when('I make a {method} request to the "{endpoint}" endpoint')
def step_make_request(context: TestContext, method: str, endpoint: str):
    """Make a request to the server."""
    try:
        response = context.client.make_recorded_request(method.upper(), endpoint)
        context.last_response = response
    except ConnectionError as e:
        raise AssertionError("Could not connect to the server") from e


@then("the response status code should be {status_code:d}")
def step_check_status_code(context: TestContext, status_code: int):
    """Check the response status code."""
    assert context.last_response is not None, "No response available to check"
    assert (
        context.last_response.status_code == status_code
    ), f"Expected status code {status_code}, got {context.last_response.status_code}"
