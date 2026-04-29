from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_account_v2 import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/{account_id}/portfolio/v2".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2 | None:
    if response.status_code == 200:
        response_200 = (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 404:
        response_404 = (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2.from_dict(
                response.json()
            )
        )

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2]:
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
) -> Response[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2]:
    """Retrieve an account portfolio details snapshot

     Retrieves a snapshot of a specified account’s portfolio, including positions, equity breakdown,
    buying power, and open orders. The account must exist and belong to the authenticated client.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2]
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
) -> ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2 | None:
    """Retrieve an account portfolio details snapshot

     Retrieves a snapshot of a specified account’s portfolio, including positions, equity breakdown,
    buying power, and open orders. The account must exist and belong to the authenticated client.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2]:
    """Retrieve an account portfolio details snapshot

     Retrieves a snapshot of a specified account’s portfolio, including positions, equity breakdown,
    buying power, and open orders. The account must exist and belong to the authenticated client.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2]
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
) -> ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2 | None:
    """Retrieve an account portfolio details snapshot

     Retrieves a snapshot of a specified account’s portfolio, including positions, equity breakdown,
    buying power, and open orders. The account must exist and belong to the authenticated client.

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
