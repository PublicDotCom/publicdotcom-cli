from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapiauthservice_api_personal_create_access_token_request import (
    ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest,
)
from ...models.com_hellopublic_userapiauthservice_api_personal_create_access_token_response import (
    ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse,
)
from ...models.com_hellopublic_userapiauthservice_domain_error_error_body import (
    ComHellopublicUserapiauthserviceDomainErrorErrorBody,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/userapiauthservice/personal/access-tokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse
    | ComHellopublicUserapiauthserviceDomainErrorErrorBody
    | None
):
    if response.status_code == 200:
        response_200 = (
            ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 401:
        response_401 = ComHellopublicUserapiauthserviceDomainErrorErrorBody.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 429:
        response_429 = ComHellopublicUserapiauthserviceDomainErrorErrorBody.from_dict(
            response.json()
        )

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse
    | ComHellopublicUserapiauthserviceDomainErrorErrorBody
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest,
) -> Response[
    ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse
    | ComHellopublicUserapiauthserviceDomainErrorErrorBody
]:
    """Create API Access Token

     Generates a new personal Access Token (JWT) with a specified validity in minutes, using an existing
    personal Secret Token. The personal Secret Token must be generated from the user's settings page.
    Secret Tokens are long-lived but revocable, while Access Tokens are short-lived and expire after the
    specified validity period. The Access Token returned from this operation is required for
    authorization in all other subsequent API requests.

    Args:
        body (ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse | ComHellopublicUserapiauthserviceDomainErrorErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest,
) -> (
    ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse
    | ComHellopublicUserapiauthserviceDomainErrorErrorBody
    | None
):
    """Create API Access Token

     Generates a new personal Access Token (JWT) with a specified validity in minutes, using an existing
    personal Secret Token. The personal Secret Token must be generated from the user's settings page.
    Secret Tokens are long-lived but revocable, while Access Tokens are short-lived and expire after the
    specified validity period. The Access Token returned from this operation is required for
    authorization in all other subsequent API requests.

    Args:
        body (ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse | ComHellopublicUserapiauthserviceDomainErrorErrorBody
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest,
) -> Response[
    ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse
    | ComHellopublicUserapiauthserviceDomainErrorErrorBody
]:
    """Create API Access Token

     Generates a new personal Access Token (JWT) with a specified validity in minutes, using an existing
    personal Secret Token. The personal Secret Token must be generated from the user's settings page.
    Secret Tokens are long-lived but revocable, while Access Tokens are short-lived and expire after the
    specified validity period. The Access Token returned from this operation is required for
    authorization in all other subsequent API requests.

    Args:
        body (ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse | ComHellopublicUserapiauthserviceDomainErrorErrorBody]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest,
) -> (
    ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse
    | ComHellopublicUserapiauthserviceDomainErrorErrorBody
    | None
):
    """Create API Access Token

     Generates a new personal Access Token (JWT) with a specified validity in minutes, using an existing
    personal Secret Token. The personal Secret Token must be generated from the user's settings page.
    Secret Tokens are long-lived but revocable, while Access Tokens are short-lived and expire after the
    specified validity period. The Access Token returned from this operation is required for
    authorization in all other subsequent API requests.

    Args:
        body (ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenResponse | ComHellopublicUserapiauthserviceDomainErrorErrorBody
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
