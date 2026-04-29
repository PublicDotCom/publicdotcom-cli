from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_order_api_instrument_dto import (
    ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto,
)
from ...models.get_instrument_type import GetInstrumentType
from ...types import Response


def _get_kwargs(
    symbol: str,
    type_: GetInstrumentType,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/instruments/{symbol}/{type_}".format(
            symbol=quote(str(symbol), safe=""),
            type_=quote(str(type_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto | None:
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    symbol: str,
    type_: GetInstrumentType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto]:
    """
    Args:
        symbol (str):
        type_ (GetInstrumentType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    type_: GetInstrumentType,
    *,
    client: AuthenticatedClient | Client,
) -> ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto | None:
    """
    Args:
        symbol (str):
        type_ (GetInstrumentType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto
    """

    return sync_detailed(
        symbol=symbol,
        type_=type_,
        client=client,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    type_: GetInstrumentType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto]:
    """
    Args:
        symbol (str):
        type_ (GetInstrumentType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    type_: GetInstrumentType,
    *,
    client: AuthenticatedClient | Client,
) -> ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto | None:
    """
    Args:
        symbol (str):
        type_ (GetInstrumentType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            type_=type_,
            client=client,
        )
    ).parsed
