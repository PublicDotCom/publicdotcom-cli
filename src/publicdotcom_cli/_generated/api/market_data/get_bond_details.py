from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_marketdata_bonddetails_bond_details_response import (
    ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    symbol: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/marketdata/{account_id}/bond-details/{symbol}".format(
            account_id=quote(str(account_id), safe=""),
            symbol=quote(str(symbol), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse | None:
    if response.status_code == 200:
        response_200 = (
            ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse.from_dict(
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
) -> Response[Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse]:
    """Retrieve bond details

     Returns comprehensive bond instrument details including pricing, ratings, and maturity information.
    Requires the `marketdata` scope. Available to individual investors.

    Args:
        account_id (str):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        symbol=symbol,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse | None:
    """Retrieve bond details

     Returns comprehensive bond instrument details including pricing, ratings, and maturity information.
    Requires the `marketdata` scope. Available to individual investors.

    Args:
        account_id (str):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse
    """

    return sync_detailed(
        account_id=account_id,
        symbol=symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse]:
    """Retrieve bond details

     Returns comprehensive bond instrument details including pricing, ratings, and maturity information.
    Requires the `marketdata` scope. Available to individual investors.

    Args:
        account_id (str):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        symbol=symbol,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse | None:
    """Retrieve bond details

     Returns comprehensive bond instrument details including pricing, ratings, and maturity information.
    Requires the `marketdata` scope. Available to individual investors.

    Args:
        account_id (str):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            symbol=symbol,
            client=client,
        )
    ).parsed
