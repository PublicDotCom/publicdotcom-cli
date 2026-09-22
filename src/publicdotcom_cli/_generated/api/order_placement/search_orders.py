from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_order_api_query_orders_request import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest,
)
from ...models.com_hellopublic_userapigateway_api_rest_order_v2_gateway_orders import (
    ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/userapigateway/trading/{account_id}/order/v2".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders | None:
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 404:
        response_404 = ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders.from_dict(
            response.json()
        )

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest,
) -> Response[ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders]:
    """Search order details

     Search order details and status for orders fulfilling defined criteria.

    Retrieve up to 500 orders.
    Works only for orders created within last 30 days.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest,
) -> ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders | None:
    """Search order details

     Search order details and status for orders fulfilling defined criteria.

    Retrieve up to 500 orders.
    Works only for orders created within last 30 days.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest,
) -> Response[ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders]:
    """Search order details

     Search order details and status for orders fulfilling defined criteria.

    Retrieve up to 500 orders.
    Works only for orders created within last 30 days.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest,
) -> ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders | None:
    """Search order details

     Search order details and status for orders fulfilling defined criteria.

    Retrieve up to 500 orders.
    Works only for orders created within last 30 days.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
