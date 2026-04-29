from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_order_gateway_order import (
    ComHellopublicUserapigatewayApiRestOrderGatewayOrder,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    order_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/{account_id}/order/{order_id}".format(
            account_id=quote(str(account_id), safe=""),
            order_id=quote(str(order_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder | None:
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestOrderGatewayOrder.from_dict(
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
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder]:
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
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder]:
    """Retrieve order details

     Fetches the status and details of a specific order for the given account.

    Note: Order placement is asynchronous. This endpoint may return HTTP 404 if the order has not yet
    been indexed for retrieval.
    In some cases, the order may already be active in the market but momentarily not yet visible through
    this API due to eventual consistency.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder]
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
) -> Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder | None:
    """Retrieve order details

     Fetches the status and details of a specific order for the given account.

    Note: Order placement is asynchronous. This endpoint may return HTTP 404 if the order has not yet
    been indexed for retrieval.
    In some cases, the order may already be active in the market but momentarily not yet visible through
    this API due to eventual consistency.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder
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
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder]:
    """Retrieve order details

     Fetches the status and details of a specific order for the given account.

    Note: Order placement is asynchronous. This endpoint may return HTTP 404 if the order has not yet
    been indexed for retrieval.
    In some cases, the order may already be active in the market but momentarily not yet visible through
    this API due to eventual consistency.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder]
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
) -> Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder | None:
    """Retrieve order details

     Fetches the status and details of a specific order for the given account.

    Note: Order placement is asynchronous. This endpoint may return HTTP 404 if the order has not yet
    been indexed for retrieval.
    In some cases, the order may already be active in the market but momentarily not yet visible through
    this API due to eventual consistency.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestOrderGatewayOrder
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            order_id=order_id,
            client=client,
        )
    ).parsed
