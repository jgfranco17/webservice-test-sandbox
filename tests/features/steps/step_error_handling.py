from behave import *  # type: ignore

from tests.shared.stubs import TestContext


@when("I try: {step}")
def step_try_step(context: TestContext, step: str):
    """Executes a step safely and captures any Exception raised."""
    try:
        context.execute_steps(step)
        context.last_exception = None
    except Exception as e:
        # Capture the exception for later assertions
        context.last_exception = e


@then("no error is raised")
def step_no_error(context: TestContext):
    """Verifies that no error was raised in the last 'try' step."""
    assert (
        context.last_exception is None
    ), f"Error was raised, but was not expected: {str(context.last_exception)}"


@then("the error message contains: {message}")
def step_error_traceback_contains(context: TestContext, message: str):
    """Verifies that an error was raised with the specified message."""
    assert (
        context.last_exception is not None
    ), "No error was raised, but one was expected."
    error_message = str(context.last_exception)
    assert (
        message in error_message
    ), f"Expected error message to contain '{message}', but got:\n{error_message}"


@then("an error is raised")
def step_error_is_raised(context: TestContext):
    """Verifies that an error was raised in the last 'try' step."""
    assert (
        context.last_exception is not None
    ), "No error was raised, but one was expected."
