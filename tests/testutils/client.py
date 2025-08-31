from typing import Any, Dict
from urllib.parse import urljoin

from requests import Session

JsonResponse = Dict[str, Any]


class ServiceClient:
    """A client for interacting with the service during testing."""

    def __init__(self, base_url: str, max_timeout: int = 5) -> None:
        self.__base_url = base_url
        self.__max_timeout = max_timeout
        self.__expecting_error = False
        self.__expected_fields: Dict[str, Any] = dict()

        # Use dedicated session for all requests
        self.session = Session()
        self.session.headers.update({"Accept": "application/json"})

    @property
    def url(self) -> str:
        """Get the base URL of the service."""
        return self.__base_url

    def expect_error(self, expected_fields: Dict[str, Any]) -> None:
        """Configure the client to expect an error response."""
        self.__expecting_error = True
        self.__expected_fields = expected_fields

    def __make_request(self, method: str, path: str, **kwargs) -> JsonResponse:
        full_url = urljoin(self.__base_url, path)
        response = self.session.request(
            method.upper(), full_url, timeout=self.__max_timeout, **kwargs
        )
        if not self.__expecting_error:
            response.raise_for_status()
        json_response = response.json()
        if self.__expected_fields:
            for field, value in self.__expected_fields.items():
                assert json_response[field] == value
        return json_response

    def get(self, path: str, **kwargs: Dict[str, Any]) -> JsonResponse:
        """Make a GET request to the service."""
        return self.__make_request(method="GET", path=path, **kwargs)

    def post(self, path: str, **kwargs: Dict[str, Any]) -> JsonResponse:
        """Make a POST request to the service."""
        return self.__make_request(method="POST", path=path, **kwargs)

    def put(self, path: str, **kwargs: Dict[str, Any]) -> JsonResponse:
        """Make a PUT request to the service."""
        return self.__make_request(method="PUT", path=path, **kwargs)

    def delete(self, path: str, **kwargs: Dict[str, Any]) -> JsonResponse:
        """Make a DELETE request to the service."""
        return self.__make_request(method="DELETE", path=path, **kwargs)
