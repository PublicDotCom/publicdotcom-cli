from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_hstier_2_service_taxlots_api_unrealized_lots_summary_response import (
    ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/{account_id}/taxlots/unrealized".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse | None:
    if response.status_code == 200:
        response_200 = (
            ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse.from_dict(
                response.json()
            )
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
) -> Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse]:
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
) -> Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse]:
    """Retrieve unrealized tax lots

     Returns an overview of unrealized tax lots for the specified account. Requires the `portfolio`
    scope. Available to individual investors.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse | None:
    """Retrieve unrealized tax lots

     Returns an overview of unrealized tax lots for the specified account. Requires the `portfolio`
    scope. Available to individual investors.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse]:
    """Retrieve unrealized tax lots

     Returns an overview of unrealized tax lots for the specified account. Requires the `portfolio`
    scope. Available to individual investors.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse | None:
    """Retrieve unrealized tax lots

     Returns an overview of unrealized tax lots for the specified account. Requires the `portfolio`
    scope. Available to individual investors.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
