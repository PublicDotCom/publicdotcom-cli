from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_user_api_dto import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_symbol: str,
    *,
    include_all_outcomes: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeAllOutcomes"] = include_all_outcomes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/eventcontract/details/{event_symbol}".format(
            event_symbol=quote(str(event_symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto
    | None
):
    if response.status_code == 200:
        response_200 = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto.from_dict(
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
    Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_symbol: str,
    *,
    client: AuthenticatedClient | Client,
    include_all_outcomes: bool | Unset = True,
) -> Response[
    Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto
]:
    """Get Event Details

     Returns full details for a single event: its outcomes, the YES/NO contracts for each outcome with
    current pricing, the trading timeline, and the CFTC contract terms. The eventSymbol comes from Get
    Event Summary. Returns 400 with code 7004 if no event matches the eventSymbol.

    Args:
        event_symbol (str):
        include_all_outcomes (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto]
    """

    kwargs = _get_kwargs(
        event_symbol=event_symbol,
        include_all_outcomes=include_all_outcomes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_symbol: str,
    *,
    client: AuthenticatedClient | Client,
    include_all_outcomes: bool | Unset = True,
) -> (
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto
    | None
):
    """Get Event Details

     Returns full details for a single event: its outcomes, the YES/NO contracts for each outcome with
    current pricing, the trading timeline, and the CFTC contract terms. The eventSymbol comes from Get
    Event Summary. Returns 400 with code 7004 if no event matches the eventSymbol.

    Args:
        event_symbol (str):
        include_all_outcomes (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto
    """

    return sync_detailed(
        event_symbol=event_symbol,
        client=client,
        include_all_outcomes=include_all_outcomes,
    ).parsed


async def asyncio_detailed(
    event_symbol: str,
    *,
    client: AuthenticatedClient | Client,
    include_all_outcomes: bool | Unset = True,
) -> Response[
    Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto
]:
    """Get Event Details

     Returns full details for a single event: its outcomes, the YES/NO contracts for each outcome with
    current pricing, the trading timeline, and the CFTC contract terms. The eventSymbol comes from Get
    Event Summary. Returns 400 with code 7004 if no event matches the eventSymbol.

    Args:
        event_symbol (str):
        include_all_outcomes (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto]
    """

    kwargs = _get_kwargs(
        event_symbol=event_symbol,
        include_all_outcomes=include_all_outcomes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_symbol: str,
    *,
    client: AuthenticatedClient | Client,
    include_all_outcomes: bool | Unset = True,
) -> (
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto
    | None
):
    """Get Event Details

     Returns full details for a single event: its outcomes, the YES/NO contracts for each outcome with
    current pricing, the trading timeline, and the CFTC contract terms. The eventSymbol comes from Get
    Event Summary. Returns 400 with code 7004 if no event matches the eventSymbol.

    Args:
        event_symbol (str):
        include_all_outcomes (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto
    """

    return (
        await asyncio_detailed(
            event_symbol=event_symbol,
            client=client,
            include_all_outcomes=include_all_outcomes,
        )
    ).parsed
