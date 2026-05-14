from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bars_response import BarsResponse
from ...models.get_bars_v2_period import GetBarsV2Period
from ...models.get_bars_v2_type import GetBarsV2Type
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_: GetBarsV2Type,
    symbol: str,
    period: GetBarsV2Period,
    *,
    purchase_date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["purchaseDate"] = purchase_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/historicdata/{type_}/{symbol}/{period}".format(
            type_=quote(str(type_), safe=""),
            symbol=quote(str(symbol), safe=""),
            period=quote(str(period), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BarsResponse | None:
    if response.status_code == 200:
        response_200 = BarsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BarsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: GetBarsV2Type,
    symbol: str,
    period: GetBarsV2Period,
    *,
    client: AuthenticatedClient | Client,
    purchase_date: str | Unset = UNSET,
) -> Response[BarsResponse]:
    """Fetch bar data for a given symbol and period

    Args:
        type_ (GetBarsV2Type):
        symbol (str):
        period (GetBarsV2Period):
        purchase_date (str | Unset):  Example: 2025-02-24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BarsResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        symbol=symbol,
        period=period,
        purchase_date=purchase_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: GetBarsV2Type,
    symbol: str,
    period: GetBarsV2Period,
    *,
    client: AuthenticatedClient | Client,
    purchase_date: str | Unset = UNSET,
) -> BarsResponse | None:
    """Fetch bar data for a given symbol and period

    Args:
        type_ (GetBarsV2Type):
        symbol (str):
        period (GetBarsV2Period):
        purchase_date (str | Unset):  Example: 2025-02-24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BarsResponse
    """

    return sync_detailed(
        type_=type_,
        symbol=symbol,
        period=period,
        client=client,
        purchase_date=purchase_date,
    ).parsed


async def asyncio_detailed(
    type_: GetBarsV2Type,
    symbol: str,
    period: GetBarsV2Period,
    *,
    client: AuthenticatedClient | Client,
    purchase_date: str | Unset = UNSET,
) -> Response[BarsResponse]:
    """Fetch bar data for a given symbol and period

    Args:
        type_ (GetBarsV2Type):
        symbol (str):
        period (GetBarsV2Period):
        purchase_date (str | Unset):  Example: 2025-02-24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BarsResponse]
    """

    kwargs = _get_kwargs(
        type_=type_,
        symbol=symbol,
        period=period,
        purchase_date=purchase_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: GetBarsV2Type,
    symbol: str,
    period: GetBarsV2Period,
    *,
    client: AuthenticatedClient | Client,
    purchase_date: str | Unset = UNSET,
) -> BarsResponse | None:
    """Fetch bar data for a given symbol and period

    Args:
        type_ (GetBarsV2Type):
        symbol (str):
        period (GetBarsV2Period):
        purchase_date (str | Unset):  Example: 2025-02-24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BarsResponse
    """

    return (
        await asyncio_detailed(
            type_=type_,
            symbol=symbol,
            period=period,
            client=client,
            purchase_date=purchase_date,
        )
    ).parsed
