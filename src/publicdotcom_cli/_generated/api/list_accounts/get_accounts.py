from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_account_account_settings_response import (
    ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/account",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse | None:
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse]:
    """Get accounts

     Retrieves the list of financial accounts associated with the authenticated user.
    This includes brokerage, retirement, and high-yield cash accounts.

    The response contains account objects that represent each available account.

    Note: The `accountId` returned by this endpoint is required for most subsequent API operations.
    It serves as a stable, persistent identifier for the lifetime of the account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse | None:
    """Get accounts

     Retrieves the list of financial accounts associated with the authenticated user.
    This includes brokerage, retirement, and high-yield cash accounts.

    The response contains account objects that represent each available account.

    Note: The `accountId` returned by this endpoint is required for most subsequent API operations.
    It serves as a stable, persistent identifier for the lifetime of the account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse]:
    """Get accounts

     Retrieves the list of financial accounts associated with the authenticated user.
    This includes brokerage, retirement, and high-yield cash accounts.

    The response contains account objects that represent each available account.

    Note: The `accountId` returned by this endpoint is required for most subsequent API operations.
    It serves as a stable, persistent identifier for the lifetime of the account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse | None:
    """Get accounts

     Retrieves the list of financial accounts associated with the authenticated user.
    This includes brokerage, retirement, and high-yield cash accounts.

    The response contains account objects that represent each available account.

    Note: The `accountId` returned by this endpoint is required for most subsequent API operations.
    It serves as a stable, persistent identifier for the lifetime of the account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
