from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_order_api_cancel_replace_order_request import (
    ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest,
)
from ...models.com_hellopublic_userapigateway_api_rest_order_api_order_result import (
    ComHellopublicUserapigatewayApiRestOrderApiOrderResult,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/userapigateway/trading/{account_id}/order".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult | None:
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestOrderApiOrderResult.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult]:
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
    body: ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest,
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult]:
    """Cancel-Replace an existing order

     Submits a request to replace an existing order asynchronously for the specified account.

    Note: Order replacement is asynchronous. This response confirms submission only.
    To verify the order status or execution details, use the GET /{orderId} endpoint after replacement.
    This feature is only available for crypto quantity orders and option orders. Equities coming soon.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest): Used for
            replacing orders placed via the UserApiGatewayService or other service
            Replaces should not be placed in parallel as ordering is not guaranteed for individual
            HTTP calls

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult]
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
    body: ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest,
) -> Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult | None:
    """Cancel-Replace an existing order

     Submits a request to replace an existing order asynchronously for the specified account.

    Note: Order replacement is asynchronous. This response confirms submission only.
    To verify the order status or execution details, use the GET /{orderId} endpoint after replacement.
    This feature is only available for crypto quantity orders and option orders. Equities coming soon.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest): Used for
            replacing orders placed via the UserApiGatewayService or other service
            Replaces should not be placed in parallel as ordering is not guaranteed for individual
            HTTP calls

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult
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
    body: ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest,
) -> Response[Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult]:
    """Cancel-Replace an existing order

     Submits a request to replace an existing order asynchronously for the specified account.

    Note: Order replacement is asynchronous. This response confirms submission only.
    To verify the order status or execution details, use the GET /{orderId} endpoint after replacement.
    This feature is only available for crypto quantity orders and option orders. Equities coming soon.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest): Used for
            replacing orders placed via the UserApiGatewayService or other service
            Replaces should not be placed in parallel as ordering is not guaranteed for individual
            HTTP calls

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult]
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
    body: ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest,
) -> Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult | None:
    """Cancel-Replace an existing order

     Submits a request to replace an existing order asynchronously for the specified account.

    Note: Order replacement is asynchronous. This response confirms submission only.
    To verify the order status or execution details, use the GET /{orderId} endpoint after replacement.
    This feature is only available for crypto quantity orders and option orders. Equities coming soon.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest): Used for
            replacing orders placed via the UserApiGatewayService or other service
            Replaces should not be placed in parallel as ordering is not guaranteed for individual
            HTTP calls

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestOrderApiOrderResult
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
