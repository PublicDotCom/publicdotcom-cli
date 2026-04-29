from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_options_greeks_response import (
    ComHellopublicUserapigatewayApiRestOptionsGreeksResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    account_id: str,
    *,
    osi_symbols: list[str],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_osi_symbols = osi_symbols

    params["osiSymbols"] = json_osi_symbols

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/option-details/{account_id}/greeks".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ComHellopublicUserapigatewayApiRestOptionsGreeksResponse | None:
    if response.status_code == 200:
        response_200 = ComHellopublicUserapigatewayApiRestOptionsGreeksResponse.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ComHellopublicUserapigatewayApiRestOptionsGreeksResponse]:
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
    osi_symbols: list[str],
) -> Response[ComHellopublicUserapigatewayApiRestOptionsGreeksResponse]:
    """Get option greeks

     Get the greeks for a list of option symbol in the OSI-normalized format. Max 250 contracts per
    request.

    Args:
        account_id (str):
        osi_symbols (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestOptionsGreeksResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        osi_symbols=osi_symbols,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    osi_symbols: list[str],
) -> ComHellopublicUserapigatewayApiRestOptionsGreeksResponse | None:
    """Get option greeks

     Get the greeks for a list of option symbol in the OSI-normalized format. Max 250 contracts per
    request.

    Args:
        account_id (str):
        osi_symbols (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestOptionsGreeksResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        osi_symbols=osi_symbols,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    osi_symbols: list[str],
) -> Response[ComHellopublicUserapigatewayApiRestOptionsGreeksResponse]:
    """Get option greeks

     Get the greeks for a list of option symbol in the OSI-normalized format. Max 250 contracts per
    request.

    Args:
        account_id (str):
        osi_symbols (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestOptionsGreeksResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        osi_symbols=osi_symbols,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    osi_symbols: list[str],
) -> ComHellopublicUserapigatewayApiRestOptionsGreeksResponse | None:
    """Get option greeks

     Get the greeks for a list of option symbol in the OSI-normalized format. Max 250 contracts per
    request.

    Args:
        account_id (str):
        osi_symbols (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestOptionsGreeksResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            osi_symbols=osi_symbols,
        )
    ).parsed
