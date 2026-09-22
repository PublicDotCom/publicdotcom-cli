from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_order_v2_gateway_order_v2 import (
    ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    order_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/{account_id}/order/v2/{order_id}".format(
            account_id=quote(str(account_id), safe=""),
            order_id=quote(str(order_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2 | None:
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    order_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2]:
    """Retrieve order details

     Fetches the status and details of a specific order for the given account.
    Works only for orders created within last 30 days.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        order_id=order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    order_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2 | None:
    """Retrieve order details

     Fetches the status and details of a specific order for the given account.
    Works only for orders created within last 30 days.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2
    """

    return sync_detailed(
        account_id=account_id,
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    order_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2]:
    """Retrieve order details

     Fetches the status and details of a specific order for the given account.
    Works only for orders created within last 30 days.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    order_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2 | None:
    """Retrieve order details

     Fetches the status and details of a specific order for the given account.
    Works only for orders created within last 30 days.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            order_id=order_id,
            client=client,
        )
    ).parsed
