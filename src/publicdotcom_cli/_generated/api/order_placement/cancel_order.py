from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    account_id: str,
    order_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/userapigateway/trading/{account_id}/order/{order_id}".format(
            account_id=quote(str(account_id), safe=""),
            order_id=quote(str(order_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
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
) -> Response[Any]:
    """Request order cancellation

     Submits an asynchronous request to cancel the specified order.

    Note: While most cancellations are processed immediately during market hours, this is not
    guaranteed.
    Always use the GET /{orderId} endpoint to confirm whether the order has been cancelled.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        order_id=order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    account_id: str,
    order_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Request order cancellation

     Submits an asynchronous request to cancel the specified order.

    Note: While most cancellations are processed immediately during market hours, this is not
    guaranteed.
    Always use the GET /{orderId} endpoint to confirm whether the order has been cancelled.

    Args:
        account_id (str):
        order_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
