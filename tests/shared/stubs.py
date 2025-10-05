from behave.runner import Context
from requests import Response

from tests.shared.client import ServiceClient


class TestContext(Context):
    """File context interface for development and testing."""

    client: ServiceClient
    last_response: Response | None
    last_exception: Exception | None
