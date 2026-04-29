import datetime
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_history_gateway_history_response_page import (
    ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = UNSET,
    next_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: str | Unset = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["pageSize"] = page_size

    params["nextToken"] = next_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/{account_id}/history".format(
            account_id=quote(str(account_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage | None:
    if response.status_code == 200:
        response_200 = (
            ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage.from_dict(
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
) -> Response[Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage]:
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
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = UNSET,
    next_token: str | Unset = UNSET,
) -> Response[Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage]:
    """Retrieve account history

     Fetches a paginated list of historical events for the specified account. Supports optional time
    range filtering and pagination via a continuation token.

    Args:
        account_id (str):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        page_size (int | Unset):
        next_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        start=start,
        end=end,
        page_size=page_size,
        next_token=next_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = UNSET,
    next_token: str | Unset = UNSET,
) -> Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage | None:
    """Retrieve account history

     Fetches a paginated list of historical events for the specified account. Supports optional time
    range filtering and pagination via a continuation token.

    Args:
        account_id (str):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        page_size (int | Unset):
        next_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        start=start,
        end=end,
        page_size=page_size,
        next_token=next_token,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = UNSET,
    next_token: str | Unset = UNSET,
) -> Response[Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage]:
    """Retrieve account history

     Fetches a paginated list of historical events for the specified account. Supports optional time
    range filtering and pagination via a continuation token.

    Args:
        account_id (str):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        page_size (int | Unset):
        next_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        start=start,
        end=end,
        page_size=page_size,
        next_token=next_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    page_size: int | Unset = UNSET,
    next_token: str | Unset = UNSET,
) -> Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage | None:
    """Retrieve account history

     Fetches a paginated list of historical events for the specified account. Supports optional time
    range filtering and pagination via a continuation token.

    Args:
        account_id (str):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        page_size (int | Unset):
        next_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            start=start,
            end=end,
            page_size=page_size,
            next_token=next_token,
        )
    ).parsed
