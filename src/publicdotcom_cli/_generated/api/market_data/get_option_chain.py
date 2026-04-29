from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_chain_request import (
    ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest,
)
from ...models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_chain_response import (
    ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/userapigateway/marketdata/{account_id}/option-chain".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse | None:
    if response.status_code == 200:
        response_200 = (
            ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse.from_dict(
                response.json()
            )
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
) -> Response[Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse]:
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
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest,
) -> Response[Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse]:
    """Retrieve option chain

     Returns the option chain for a given instrument. Requires the `marketdata` scope. Available to
    individual investors. Supported types: EQUITY, UNDERLYING_SECURITY_FOR_INDEX_OPTION.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse]
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
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest,
) -> Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse | None:
    """Retrieve option chain

     Returns the option chain for a given instrument. Requires the `marketdata` scope. Available to
    individual investors. Supported types: EQUITY, UNDERLYING_SECURITY_FOR_INDEX_OPTION.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse
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
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest,
) -> Response[Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse]:
    """Retrieve option chain

     Returns the option chain for a given instrument. Requires the `marketdata` scope. Available to
    individual investors. Supported types: EQUITY, UNDERLYING_SECURITY_FOR_INDEX_OPTION.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse]
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
    body: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest,
) -> Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse | None:
    """Retrieve option chain

     Returns the option chain for a given instrument. Requires the `marketdata` scope. Available to
    individual investors. Supported types: EQUITY, UNDERLYING_SECURITY_FOR_INDEX_OPTION.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
