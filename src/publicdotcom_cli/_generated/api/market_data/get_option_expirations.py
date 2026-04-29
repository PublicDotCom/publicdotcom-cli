from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_expirations_request import (
    ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest,
)
from ...models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_expirations_response import (
    ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/userapigateway/marketdata/{account_id}/option-expirations".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse | None
):
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse.from_dict(
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
) -> Response[
    Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse
]:
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
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest,
) -> Response[
    Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse
]:
    """Retrieve option expiration dates

     Returns available option expiration dates for a given instrument. Requires the `marketdata` scope.
    Available to individual investors. Supported types: EQUITY, UNDERLYING_SECURITY_FOR_INDEX_OPTION.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse]
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
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest,
) -> (
    Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse | None
):
    """Retrieve option expiration dates

     Returns available option expiration dates for a given instrument. Requires the `marketdata` scope.
    Available to individual investors. Supported types: EQUITY, UNDERLYING_SECURITY_FOR_INDEX_OPTION.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse
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
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest,
) -> Response[
    Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse
]:
    """Retrieve option expiration dates

     Returns available option expiration dates for a given instrument. Requires the `marketdata` scope.
    Available to individual investors. Supported types: EQUITY, UNDERLYING_SECURITY_FOR_INDEX_OPTION.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse]
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
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest,
) -> (
    Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse | None
):
    """Retrieve option expiration dates

     Returns available option expiration dates for a given instrument. Requires the `marketdata` scope.
    Available to individual investors. Supported types: EQUITY, UNDERLYING_SECURITY_FOR_INDEX_OPTION.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
