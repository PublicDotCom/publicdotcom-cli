from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_request import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest,
)
from ...models.com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_response import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse,
)
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/userapigateway/trading/{account_id}/preflight/single-leg".format(
            account_id=quote(str(account_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse | None:
    if response.status_code == 200:
        response_200 = (
            ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse.from_dict(
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
) -> Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse]:
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
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest,
) -> Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse]:
    """Calculates the estimated financial impact of a potential trade before execution

     Performs preflight calculations for a single-leg order (a transaction involving a single security)
    to provide comprehensive cost estimates and account impact details. Returns estimated commission,
    regulatory fees, order value, buying power requirements, margin impact, and other trade-specific
    information to help users make informed trading decisions before order placement. Note that these
    are estimates only, and actual execution values may vary depending on market conditions. This
    endpoint may be called before submitting an actual order to understand the potential financial
    implications.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse]
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
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest,
) -> Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse | None:
    """Calculates the estimated financial impact of a potential trade before execution

     Performs preflight calculations for a single-leg order (a transaction involving a single security)
    to provide comprehensive cost estimates and account impact details. Returns estimated commission,
    regulatory fees, order value, buying power requirements, margin impact, and other trade-specific
    information to help users make informed trading decisions before order placement. Note that these
    are estimates only, and actual execution values may vary depending on market conditions. This
    endpoint may be called before submitting an actual order to understand the potential financial
    implications.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse
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
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest,
) -> Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse]:
    """Calculates the estimated financial impact of a potential trade before execution

     Performs preflight calculations for a single-leg order (a transaction involving a single security)
    to provide comprehensive cost estimates and account impact details. Returns estimated commission,
    regulatory fees, order value, buying power requirements, margin impact, and other trade-specific
    information to help users make informed trading decisions before order placement. Note that these
    are estimates only, and actual execution values may vary depending on market conditions. This
    endpoint may be called before submitting an actual order to understand the potential financial
    implications.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse]
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
    body: ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest,
) -> Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse | None:
    """Calculates the estimated financial impact of a potential trade before execution

     Performs preflight calculations for a single-leg order (a transaction involving a single security)
    to provide comprehensive cost estimates and account impact details. Returns estimated commission,
    regulatory fees, order value, buying power requirements, margin impact, and other trade-specific
    information to help users make informed trading decisions before order placement. Note that these
    are estimates only, and actual execution values may vary depending on market conditions. This
    endpoint may be called before submitting an actual order to understand the potential financial
    implications.

    Args:
        account_id (str):
        body (ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            body=body,
        )
    ).parsed
