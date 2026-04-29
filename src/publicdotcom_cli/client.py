from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx


class MissingTokenError(RuntimeError):
    """Raised when a secured API endpoint is called without an access token."""


@dataclass
class ApiError(RuntimeError):
    method: str
    path: str
    status_code: int
    body: Any

    def __str__(self) -> str:
        return f"{self.method.upper()} {self.path} failed with HTTP {self.status_code}"


def _response_body(response: httpx.Response) -> Any:
    if not response.content:
        return None
    try:
        return response.json()
    except ValueError:
        return response.text


def compact_params(params: dict[str, Any] | None) -> list[tuple[str, Any]]:
    if not params:
        return []

    compacted: list[tuple[str, Any]] = []
    for key, value in params.items():
        if value is None or value == []:
            continue
        if isinstance(value, list):
            compacted.extend((key, item) for item in value)
        else:
            compacted.append((key, value))
    return compacted


class ApiClient:
    def __init__(self, *, base_url: str, token: str | None, timeout: float) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: Any | None = None,
        authenticated: bool = True,
    ) -> Any:
        headers = {"Accept": "application/json"}
        if authenticated:
            if not self.token:
                raise MissingTokenError(
                    "No access token found. Run `public auth login` or set PUBLIC_ACCESS_TOKEN."
                )
            headers["Authorization"] = f"Bearer {self.token}"

        with httpx.Client(base_url=self.base_url, timeout=self.timeout) as client:
            response = client.request(
                method,
                path,
                params=compact_params(params),
                json=json_body,
                headers=headers,
            )

        body = _response_body(response)
        if response.status_code >= 400:
            raise ApiError(method=method, path=path, status_code=response.status_code, body=body)
        return body
