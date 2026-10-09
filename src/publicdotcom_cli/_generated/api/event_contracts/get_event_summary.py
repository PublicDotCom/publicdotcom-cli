from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_request_dto import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto,
)
from ...models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_list_dto import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto,
)
from ...types import Response


def _get_kwargs(
    *,
    body: ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/userapigateway/eventcontract/summary",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto
    | None
):
    if response.status_code == 200:
        response_200 = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto.from_dict(
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
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto,
) -> Response[
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto
]:
    """Get Event Summary

     Returns a paginated list of event summaries, optionally limited to a category and filtered by
    eventSymbol or frequency. Each result includes the event's symbol, title, volume and status. Use the
    returned eventSymbol with Get Event Details to fetch outcomes, contracts and pricing. Results can
    include resolved and halted events. Up to 100 events are returned per page; to fetch the next page,
    send the same request with the nextToken from the previous response.

    Args:
        body (ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSumma
            ryUserApiRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto,
) -> (
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto
    | None
):
    """Get Event Summary

     Returns a paginated list of event summaries, optionally limited to a category and filtered by
    eventSymbol or frequency. Each result includes the event's symbol, title, volume and status. Use the
    returned eventSymbol with Get Event Details to fetch outcomes, contracts and pricing. Results can
    include resolved and halted events. Up to 100 events are returned per page; to fetch the next page,
    send the same request with the nextToken from the previous response.

    Args:
        body (ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSumma
            ryUserApiRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto,
) -> Response[
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto
]:
    """Get Event Summary

     Returns a paginated list of event summaries, optionally limited to a category and filtered by
    eventSymbol or frequency. Each result includes the event's symbol, title, volume and status. Use the
    returned eventSymbol with Get Event Details to fetch outcomes, contracts and pricing. Results can
    include resolved and halted events. Up to 100 events are returned per page; to fetch the next page,
    send the same request with the nextToken from the previous response.

    Args:
        body (ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSumma
            ryUserApiRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto,
) -> (
    Any
    | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto
    | None
):
    """Get Event Summary

     Returns a paginated list of event summaries, optionally limited to a category and filtered by
    eventSymbol or frequency. Each result includes the event's symbol, title, volume and status. Use the
    returned eventSymbol with Get Event Details to fetch outcomes, contracts and pricing. Results can
    include resolved and halted events. Up to 100 events are returned per page; to fetch the next page,
    send the same request with the nextToken from the previous response.

    Args:
        body (ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSumma
            ryUserApiRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
