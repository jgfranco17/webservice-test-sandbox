from collections import defaultdict
from dataclasses import dataclass

from requests import Response, Session


@dataclass(frozen=True)
class RequestRecord:
    """A record of a request made to the test client."""

    method: str
    path: str
    response: Response


class InternalClient:
    """A simple test client for making HTTP requests."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.__session = Session()
        self.__requests_history = defaultdict(list)

    def __make_registered_request(self, method: str, path: str, **kwargs) -> Response:
        """Register a request made to the client."""
        response = self.__session.request(method, path, **kwargs)
        record = RequestRecord(method, path, response)
        self.__requests_history[path].append(record)
        return response

    def get(self, path: str, **kwargs) -> Response:
        """Make a GET request."""
        url = f"{self.base_url}{path}"
        return self.__make_registered_request("GET", url, **kwargs)

    def post(self, path: str, **kwargs) -> Response:
        """Make a POST request."""
        url = f"{self.base_url}{path}"
        return self.__make_registered_request("POST", url, **kwargs)

    def put(self, path: str, **kwargs) -> Response:
        """Make a PUT request."""
        url = f"{self.base_url}{path}"
        return self.__make_registered_request("PUT", url, **kwargs)

    def delete(self, path: str, **kwargs) -> Response:
        """Make a DELETE request."""
        url = f"{self.base_url}{path}"
        return self.__session.delete(url, **kwargs)

    def patch(self, path: str, **kwargs) -> Response:
        """Make a PATCH request."""
        url = f"{self.base_url}{path}"
        return self.__make_registered_request("PATCH", url, **kwargs)
