from behave import *  # type: ignore
from requests import HTTPError
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


@then("the response should raise an error")
def step_check_response_error(context: TestContext):
    """Check the response status code."""
    assert context.last_response is not None, "No response available to check"
    try:
        context.last_response.raise_for_status()
        raise AssertionError("Expected an error, but none was raised")
    except HTTPError as e:
        context.last_exception = e


@then("the response body should contain the following key-value pairs")
def step_check_response_content_table(context: TestContext):
    """Check the response content against a table of key-value pairs."""
    assert context.last_response is not None, "No response available to check"
    assert context.table is not None, "No table provided for content checks"

    try:
        response_data = context.last_response.json()
    except Exception as e:
        raise AssertionError(
            f"Response body is not valid JSON: {context.last_response.text}"
        ) from e

    try:
        for row in context.table:
            key = row["key"]
            expected_value = row["value"]

            assert key in response_data, f"Key '{key}' not found in response body"
            actual_value = str(response_data[key])
            assert (
                actual_value == expected_value
            ), f"Expected '{key}' to be '{expected_value}', got '{actual_value}'"
    except KeyError as ke:
        raise AssertionError(f"Error checking response content: {ke}")
