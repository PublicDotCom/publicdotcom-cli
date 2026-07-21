from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_hstier_2_service_taxlots_api_unrealized_lots_detail_response import (
    ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    symbol: str,
    *,
    price: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["price"] = price

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/{account_id}/taxlots/unrealized/{symbol}".format(
            account_id=quote(str(account_id), safe=""),
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse | None:
    if response.status_code == 200:
        response_200 = ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse.from_dict(
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
) -> Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse]:
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
    price: str | Unset = UNSET,
) -> Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse]:
    """Retrieve unrealized tax lots for a specific symbol

     Returns detailed unrealized tax lots for a specific symbol in the account. Requires the `portfolio`
    scope. Available to individual investors.

    Args:
        account_id (str):
        symbol (str):
        price (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        symbol=symbol,
        price=price,
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
    price: str | Unset = UNSET,
) -> Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse | None:
    """Retrieve unrealized tax lots for a specific symbol

     Returns detailed unrealized tax lots for a specific symbol in the account. Requires the `portfolio`
    scope. Available to individual investors.

    Args:
        account_id (str):
        symbol (str):
        price (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse
    """

    return sync_detailed(
        account_id=account_id,
        symbol=symbol,
        client=client,
        price=price,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    price: str | Unset = UNSET,
) -> Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse]:
    """Retrieve unrealized tax lots for a specific symbol

     Returns detailed unrealized tax lots for a specific symbol in the account. Requires the `portfolio`
    scope. Available to individual investors.

    Args:
        account_id (str):
        symbol (str):
        price (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        symbol=symbol,
        price=price,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    price: str | Unset = UNSET,
) -> Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse | None:
    """Retrieve unrealized tax lots for a specific symbol

     Returns detailed unrealized tax lots for a specific symbol in the account. Requires the `portfolio`
    scope. Available to individual investors.

    Args:
        account_id (str):
        symbol (str):
        price (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            symbol=symbol,
            client=client,
            price=price,
        )
    ).parsed
