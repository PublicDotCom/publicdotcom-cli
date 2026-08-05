import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.org_springframework_data_domain_page_com_hellopublic_fixedincomegateway_instrument_instrument_dto import (
    OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto,
)
from ...models.search_bonds_bond_status_item import SearchBondsBondStatusItem
from ...models.search_bonds_bond_type_item import SearchBondsBondTypeItem
from ...models.search_bonds_coupon_frequency_item import SearchBondsCouponFrequencyItem
from ...models.search_bonds_rating_category import SearchBondsRatingCategory
from ...models.search_bonds_rating_item import SearchBondsRatingItem
from ...models.search_bonds_sort_direction import SearchBondsSortDirection
from ...models.search_bonds_sp_creditwatch_item import SearchBondsSpCreditwatchItem
from ...models.search_bonds_sp_outlook_item import SearchBondsSpOutlookItem
from ...models.search_bonds_treasury_subtype_item import SearchBondsTreasurySubtypeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_property: str | Unset = UNSET,
    sort_direction: SearchBondsSortDirection | Unset = SearchBondsSortDirection.DESC,
    issuer: str | Unset = UNSET,
    issuer_symbol: list[str] | Unset = UNSET,
    bond_status: list[SearchBondsBondStatusItem] | Unset = UNSET,
    bond_type: list[SearchBondsBondTypeItem] | Unset = UNSET,
    treasury_subtype: list[SearchBondsTreasurySubtypeItem] | Unset = UNSET,
    rating: list[SearchBondsRatingItem] | Unset = UNSET,
    rating_category: SearchBondsRatingCategory | Unset = UNSET,
    sp_outlook: list[SearchBondsSpOutlookItem] | Unset = UNSET,
    sp_creditwatch: list[SearchBondsSpCreditwatchItem] | Unset = UNSET,
    coupon_frequency: list[SearchBondsCouponFrequencyItem] | Unset = UNSET,
    min_coupon: float | Unset = UNSET,
    max_coupon: float | Unset = UNSET,
    min_maturity_date: datetime.date | Unset = UNSET,
    max_maturity_date: datetime.date | Unset = UNSET,
    min_current_yield: float | Unset = UNSET,
    max_current_yield: float | Unset = UNSET,
    min_par_value: float | Unset = UNSET,
    max_par_value: float | Unset = UNSET,
    min_liquidity_rating: float | Unset = UNSET,
    max_liquidity_rating: float | Unset = UNSET,
    liquidity_rating: list[float] | Unset = UNSET,
    callable_: bool | Unset = UNSET,
    perpetual: bool | Unset = UNSET,
    partial_par: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params["sortProperty"] = sort_property

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    params["issuer"] = issuer

    json_issuer_symbol: list[str] | Unset = UNSET
    if not isinstance(issuer_symbol, Unset):
        json_issuer_symbol = issuer_symbol

    params["issuerSymbol"] = json_issuer_symbol

    json_bond_status: list[str] | Unset = UNSET
    if not isinstance(bond_status, Unset):
        json_bond_status = []
        for bond_status_item_data in bond_status:
            bond_status_item = bond_status_item_data.value
            json_bond_status.append(bond_status_item)

    params["bondStatus"] = json_bond_status

    json_bond_type: list[str] | Unset = UNSET
    if not isinstance(bond_type, Unset):
        json_bond_type = []
        for bond_type_item_data in bond_type:
            bond_type_item = bond_type_item_data.value
            json_bond_type.append(bond_type_item)

    params["bondType"] = json_bond_type

    json_treasury_subtype: list[str] | Unset = UNSET
    if not isinstance(treasury_subtype, Unset):
        json_treasury_subtype = []
        for treasury_subtype_item_data in treasury_subtype:
            treasury_subtype_item = treasury_subtype_item_data.value
            json_treasury_subtype.append(treasury_subtype_item)

    params["treasurySubtype"] = json_treasury_subtype

    json_rating: list[str] | Unset = UNSET
    if not isinstance(rating, Unset):
        json_rating = []
        for rating_item_data in rating:
            rating_item = rating_item_data.value
            json_rating.append(rating_item)

    params["rating"] = json_rating

    json_rating_category: str | Unset = UNSET
    if not isinstance(rating_category, Unset):
        json_rating_category = rating_category.value

    params["ratingCategory"] = json_rating_category

    json_sp_outlook: list[str] | Unset = UNSET
    if not isinstance(sp_outlook, Unset):
        json_sp_outlook = []
        for sp_outlook_item_data in sp_outlook:
            sp_outlook_item = sp_outlook_item_data.value
            json_sp_outlook.append(sp_outlook_item)

    params["spOutlook"] = json_sp_outlook

    json_sp_creditwatch: list[str] | Unset = UNSET
    if not isinstance(sp_creditwatch, Unset):
        json_sp_creditwatch = []
        for sp_creditwatch_item_data in sp_creditwatch:
            sp_creditwatch_item = sp_creditwatch_item_data.value
            json_sp_creditwatch.append(sp_creditwatch_item)

    params["spCreditwatch"] = json_sp_creditwatch

    json_coupon_frequency: list[str] | Unset = UNSET
    if not isinstance(coupon_frequency, Unset):
        json_coupon_frequency = []
        for coupon_frequency_item_data in coupon_frequency:
            coupon_frequency_item = coupon_frequency_item_data.value
            json_coupon_frequency.append(coupon_frequency_item)

    params["couponFrequency"] = json_coupon_frequency

    params["minCoupon"] = min_coupon

    params["maxCoupon"] = max_coupon

    json_min_maturity_date: str | Unset = UNSET
    if not isinstance(min_maturity_date, Unset):
        json_min_maturity_date = min_maturity_date.isoformat()
    params["minMaturityDate"] = json_min_maturity_date

    json_max_maturity_date: str | Unset = UNSET
    if not isinstance(max_maturity_date, Unset):
        json_max_maturity_date = max_maturity_date.isoformat()
    params["maxMaturityDate"] = json_max_maturity_date

    params["minCurrentYield"] = min_current_yield

    params["maxCurrentYield"] = max_current_yield

    params["minParValue"] = min_par_value

    params["maxParValue"] = max_par_value

    params["minLiquidityRating"] = min_liquidity_rating

    params["maxLiquidityRating"] = max_liquidity_rating

    json_liquidity_rating: list[float] | Unset = UNSET
    if not isinstance(liquidity_rating, Unset):
        json_liquidity_rating = liquidity_rating

    params["liquidityRating"] = json_liquidity_rating

    params["callable"] = callable_

    params["perpetual"] = perpetual

    params["partialPar"] = partial_par

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userapigateway/trading/instruments/bonds",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto | None:
    if response.status_code == 200:
        response_200 = OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto
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
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_property: str | Unset = UNSET,
    sort_direction: SearchBondsSortDirection | Unset = SearchBondsSortDirection.DESC,
    issuer: str | Unset = UNSET,
    issuer_symbol: list[str] | Unset = UNSET,
    bond_status: list[SearchBondsBondStatusItem] | Unset = UNSET,
    bond_type: list[SearchBondsBondTypeItem] | Unset = UNSET,
    treasury_subtype: list[SearchBondsTreasurySubtypeItem] | Unset = UNSET,
    rating: list[SearchBondsRatingItem] | Unset = UNSET,
    rating_category: SearchBondsRatingCategory | Unset = UNSET,
    sp_outlook: list[SearchBondsSpOutlookItem] | Unset = UNSET,
    sp_creditwatch: list[SearchBondsSpCreditwatchItem] | Unset = UNSET,
    coupon_frequency: list[SearchBondsCouponFrequencyItem] | Unset = UNSET,
    min_coupon: float | Unset = UNSET,
    max_coupon: float | Unset = UNSET,
    min_maturity_date: datetime.date | Unset = UNSET,
    max_maturity_date: datetime.date | Unset = UNSET,
    min_current_yield: float | Unset = UNSET,
    max_current_yield: float | Unset = UNSET,
    min_par_value: float | Unset = UNSET,
    max_par_value: float | Unset = UNSET,
    min_liquidity_rating: float | Unset = UNSET,
    max_liquidity_rating: float | Unset = UNSET,
    liquidity_rating: list[float] | Unset = UNSET,
    callable_: bool | Unset = UNSET,
    perpetual: bool | Unset = UNSET,
    partial_par: bool | Unset = UNSET,
) -> Response[
    OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto
]:
    """Filtered search for fixed income instruments

     Returns a paged list of fixed income instruments from the bonds hub with support for filtering,
    sorting, and pagination.

    Args:
        page_number (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        sort_property (str | Unset):
        sort_direction (SearchBondsSortDirection | Unset):  Default:
            SearchBondsSortDirection.DESC.
        issuer (str | Unset):
        issuer_symbol (list[str] | Unset):
        bond_status (list[SearchBondsBondStatusItem] | Unset):
        bond_type (list[SearchBondsBondTypeItem] | Unset):
        treasury_subtype (list[SearchBondsTreasurySubtypeItem] | Unset):
        rating (list[SearchBondsRatingItem] | Unset):
        rating_category (SearchBondsRatingCategory | Unset):
        sp_outlook (list[SearchBondsSpOutlookItem] | Unset):
        sp_creditwatch (list[SearchBondsSpCreditwatchItem] | Unset):
        coupon_frequency (list[SearchBondsCouponFrequencyItem] | Unset):
        min_coupon (float | Unset):
        max_coupon (float | Unset):
        min_maturity_date (datetime.date | Unset):
        max_maturity_date (datetime.date | Unset):
        min_current_yield (float | Unset):
        max_current_yield (float | Unset):
        min_par_value (float | Unset):
        max_par_value (float | Unset):
        min_liquidity_rating (float | Unset):
        max_liquidity_rating (float | Unset):
        liquidity_rating (list[float] | Unset):
        callable_ (bool | Unset):
        perpetual (bool | Unset):
        partial_par (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        sort_property=sort_property,
        sort_direction=sort_direction,
        issuer=issuer,
        issuer_symbol=issuer_symbol,
        bond_status=bond_status,
        bond_type=bond_type,
        treasury_subtype=treasury_subtype,
        rating=rating,
        rating_category=rating_category,
        sp_outlook=sp_outlook,
        sp_creditwatch=sp_creditwatch,
        coupon_frequency=coupon_frequency,
        min_coupon=min_coupon,
        max_coupon=max_coupon,
        min_maturity_date=min_maturity_date,
        max_maturity_date=max_maturity_date,
        min_current_yield=min_current_yield,
        max_current_yield=max_current_yield,
        min_par_value=min_par_value,
        max_par_value=max_par_value,
        min_liquidity_rating=min_liquidity_rating,
        max_liquidity_rating=max_liquidity_rating,
        liquidity_rating=liquidity_rating,
        callable_=callable_,
        perpetual=perpetual,
        partial_par=partial_par,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_property: str | Unset = UNSET,
    sort_direction: SearchBondsSortDirection | Unset = SearchBondsSortDirection.DESC,
    issuer: str | Unset = UNSET,
    issuer_symbol: list[str] | Unset = UNSET,
    bond_status: list[SearchBondsBondStatusItem] | Unset = UNSET,
    bond_type: list[SearchBondsBondTypeItem] | Unset = UNSET,
    treasury_subtype: list[SearchBondsTreasurySubtypeItem] | Unset = UNSET,
    rating: list[SearchBondsRatingItem] | Unset = UNSET,
    rating_category: SearchBondsRatingCategory | Unset = UNSET,
    sp_outlook: list[SearchBondsSpOutlookItem] | Unset = UNSET,
    sp_creditwatch: list[SearchBondsSpCreditwatchItem] | Unset = UNSET,
    coupon_frequency: list[SearchBondsCouponFrequencyItem] | Unset = UNSET,
    min_coupon: float | Unset = UNSET,
    max_coupon: float | Unset = UNSET,
    min_maturity_date: datetime.date | Unset = UNSET,
    max_maturity_date: datetime.date | Unset = UNSET,
    min_current_yield: float | Unset = UNSET,
    max_current_yield: float | Unset = UNSET,
    min_par_value: float | Unset = UNSET,
    max_par_value: float | Unset = UNSET,
    min_liquidity_rating: float | Unset = UNSET,
    max_liquidity_rating: float | Unset = UNSET,
    liquidity_rating: list[float] | Unset = UNSET,
    callable_: bool | Unset = UNSET,
    perpetual: bool | Unset = UNSET,
    partial_par: bool | Unset = UNSET,
) -> OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto | None:
    """Filtered search for fixed income instruments

     Returns a paged list of fixed income instruments from the bonds hub with support for filtering,
    sorting, and pagination.

    Args:
        page_number (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        sort_property (str | Unset):
        sort_direction (SearchBondsSortDirection | Unset):  Default:
            SearchBondsSortDirection.DESC.
        issuer (str | Unset):
        issuer_symbol (list[str] | Unset):
        bond_status (list[SearchBondsBondStatusItem] | Unset):
        bond_type (list[SearchBondsBondTypeItem] | Unset):
        treasury_subtype (list[SearchBondsTreasurySubtypeItem] | Unset):
        rating (list[SearchBondsRatingItem] | Unset):
        rating_category (SearchBondsRatingCategory | Unset):
        sp_outlook (list[SearchBondsSpOutlookItem] | Unset):
        sp_creditwatch (list[SearchBondsSpCreditwatchItem] | Unset):
        coupon_frequency (list[SearchBondsCouponFrequencyItem] | Unset):
        min_coupon (float | Unset):
        max_coupon (float | Unset):
        min_maturity_date (datetime.date | Unset):
        max_maturity_date (datetime.date | Unset):
        min_current_yield (float | Unset):
        max_current_yield (float | Unset):
        min_par_value (float | Unset):
        max_par_value (float | Unset):
        min_liquidity_rating (float | Unset):
        max_liquidity_rating (float | Unset):
        liquidity_rating (list[float] | Unset):
        callable_ (bool | Unset):
        perpetual (bool | Unset):
        partial_par (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto
    """

    return sync_detailed(
        client=client,
        page_number=page_number,
        page_size=page_size,
        sort_property=sort_property,
        sort_direction=sort_direction,
        issuer=issuer,
        issuer_symbol=issuer_symbol,
        bond_status=bond_status,
        bond_type=bond_type,
        treasury_subtype=treasury_subtype,
        rating=rating,
        rating_category=rating_category,
        sp_outlook=sp_outlook,
        sp_creditwatch=sp_creditwatch,
        coupon_frequency=coupon_frequency,
        min_coupon=min_coupon,
        max_coupon=max_coupon,
        min_maturity_date=min_maturity_date,
        max_maturity_date=max_maturity_date,
        min_current_yield=min_current_yield,
        max_current_yield=max_current_yield,
        min_par_value=min_par_value,
        max_par_value=max_par_value,
        min_liquidity_rating=min_liquidity_rating,
        max_liquidity_rating=max_liquidity_rating,
        liquidity_rating=liquidity_rating,
        callable_=callable_,
        perpetual=perpetual,
        partial_par=partial_par,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_property: str | Unset = UNSET,
    sort_direction: SearchBondsSortDirection | Unset = SearchBondsSortDirection.DESC,
    issuer: str | Unset = UNSET,
    issuer_symbol: list[str] | Unset = UNSET,
    bond_status: list[SearchBondsBondStatusItem] | Unset = UNSET,
    bond_type: list[SearchBondsBondTypeItem] | Unset = UNSET,
    treasury_subtype: list[SearchBondsTreasurySubtypeItem] | Unset = UNSET,
    rating: list[SearchBondsRatingItem] | Unset = UNSET,
    rating_category: SearchBondsRatingCategory | Unset = UNSET,
    sp_outlook: list[SearchBondsSpOutlookItem] | Unset = UNSET,
    sp_creditwatch: list[SearchBondsSpCreditwatchItem] | Unset = UNSET,
    coupon_frequency: list[SearchBondsCouponFrequencyItem] | Unset = UNSET,
    min_coupon: float | Unset = UNSET,
    max_coupon: float | Unset = UNSET,
    min_maturity_date: datetime.date | Unset = UNSET,
    max_maturity_date: datetime.date | Unset = UNSET,
    min_current_yield: float | Unset = UNSET,
    max_current_yield: float | Unset = UNSET,
    min_par_value: float | Unset = UNSET,
    max_par_value: float | Unset = UNSET,
    min_liquidity_rating: float | Unset = UNSET,
    max_liquidity_rating: float | Unset = UNSET,
    liquidity_rating: list[float] | Unset = UNSET,
    callable_: bool | Unset = UNSET,
    perpetual: bool | Unset = UNSET,
    partial_par: bool | Unset = UNSET,
) -> Response[
    OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto
]:
    """Filtered search for fixed income instruments

     Returns a paged list of fixed income instruments from the bonds hub with support for filtering,
    sorting, and pagination.

    Args:
        page_number (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        sort_property (str | Unset):
        sort_direction (SearchBondsSortDirection | Unset):  Default:
            SearchBondsSortDirection.DESC.
        issuer (str | Unset):
        issuer_symbol (list[str] | Unset):
        bond_status (list[SearchBondsBondStatusItem] | Unset):
        bond_type (list[SearchBondsBondTypeItem] | Unset):
        treasury_subtype (list[SearchBondsTreasurySubtypeItem] | Unset):
        rating (list[SearchBondsRatingItem] | Unset):
        rating_category (SearchBondsRatingCategory | Unset):
        sp_outlook (list[SearchBondsSpOutlookItem] | Unset):
        sp_creditwatch (list[SearchBondsSpCreditwatchItem] | Unset):
        coupon_frequency (list[SearchBondsCouponFrequencyItem] | Unset):
        min_coupon (float | Unset):
        max_coupon (float | Unset):
        min_maturity_date (datetime.date | Unset):
        max_maturity_date (datetime.date | Unset):
        min_current_yield (float | Unset):
        max_current_yield (float | Unset):
        min_par_value (float | Unset):
        max_par_value (float | Unset):
        min_liquidity_rating (float | Unset):
        max_liquidity_rating (float | Unset):
        liquidity_rating (list[float] | Unset):
        callable_ (bool | Unset):
        perpetual (bool | Unset):
        partial_par (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        sort_property=sort_property,
        sort_direction=sort_direction,
        issuer=issuer,
        issuer_symbol=issuer_symbol,
        bond_status=bond_status,
        bond_type=bond_type,
        treasury_subtype=treasury_subtype,
        rating=rating,
        rating_category=rating_category,
        sp_outlook=sp_outlook,
        sp_creditwatch=sp_creditwatch,
        coupon_frequency=coupon_frequency,
        min_coupon=min_coupon,
        max_coupon=max_coupon,
        min_maturity_date=min_maturity_date,
        max_maturity_date=max_maturity_date,
        min_current_yield=min_current_yield,
        max_current_yield=max_current_yield,
        min_par_value=min_par_value,
        max_par_value=max_par_value,
        min_liquidity_rating=min_liquidity_rating,
        max_liquidity_rating=max_liquidity_rating,
        liquidity_rating=liquidity_rating,
        callable_=callable_,
        perpetual=perpetual,
        partial_par=partial_par,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    sort_property: str | Unset = UNSET,
    sort_direction: SearchBondsSortDirection | Unset = SearchBondsSortDirection.DESC,
    issuer: str | Unset = UNSET,
    issuer_symbol: list[str] | Unset = UNSET,
    bond_status: list[SearchBondsBondStatusItem] | Unset = UNSET,
    bond_type: list[SearchBondsBondTypeItem] | Unset = UNSET,
    treasury_subtype: list[SearchBondsTreasurySubtypeItem] | Unset = UNSET,
    rating: list[SearchBondsRatingItem] | Unset = UNSET,
    rating_category: SearchBondsRatingCategory | Unset = UNSET,
    sp_outlook: list[SearchBondsSpOutlookItem] | Unset = UNSET,
    sp_creditwatch: list[SearchBondsSpCreditwatchItem] | Unset = UNSET,
    coupon_frequency: list[SearchBondsCouponFrequencyItem] | Unset = UNSET,
    min_coupon: float | Unset = UNSET,
    max_coupon: float | Unset = UNSET,
    min_maturity_date: datetime.date | Unset = UNSET,
    max_maturity_date: datetime.date | Unset = UNSET,
    min_current_yield: float | Unset = UNSET,
    max_current_yield: float | Unset = UNSET,
    min_par_value: float | Unset = UNSET,
    max_par_value: float | Unset = UNSET,
    min_liquidity_rating: float | Unset = UNSET,
    max_liquidity_rating: float | Unset = UNSET,
    liquidity_rating: list[float] | Unset = UNSET,
    callable_: bool | Unset = UNSET,
    perpetual: bool | Unset = UNSET,
    partial_par: bool | Unset = UNSET,
) -> OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto | None:
    """Filtered search for fixed income instruments

     Returns a paged list of fixed income instruments from the bonds hub with support for filtering,
    sorting, and pagination.

    Args:
        page_number (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        sort_property (str | Unset):
        sort_direction (SearchBondsSortDirection | Unset):  Default:
            SearchBondsSortDirection.DESC.
        issuer (str | Unset):
        issuer_symbol (list[str] | Unset):
        bond_status (list[SearchBondsBondStatusItem] | Unset):
        bond_type (list[SearchBondsBondTypeItem] | Unset):
        treasury_subtype (list[SearchBondsTreasurySubtypeItem] | Unset):
        rating (list[SearchBondsRatingItem] | Unset):
        rating_category (SearchBondsRatingCategory | Unset):
        sp_outlook (list[SearchBondsSpOutlookItem] | Unset):
        sp_creditwatch (list[SearchBondsSpCreditwatchItem] | Unset):
        coupon_frequency (list[SearchBondsCouponFrequencyItem] | Unset):
        min_coupon (float | Unset):
        max_coupon (float | Unset):
        min_maturity_date (datetime.date | Unset):
        max_maturity_date (datetime.date | Unset):
        min_current_yield (float | Unset):
        max_current_yield (float | Unset):
        min_par_value (float | Unset):
        max_par_value (float | Unset):
        min_liquidity_rating (float | Unset):
        max_liquidity_rating (float | Unset):
        liquidity_rating (list[float] | Unset):
        callable_ (bool | Unset):
        perpetual (bool | Unset):
        partial_par (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto
    """

    return (
        await asyncio_detailed(
            client=client,
            page_number=page_number,
            page_size=page_size,
            sort_property=sort_property,
            sort_direction=sort_direction,
            issuer=issuer,
            issuer_symbol=issuer_symbol,
            bond_status=bond_status,
            bond_type=bond_type,
            treasury_subtype=treasury_subtype,
            rating=rating,
            rating_category=rating_category,
            sp_outlook=sp_outlook,
            sp_creditwatch=sp_creditwatch,
            coupon_frequency=coupon_frequency,
            min_coupon=min_coupon,
            max_coupon=max_coupon,
            min_maturity_date=min_maturity_date,
            max_maturity_date=max_maturity_date,
            min_current_yield=min_current_yield,
            max_current_yield=max_current_yield,
            min_par_value=min_par_value,
            max_par_value=max_par_value,
            min_liquidity_rating=min_liquidity_rating,
            max_liquidity_rating=max_liquidity_rating,
            liquidity_rating=liquidity_rating,
            callable_=callable_,
            perpetual=perpetual,
            partial_par=partial_par,
        )
    ).parsed
