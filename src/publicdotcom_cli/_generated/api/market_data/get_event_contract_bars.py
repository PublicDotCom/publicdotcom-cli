from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_contract_charts_response import EventContractChartsResponse
from ...models.get_event_contract_bars_period import GetEventContractBarsPeriod
from ...types import UNSET, Response


def _get_kwargs(
    event_id: str,
    period: GetEventContractBarsPeriod,
    *,
    symbols: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["symbols"] = symbols

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/historicdata/event-contracts/{event_id}/bars/{period}".format(
            event_id=quote(str(event_id), safe=""),
            period=quote(str(period), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EventContractChartsResponse | None:
    if response.status_code == 200:
        response_200 = EventContractChartsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EventContractChartsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    period: GetEventContractBarsPeriod,
    *,
    client: AuthenticatedClient | Client,
    symbols: str,
) -> Response[Any | EventContractChartsResponse]:
    """Fetch chart bars for event contracts

    Args:
        event_id (str):  Example: KALSHI.KXBALANCESHEET-EO26-EVENT.
        period (GetEventContractBarsPeriod):
        symbols (str):  Example: KALSHI.KXBALANCESHEET-EO26-6.6.Y-EVENTCONTRACT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EventContractChartsResponse]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        period=period,
        symbols=symbols,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    period: GetEventContractBarsPeriod,
    *,
    client: AuthenticatedClient | Client,
    symbols: str,
) -> Any | EventContractChartsResponse | None:
    """Fetch chart bars for event contracts

    Args:
        event_id (str):  Example: KALSHI.KXBALANCESHEET-EO26-EVENT.
        period (GetEventContractBarsPeriod):
        symbols (str):  Example: KALSHI.KXBALANCESHEET-EO26-6.6.Y-EVENTCONTRACT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EventContractChartsResponse
    """

    return sync_detailed(
        event_id=event_id,
        period=period,
        client=client,
        symbols=symbols,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    period: GetEventContractBarsPeriod,
    *,
    client: AuthenticatedClient | Client,
    symbols: str,
) -> Response[Any | EventContractChartsResponse]:
    """Fetch chart bars for event contracts

    Args:
        event_id (str):  Example: KALSHI.KXBALANCESHEET-EO26-EVENT.
        period (GetEventContractBarsPeriod):
        symbols (str):  Example: KALSHI.KXBALANCESHEET-EO26-6.6.Y-EVENTCONTRACT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EventContractChartsResponse]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        period=period,
        symbols=symbols,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    period: GetEventContractBarsPeriod,
    *,
    client: AuthenticatedClient | Client,
    symbols: str,
) -> Any | EventContractChartsResponse | None:
    """Fetch chart bars for event contracts

    Args:
        event_id (str):  Example: KALSHI.KXBALANCESHEET-EO26-EVENT.
        period (GetEventContractBarsPeriod):
        symbols (str):  Example: KALSHI.KXBALANCESHEET-EO26-6.6.Y-EVENTCONTRACT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EventContractChartsResponse
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            period=period,
            client=client,
            symbols=symbols,
        )
    ).parsed
