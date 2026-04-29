from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_order_api_instrument_response import (
    ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse,
)
from ...models.get_all_instruments_fractional_trading_filter_item import (
    GetAllInstrumentsFractionalTradingFilterItem,
)
from ...models.get_all_instruments_option_spread_trading_filter_item import (
    GetAllInstrumentsOptionSpreadTradingFilterItem,
)
from ...models.get_all_instruments_option_trading_filter_item import (
    GetAllInstrumentsOptionTradingFilterItem,
)
from ...models.get_all_instruments_trading_filter_item import GetAllInstrumentsTradingFilterItem
from ...models.get_all_instruments_type_filter_item import GetAllInstrumentsTypeFilterItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_filter: list[GetAllInstrumentsTypeFilterItem] | Unset = UNSET,
    trading_filter: list[GetAllInstrumentsTradingFilterItem] | Unset = UNSET,
    fractional_trading_filter: list[GetAllInstrumentsFractionalTradingFilterItem] | Unset = UNSET,
    option_trading_filter: list[GetAllInstrumentsOptionTradingFilterItem] | Unset = UNSET,
    option_spread_trading_filter: list[GetAllInstrumentsOptionSpreadTradingFilterItem]
    | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_filter: list[str] | Unset = UNSET
    if not isinstance(type_filter, Unset):
        json_type_filter = []
        for type_filter_item_data in type_filter:
            type_filter_item = type_filter_item_data.value
            json_type_filter.append(type_filter_item)

    params["typeFilter"] = json_type_filter

    json_trading_filter: list[str] | Unset = UNSET
    if not isinstance(trading_filter, Unset):
        json_trading_filter = []
        for trading_filter_item_data in trading_filter:
            trading_filter_item = trading_filter_item_data.value
            json_trading_filter.append(trading_filter_item)

    params["tradingFilter"] = json_trading_filter

    json_fractional_trading_filter: list[str] | Unset = UNSET
    if not isinstance(fractional_trading_filter, Unset):
        json_fractional_trading_filter = []
        for fractional_trading_filter_item_data in fractional_trading_filter:
            fractional_trading_filter_item = fractional_trading_filter_item_data.value
            json_fractional_trading_filter.append(fractional_trading_filter_item)

    params["fractionalTradingFilter"] = json_fractional_trading_filter

    json_option_trading_filter: list[str] | Unset = UNSET
    if not isinstance(option_trading_filter, Unset):
        json_option_trading_filter = []
        for option_trading_filter_item_data in option_trading_filter:
            option_trading_filter_item = option_trading_filter_item_data.value
            json_option_trading_filter.append(option_trading_filter_item)

    params["optionTradingFilter"] = json_option_trading_filter

    json_option_spread_trading_filter: list[str] | Unset = UNSET
    if not isinstance(option_spread_trading_filter, Unset):
        json_option_spread_trading_filter = []
        for option_spread_trading_filter_item_data in option_spread_trading_filter:
            option_spread_trading_filter_item = option_spread_trading_filter_item_data.value
            json_option_spread_trading_filter.append(option_spread_trading_filter_item)

    params["optionSpreadTradingFilter"] = json_option_spread_trading_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/instruments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse | None:
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_filter: list[GetAllInstrumentsTypeFilterItem] | Unset = UNSET,
    trading_filter: list[GetAllInstrumentsTradingFilterItem] | Unset = UNSET,
    fractional_trading_filter: list[GetAllInstrumentsFractionalTradingFilterItem] | Unset = UNSET,
    option_trading_filter: list[GetAllInstrumentsOptionTradingFilterItem] | Unset = UNSET,
    option_spread_trading_filter: list[GetAllInstrumentsOptionSpreadTradingFilterItem]
    | Unset = UNSET,
) -> Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse]:
    """Retrieves all available trading instruments with optional filtering capabilities.

     Retrieves all available trading instruments with optional filtering capabilities.

    This endpoint returns a comprehensive list of instruments available for trading,
    with support for filtering by security type and various trading capabilities.
    All filter parameters are optional and can be combined to narrow down results.

    Args:
        type_filter (list[GetAllInstrumentsTypeFilterItem] | Unset):
        trading_filter (list[GetAllInstrumentsTradingFilterItem] | Unset):
        fractional_trading_filter (list[GetAllInstrumentsFractionalTradingFilterItem] | Unset):
        option_trading_filter (list[GetAllInstrumentsOptionTradingFilterItem] | Unset):
        option_spread_trading_filter (list[GetAllInstrumentsOptionSpreadTradingFilterItem] |
            Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse]
    """

    kwargs = _get_kwargs(
        type_filter=type_filter,
        trading_filter=trading_filter,
        fractional_trading_filter=fractional_trading_filter,
        option_trading_filter=option_trading_filter,
        option_spread_trading_filter=option_spread_trading_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_filter: list[GetAllInstrumentsTypeFilterItem] | Unset = UNSET,
    trading_filter: list[GetAllInstrumentsTradingFilterItem] | Unset = UNSET,
    fractional_trading_filter: list[GetAllInstrumentsFractionalTradingFilterItem] | Unset = UNSET,
    option_trading_filter: list[GetAllInstrumentsOptionTradingFilterItem] | Unset = UNSET,
    option_spread_trading_filter: list[GetAllInstrumentsOptionSpreadTradingFilterItem]
    | Unset = UNSET,
) -> ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse | None:
    """Retrieves all available trading instruments with optional filtering capabilities.

     Retrieves all available trading instruments with optional filtering capabilities.

    This endpoint returns a comprehensive list of instruments available for trading,
    with support for filtering by security type and various trading capabilities.
    All filter parameters are optional and can be combined to narrow down results.

    Args:
        type_filter (list[GetAllInstrumentsTypeFilterItem] | Unset):
        trading_filter (list[GetAllInstrumentsTradingFilterItem] | Unset):
        fractional_trading_filter (list[GetAllInstrumentsFractionalTradingFilterItem] | Unset):
        option_trading_filter (list[GetAllInstrumentsOptionTradingFilterItem] | Unset):
        option_spread_trading_filter (list[GetAllInstrumentsOptionSpreadTradingFilterItem] |
            Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse
    """

    return sync_detailed(
        client=client,
        type_filter=type_filter,
        trading_filter=trading_filter,
        fractional_trading_filter=fractional_trading_filter,
        option_trading_filter=option_trading_filter,
        option_spread_trading_filter=option_spread_trading_filter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_filter: list[GetAllInstrumentsTypeFilterItem] | Unset = UNSET,
    trading_filter: list[GetAllInstrumentsTradingFilterItem] | Unset = UNSET,
    fractional_trading_filter: list[GetAllInstrumentsFractionalTradingFilterItem] | Unset = UNSET,
    option_trading_filter: list[GetAllInstrumentsOptionTradingFilterItem] | Unset = UNSET,
    option_spread_trading_filter: list[GetAllInstrumentsOptionSpreadTradingFilterItem]
    | Unset = UNSET,
) -> Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse]:
    """Retrieves all available trading instruments with optional filtering capabilities.

     Retrieves all available trading instruments with optional filtering capabilities.

    This endpoint returns a comprehensive list of instruments available for trading,
    with support for filtering by security type and various trading capabilities.
    All filter parameters are optional and can be combined to narrow down results.

    Args:
        type_filter (list[GetAllInstrumentsTypeFilterItem] | Unset):
        trading_filter (list[GetAllInstrumentsTradingFilterItem] | Unset):
        fractional_trading_filter (list[GetAllInstrumentsFractionalTradingFilterItem] | Unset):
        option_trading_filter (list[GetAllInstrumentsOptionTradingFilterItem] | Unset):
        option_spread_trading_filter (list[GetAllInstrumentsOptionSpreadTradingFilterItem] |
            Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse]
    """

    kwargs = _get_kwargs(
        type_filter=type_filter,
        trading_filter=trading_filter,
        fractional_trading_filter=fractional_trading_filter,
        option_trading_filter=option_trading_filter,
        option_spread_trading_filter=option_spread_trading_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_filter: list[GetAllInstrumentsTypeFilterItem] | Unset = UNSET,
    trading_filter: list[GetAllInstrumentsTradingFilterItem] | Unset = UNSET,
    fractional_trading_filter: list[GetAllInstrumentsFractionalTradingFilterItem] | Unset = UNSET,
    option_trading_filter: list[GetAllInstrumentsOptionTradingFilterItem] | Unset = UNSET,
    option_spread_trading_filter: list[GetAllInstrumentsOptionSpreadTradingFilterItem]
    | Unset = UNSET,
) -> ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse | None:
    """Retrieves all available trading instruments with optional filtering capabilities.

     Retrieves all available trading instruments with optional filtering capabilities.

    This endpoint returns a comprehensive list of instruments available for trading,
    with support for filtering by security type and various trading capabilities.
    All filter parameters are optional and can be combined to narrow down results.

    Args:
        type_filter (list[GetAllInstrumentsTypeFilterItem] | Unset):
        trading_filter (list[GetAllInstrumentsTradingFilterItem] | Unset):
        fractional_trading_filter (list[GetAllInstrumentsFractionalTradingFilterItem] | Unset):
        option_trading_filter (list[GetAllInstrumentsOptionTradingFilterItem] | Unset):
        option_spread_trading_filter (list[GetAllInstrumentsOptionSpreadTradingFilterItem] |
            Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            type_filter=type_filter,
            trading_filter=trading_filter,
            fractional_trading_filter=fractional_trading_filter,
            option_trading_filter=option_trading_filter,
            option_spread_trading_filter=option_spread_trading_filter,
        )
    ).parsed
