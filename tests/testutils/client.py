"""
Test client utilities for making HTTP requests in tests.
"""

from typing import Any, Dict, Optional

import requests


class TestClient:
    """A simple test client for making HTTP requests."""

    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, path: str, **kwargs) -> requests.Response:
        """Make a GET request."""
        url = f"{self.base_url}{path}"
        return self.session.get(url, timeout=self.timeout, **kwargs)

    def post(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> requests.Response:
        """Make a POST request."""
        url = f"{self.base_url}{path}"
        return self.session.post(
            url, data=data, json=json, timeout=self.timeout, **kwargs
        )

    def put(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> requests.Response:
        """Make a PUT request."""
        url = f"{self.base_url}{path}"
        return self.session.put(
            url, data=data, json=json, timeout=self.timeout, **kwargs
        )

    def delete(self, path: str, **kwargs) -> requests.Response:
        """Make a DELETE request."""
        url = f"{self.base_url}{path}"
        return self.session.delete(url, timeout=self.timeout, **kwargs)

    def patch(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> requests.Response:
        """Make a PATCH request."""
        url = f"{self.base_url}{path}"
        return self.session.patch(
            url, data=data, json=json, timeout=self.timeout, **kwargs
        )
