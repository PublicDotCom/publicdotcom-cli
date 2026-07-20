from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_request import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest,
)
from ...models.com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_response import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/userapigateway/trading/{account_id}/preflight/multi-leg".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse | None:
    if response.status_code == 200:
        response_200 = (
            ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse.from_dict(
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
) -> Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse]:
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
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest,
) -> Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse]:
    """Calculates the estimated financial impact of a complex multi-leg trade before execution

     Performs preflight calculations for a multi-leg order (a transaction involving multiple securities
    or options strategies such as spreads, straddles, or combinations) to provide comprehensive cost
    estimates and account impact details. Returns estimated commission, regulatory fees, total order
    value, buying power requirements, margin impact, net credit/debit amounts, and strategy-specific
    information to help users make informed trading decisions before order placement. This endpoint
    handles complex options strategies and calculates the combined effect of all legs in the trade. Note
    that these are estimates only, and actual execution values may vary depending on market conditions
    and fill prices. This endpoint may be called before submitting an actual multi-leg order to
    understand the potential financial implications of the strategy.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest): #
            PreflightMultiLegRequest
            Request for preflight calculations on multi-leg orders.

            ## Fields
            - **orderType** - The type of order (only LIMIT orders are allowed for multi-leg)
            - **expiration** - The order expiration configuration
            - **quantity** - The order quantity (number of strategies)
            - **limitPrice** - The limit price for the order (required for LIMIT orders)
            - **legs** - List of order legs (2-6 legs allowed, at most 1 equity leg)
            - **equityMarketSession** - The market session for equity legs
            - **validateOrder** - If true, the order will be validated against current account state.
            Defaults to true.
            - **useMargin** - If false, the order will be evaluated using cash-only buying power
            instead of margin buying power when available. This parameter only has an effect when
            validateOrder is true and the account has margin enabled. Defaults to true.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest,
) -> Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse | None:
    """Calculates the estimated financial impact of a complex multi-leg trade before execution

     Performs preflight calculations for a multi-leg order (a transaction involving multiple securities
    or options strategies such as spreads, straddles, or combinations) to provide comprehensive cost
    estimates and account impact details. Returns estimated commission, regulatory fees, total order
    value, buying power requirements, margin impact, net credit/debit amounts, and strategy-specific
    information to help users make informed trading decisions before order placement. This endpoint
    handles complex options strategies and calculates the combined effect of all legs in the trade. Note
    that these are estimates only, and actual execution values may vary depending on market conditions
    and fill prices. This endpoint may be called before submitting an actual multi-leg order to
    understand the potential financial implications of the strategy.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest): #
            PreflightMultiLegRequest
            Request for preflight calculations on multi-leg orders.

            ## Fields
            - **orderType** - The type of order (only LIMIT orders are allowed for multi-leg)
            - **expiration** - The order expiration configuration
            - **quantity** - The order quantity (number of strategies)
            - **limitPrice** - The limit price for the order (required for LIMIT orders)
            - **legs** - List of order legs (2-6 legs allowed, at most 1 equity leg)
            - **equityMarketSession** - The market session for equity legs
            - **validateOrder** - If true, the order will be validated against current account state.
            Defaults to true.
            - **useMargin** - If false, the order will be evaluated using cash-only buying power
            instead of margin buying power when available. This parameter only has an effect when
            validateOrder is true and the account has margin enabled. Defaults to true.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest,
) -> Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse]:
    """Calculates the estimated financial impact of a complex multi-leg trade before execution

     Performs preflight calculations for a multi-leg order (a transaction involving multiple securities
    or options strategies such as spreads, straddles, or combinations) to provide comprehensive cost
    estimates and account impact details. Returns estimated commission, regulatory fees, total order
    value, buying power requirements, margin impact, net credit/debit amounts, and strategy-specific
    information to help users make informed trading decisions before order placement. This endpoint
    handles complex options strategies and calculates the combined effect of all legs in the trade. Note
    that these are estimates only, and actual execution values may vary depending on market conditions
    and fill prices. This endpoint may be called before submitting an actual multi-leg order to
    understand the potential financial implications of the strategy.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest): #
            PreflightMultiLegRequest
            Request for preflight calculations on multi-leg orders.

            ## Fields
            - **orderType** - The type of order (only LIMIT orders are allowed for multi-leg)
            - **expiration** - The order expiration configuration
            - **quantity** - The order quantity (number of strategies)
            - **limitPrice** - The limit price for the order (required for LIMIT orders)
            - **legs** - List of order legs (2-6 legs allowed, at most 1 equity leg)
            - **equityMarketSession** - The market session for equity legs
            - **validateOrder** - If true, the order will be validated against current account state.
            Defaults to true.
            - **useMargin** - If false, the order will be evaluated using cash-only buying power
            instead of margin buying power when available. This parameter only has an effect when
            validateOrder is true and the account has margin enabled. Defaults to true.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest,
) -> Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse | None:
    """Calculates the estimated financial impact of a complex multi-leg trade before execution

     Performs preflight calculations for a multi-leg order (a transaction involving multiple securities
    or options strategies such as spreads, straddles, or combinations) to provide comprehensive cost
    estimates and account impact details. Returns estimated commission, regulatory fees, total order
    value, buying power requirements, margin impact, net credit/debit amounts, and strategy-specific
    information to help users make informed trading decisions before order placement. This endpoint
    handles complex options strategies and calculates the combined effect of all legs in the trade. Note
    that these are estimates only, and actual execution values may vary depending on market conditions
    and fill prices. This endpoint may be called before submitting an actual multi-leg order to
    understand the potential financial implications of the strategy.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest): #
            PreflightMultiLegRequest
            Request for preflight calculations on multi-leg orders.

            ## Fields
            - **orderType** - The type of order (only LIMIT orders are allowed for multi-leg)
            - **expiration** - The order expiration configuration
            - **quantity** - The order quantity (number of strategies)
            - **limitPrice** - The limit price for the order (required for LIMIT orders)
            - **legs** - List of order legs (2-6 legs allowed, at most 1 equity leg)
            - **equityMarketSession** - The market session for equity legs
            - **validateOrder** - If true, the order will be validated against current account state.
            Defaults to true.
            - **useMargin** - If false, the order will be evaluated using cash-only buying power
            instead of margin buying power when available. This parameter only has an effect when
            validateOrder is true and the account has margin enabled. Defaults to true.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
