from dataclasses import dataclass

from requests import Response, Session


@dataclass
class RequestRecord:
    method: str
    url: str
    kwargs: dict
    response: Response


Record = list[RequestRecord]


class ServiceClient:
    """A simple wrapper around Session to interact with the web service."""

    def __init__(self, port: int = 8080):
        self.base_url = f"http://localhost:{port}"
        self.session = Session()
        self.session.headers.update({"Accept": "application/json"})
        self._records: Record = []

    def make_simple_request(self, method: str, endpoint: str, **kwargs):
        """Make a request and record it."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        return response

    def make_recorded_request(self, method: str, endpoint: str, **kwargs):
        """Make a request and record it."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        record = RequestRecord(method, url, kwargs, response)
        self._records.append(record)
        return response

    def get_requests_by_endpoint(self, endpoint: str):
        """Retrieve all requests made to a specific endpoint."""
        return [r for r in self._records if r.url.endswith(endpoint)]

    def close(self):
        """Close the session."""
        self.session.close()
