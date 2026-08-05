from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse"
)


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataBonddetailsBondDetailsResponse:
    """Bond details response combining instrument data and quote information

    Attributes:
        cusip (str | Unset): CUSIP identifier
        issuer (None | str | Unset): Name of the bond issuer
        issuer_symbol (None | str | Unset): Symbol of the bond issuer
        symbol (None | str | Unset): Bond symbol (typically CUSIP-BOND format)
        description (None | str | Unset): Full description of the bond
        description_short (None | str | Unset): Short description of the bond
        bond_type (None | str | Unset): Type of bond (e.g., TREASURY, CORPORATE, MUNICIPAL)
        treasury_subtype (None | str | Unset): Treasury subtype (e.g., STRIPS)
        treasury_duration (None | str | Unset): Treasury duration (e.g., 30Y)
        bond_status (None | str | Unset): Bond status (e.g., OUTSTANDING)
        issue_date (datetime.date | None | Unset): Date when the bond was issued
        issue_price (None | str | Unset): Original price at which the bond was issued
        issue_size (None | str | Unset): Total size of the bond issue
        maturity_date (datetime.date | None | Unset): Date when the bond matures
        rating (None | str | Unset): Credit rating of the bond
        rating_category (None | str | Unset): Rating category (e.g., INVESTMENT_GRADE)
        coupon (None | str | Unset): Coupon rate of the bond
        coupon_frequency (None | str | Unset): Frequency of coupon payments
        next_coupon_date (datetime.date | None | Unset): Date of the next coupon payment
        par_value (None | str | Unset): Par value of the bond
        accrued_interest (None | str | Unset): Accrued interest on the bond
        callable_ (bool | None | Unset): Whether the bond is callable
        next_call_date (datetime.date | None | Unset): Date of the next call option
        next_call_price (None | str | Unset): Price at which the bond can be called
        current_yield (None | str | Unset): Current yield of the bond
        current_price (None | str | Unset): Current market price of the bond
        sp_outlook (None | str | Unset): S&P rating outlook
        sp_outlook_date (datetime.date | None | Unset): Date of S&P outlook
        sp_creditwatch (None | str | Unset): S&P creditwatch status
        sp_creditwatch_date (datetime.date | None | Unset): Date of S&P creditwatch
        perpetual (bool | None | Unset): Whether the bond is perpetual
        country_issue (None | str | Unset): Country where the bond was issued
        country_domicile (None | str | Unset): Country of issuer domicile
        days_until_maturity (int | None | Unset): Number of days until the bond matures
        liquidity_rating (None | str | Unset): Liquidity rating of the bond
        seniority (None | str | Unset): Seniority level of the bond
        partial_par (bool | Unset): Whether partial par trading is allowed
        minimum_order_size (None | str | Unset): Minimum order size for trading
        minimum_order_increment (None | str | Unset): Minimum order increment for trading
    """

    cusip: str | Unset = UNSET
    issuer: None | str | Unset = UNSET
    issuer_symbol: None | str | Unset = UNSET
    symbol: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    description_short: None | str | Unset = UNSET
    bond_type: None | str | Unset = UNSET
    treasury_subtype: None | str | Unset = UNSET
    treasury_duration: None | str | Unset = UNSET
    bond_status: None | str | Unset = UNSET
    issue_date: datetime.date | None | Unset = UNSET
    issue_price: None | str | Unset = UNSET
    issue_size: None | str | Unset = UNSET
    maturity_date: datetime.date | None | Unset = UNSET
    rating: None | str | Unset = UNSET
    rating_category: None | str | Unset = UNSET
    coupon: None | str | Unset = UNSET
    coupon_frequency: None | str | Unset = UNSET
    next_coupon_date: datetime.date | None | Unset = UNSET
    par_value: None | str | Unset = UNSET
    accrued_interest: None | str | Unset = UNSET
    callable_: bool | None | Unset = UNSET
    next_call_date: datetime.date | None | Unset = UNSET
    next_call_price: None | str | Unset = UNSET
    current_yield: None | str | Unset = UNSET
    current_price: None | str | Unset = UNSET
    sp_outlook: None | str | Unset = UNSET
    sp_outlook_date: datetime.date | None | Unset = UNSET
    sp_creditwatch: None | str | Unset = UNSET
    sp_creditwatch_date: datetime.date | None | Unset = UNSET
    perpetual: bool | None | Unset = UNSET
    country_issue: None | str | Unset = UNSET
    country_domicile: None | str | Unset = UNSET
    days_until_maturity: int | None | Unset = UNSET
    liquidity_rating: None | str | Unset = UNSET
    seniority: None | str | Unset = UNSET
    partial_par: bool | Unset = UNSET
    minimum_order_size: None | str | Unset = UNSET
    minimum_order_increment: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cusip = self.cusip

        issuer: None | str | Unset
        if isinstance(self.issuer, Unset):
            issuer = UNSET
        else:
            issuer = self.issuer

        issuer_symbol: None | str | Unset
        if isinstance(self.issuer_symbol, Unset):
            issuer_symbol = UNSET
        else:
            issuer_symbol = self.issuer_symbol

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        description_short: None | str | Unset
        if isinstance(self.description_short, Unset):
            description_short = UNSET
        else:
            description_short = self.description_short

        bond_type: None | str | Unset
        if isinstance(self.bond_type, Unset):
            bond_type = UNSET
        else:
            bond_type = self.bond_type

        treasury_subtype: None | str | Unset
        if isinstance(self.treasury_subtype, Unset):
            treasury_subtype = UNSET
        else:
            treasury_subtype = self.treasury_subtype

        treasury_duration: None | str | Unset
        if isinstance(self.treasury_duration, Unset):
            treasury_duration = UNSET
        else:
            treasury_duration = self.treasury_duration

        bond_status: None | str | Unset
        if isinstance(self.bond_status, Unset):
            bond_status = UNSET
        else:
            bond_status = self.bond_status

        issue_date: None | str | Unset
        if isinstance(self.issue_date, Unset):
            issue_date = UNSET
        elif isinstance(self.issue_date, datetime.date):
            issue_date = self.issue_date.isoformat()
        else:
            issue_date = self.issue_date

        issue_price: None | str | Unset
        if isinstance(self.issue_price, Unset):
            issue_price = UNSET
        else:
            issue_price = self.issue_price

        issue_size: None | str | Unset
        if isinstance(self.issue_size, Unset):
            issue_size = UNSET
        else:
            issue_size = self.issue_size

        maturity_date: None | str | Unset
        if isinstance(self.maturity_date, Unset):
            maturity_date = UNSET
        elif isinstance(self.maturity_date, datetime.date):
            maturity_date = self.maturity_date.isoformat()
        else:
            maturity_date = self.maturity_date

        rating: None | str | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        rating_category: None | str | Unset
        if isinstance(self.rating_category, Unset):
            rating_category = UNSET
        else:
            rating_category = self.rating_category

        coupon: None | str | Unset
        if isinstance(self.coupon, Unset):
            coupon = UNSET
        else:
            coupon = self.coupon

        coupon_frequency: None | str | Unset
        if isinstance(self.coupon_frequency, Unset):
            coupon_frequency = UNSET
        else:
            coupon_frequency = self.coupon_frequency

        next_coupon_date: None | str | Unset
        if isinstance(self.next_coupon_date, Unset):
            next_coupon_date = UNSET
        elif isinstance(self.next_coupon_date, datetime.date):
            next_coupon_date = self.next_coupon_date.isoformat()
        else:
            next_coupon_date = self.next_coupon_date

        par_value: None | str | Unset
        if isinstance(self.par_value, Unset):
            par_value = UNSET
        else:
            par_value = self.par_value

        accrued_interest: None | str | Unset
        if isinstance(self.accrued_interest, Unset):
            accrued_interest = UNSET
        else:
            accrued_interest = self.accrued_interest

        callable_: bool | None | Unset
        if isinstance(self.callable_, Unset):
            callable_ = UNSET
        else:
            callable_ = self.callable_

        next_call_date: None | str | Unset
        if isinstance(self.next_call_date, Unset):
            next_call_date = UNSET
        elif isinstance(self.next_call_date, datetime.date):
            next_call_date = self.next_call_date.isoformat()
        else:
            next_call_date = self.next_call_date

        next_call_price: None | str | Unset
        if isinstance(self.next_call_price, Unset):
            next_call_price = UNSET
        else:
            next_call_price = self.next_call_price

        current_yield: None | str | Unset
        if isinstance(self.current_yield, Unset):
            current_yield = UNSET
        else:
            current_yield = self.current_yield

        current_price: None | str | Unset
        if isinstance(self.current_price, Unset):
            current_price = UNSET
        else:
            current_price = self.current_price

        sp_outlook: None | str | Unset
        if isinstance(self.sp_outlook, Unset):
            sp_outlook = UNSET
        else:
            sp_outlook = self.sp_outlook

        sp_outlook_date: None | str | Unset
        if isinstance(self.sp_outlook_date, Unset):
            sp_outlook_date = UNSET
        elif isinstance(self.sp_outlook_date, datetime.date):
            sp_outlook_date = self.sp_outlook_date.isoformat()
        else:
            sp_outlook_date = self.sp_outlook_date

        sp_creditwatch: None | str | Unset
        if isinstance(self.sp_creditwatch, Unset):
            sp_creditwatch = UNSET
        else:
            sp_creditwatch = self.sp_creditwatch

        sp_creditwatch_date: None | str | Unset
        if isinstance(self.sp_creditwatch_date, Unset):
            sp_creditwatch_date = UNSET
        elif isinstance(self.sp_creditwatch_date, datetime.date):
            sp_creditwatch_date = self.sp_creditwatch_date.isoformat()
        else:
            sp_creditwatch_date = self.sp_creditwatch_date

        perpetual: bool | None | Unset
        if isinstance(self.perpetual, Unset):
            perpetual = UNSET
        else:
            perpetual = self.perpetual

        country_issue: None | str | Unset
        if isinstance(self.country_issue, Unset):
            country_issue = UNSET
        else:
            country_issue = self.country_issue

        country_domicile: None | str | Unset
        if isinstance(self.country_domicile, Unset):
            country_domicile = UNSET
        else:
            country_domicile = self.country_domicile

        days_until_maturity: int | None | Unset
        if isinstance(self.days_until_maturity, Unset):
            days_until_maturity = UNSET
        else:
            days_until_maturity = self.days_until_maturity

        liquidity_rating: None | str | Unset
        if isinstance(self.liquidity_rating, Unset):
            liquidity_rating = UNSET
        else:
            liquidity_rating = self.liquidity_rating

        seniority: None | str | Unset
        if isinstance(self.seniority, Unset):
            seniority = UNSET
        else:
            seniority = self.seniority

        partial_par = self.partial_par

        minimum_order_size: None | str | Unset
        if isinstance(self.minimum_order_size, Unset):
            minimum_order_size = UNSET
        else:
            minimum_order_size = self.minimum_order_size

        minimum_order_increment: None | str | Unset
        if isinstance(self.minimum_order_increment, Unset):
            minimum_order_increment = UNSET
        else:
            minimum_order_increment = self.minimum_order_increment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cusip is not UNSET:
            field_dict["cusip"] = cusip
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if issuer_symbol is not UNSET:
            field_dict["issuerSymbol"] = issuer_symbol
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if description is not UNSET:
            field_dict["description"] = description
        if description_short is not UNSET:
            field_dict["descriptionShort"] = description_short
        if bond_type is not UNSET:
            field_dict["bondType"] = bond_type
        if treasury_subtype is not UNSET:
            field_dict["treasurySubtype"] = treasury_subtype
        if treasury_duration is not UNSET:
            field_dict["treasuryDuration"] = treasury_duration
        if bond_status is not UNSET:
            field_dict["bondStatus"] = bond_status
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if issue_price is not UNSET:
            field_dict["issuePrice"] = issue_price
        if issue_size is not UNSET:
            field_dict["issueSize"] = issue_size
        if maturity_date is not UNSET:
            field_dict["maturityDate"] = maturity_date
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_category is not UNSET:
            field_dict["ratingCategory"] = rating_category
        if coupon is not UNSET:
            field_dict["coupon"] = coupon
        if coupon_frequency is not UNSET:
            field_dict["couponFrequency"] = coupon_frequency
        if next_coupon_date is not UNSET:
            field_dict["nextCouponDate"] = next_coupon_date
        if par_value is not UNSET:
            field_dict["parValue"] = par_value
        if accrued_interest is not UNSET:
            field_dict["accruedInterest"] = accrued_interest
        if callable_ is not UNSET:
            field_dict["callable"] = callable_
        if next_call_date is not UNSET:
            field_dict["nextCallDate"] = next_call_date
        if next_call_price is not UNSET:
            field_dict["nextCallPrice"] = next_call_price
        if current_yield is not UNSET:
            field_dict["currentYield"] = current_yield
        if current_price is not UNSET:
            field_dict["currentPrice"] = current_price
        if sp_outlook is not UNSET:
            field_dict["spOutlook"] = sp_outlook
        if sp_outlook_date is not UNSET:
            field_dict["spOutlookDate"] = sp_outlook_date
        if sp_creditwatch is not UNSET:
            field_dict["spCreditwatch"] = sp_creditwatch
        if sp_creditwatch_date is not UNSET:
            field_dict["spCreditwatchDate"] = sp_creditwatch_date
        if perpetual is not UNSET:
            field_dict["perpetual"] = perpetual
        if country_issue is not UNSET:
            field_dict["countryIssue"] = country_issue
        if country_domicile is not UNSET:
            field_dict["countryDomicile"] = country_domicile
        if days_until_maturity is not UNSET:
            field_dict["daysUntilMaturity"] = days_until_maturity
        if liquidity_rating is not UNSET:
            field_dict["liquidityRating"] = liquidity_rating
        if seniority is not UNSET:
            field_dict["seniority"] = seniority
        if partial_par is not UNSET:
            field_dict["partialPar"] = partial_par
        if minimum_order_size is not UNSET:
            field_dict["minimumOrderSize"] = minimum_order_size
        if minimum_order_increment is not UNSET:
            field_dict["minimumOrderIncrement"] = minimum_order_increment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cusip = d.pop("cusip", UNSET)

        def _parse_issuer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer = _parse_issuer(d.pop("issuer", UNSET))

        def _parse_issuer_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer_symbol = _parse_issuer_symbol(d.pop("issuerSymbol", UNSET))

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_description_short(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description_short = _parse_description_short(d.pop("descriptionShort", UNSET))

        def _parse_bond_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bond_type = _parse_bond_type(d.pop("bondType", UNSET))

        def _parse_treasury_subtype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        treasury_subtype = _parse_treasury_subtype(d.pop("treasurySubtype", UNSET))

        def _parse_treasury_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        treasury_duration = _parse_treasury_duration(d.pop("treasuryDuration", UNSET))

        def _parse_bond_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bond_status = _parse_bond_status(d.pop("bondStatus", UNSET))

        def _parse_issue_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issue_date_type_0 = datetime.date.fromisoformat(data)

                return issue_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        issue_date = _parse_issue_date(d.pop("issueDate", UNSET))

        def _parse_issue_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_price = _parse_issue_price(d.pop("issuePrice", UNSET))

        def _parse_issue_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue_size = _parse_issue_size(d.pop("issueSize", UNSET))

        def _parse_maturity_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maturity_date_type_0 = datetime.date.fromisoformat(data)

                return maturity_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        maturity_date = _parse_maturity_date(d.pop("maturityDate", UNSET))

        def _parse_rating(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))

        def _parse_rating_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rating_category = _parse_rating_category(d.pop("ratingCategory", UNSET))

        def _parse_coupon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coupon = _parse_coupon(d.pop("coupon", UNSET))

        def _parse_coupon_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coupon_frequency = _parse_coupon_frequency(d.pop("couponFrequency", UNSET))

        def _parse_next_coupon_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_coupon_date_type_0 = datetime.date.fromisoformat(data)

                return next_coupon_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        next_coupon_date = _parse_next_coupon_date(d.pop("nextCouponDate", UNSET))

        def _parse_par_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        par_value = _parse_par_value(d.pop("parValue", UNSET))

        def _parse_accrued_interest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accrued_interest = _parse_accrued_interest(d.pop("accruedInterest", UNSET))

        def _parse_callable_(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        callable_ = _parse_callable_(d.pop("callable", UNSET))

        def _parse_next_call_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_call_date_type_0 = datetime.date.fromisoformat(data)

                return next_call_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        next_call_date = _parse_next_call_date(d.pop("nextCallDate", UNSET))

        def _parse_next_call_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_call_price = _parse_next_call_price(d.pop("nextCallPrice", UNSET))

        def _parse_current_yield(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_yield = _parse_current_yield(d.pop("currentYield", UNSET))

        def _parse_current_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_price = _parse_current_price(d.pop("currentPrice", UNSET))

        def _parse_sp_outlook(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sp_outlook = _parse_sp_outlook(d.pop("spOutlook", UNSET))

        def _parse_sp_outlook_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sp_outlook_date_type_0 = datetime.date.fromisoformat(data)

                return sp_outlook_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        sp_outlook_date = _parse_sp_outlook_date(d.pop("spOutlookDate", UNSET))

        def _parse_sp_creditwatch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sp_creditwatch = _parse_sp_creditwatch(d.pop("spCreditwatch", UNSET))

        def _parse_sp_creditwatch_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sp_creditwatch_date_type_0 = datetime.date.fromisoformat(data)

                return sp_creditwatch_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        sp_creditwatch_date = _parse_sp_creditwatch_date(d.pop("spCreditwatchDate", UNSET))

        def _parse_perpetual(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        perpetual = _parse_perpetual(d.pop("perpetual", UNSET))

        def _parse_country_issue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_issue = _parse_country_issue(d.pop("countryIssue", UNSET))

        def _parse_country_domicile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_domicile = _parse_country_domicile(d.pop("countryDomicile", UNSET))

        def _parse_days_until_maturity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_until_maturity = _parse_days_until_maturity(d.pop("daysUntilMaturity", UNSET))

        def _parse_liquidity_rating(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        liquidity_rating = _parse_liquidity_rating(d.pop("liquidityRating", UNSET))

        def _parse_seniority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seniority = _parse_seniority(d.pop("seniority", UNSET))

        partial_par = d.pop("partialPar", UNSET)

        def _parse_minimum_order_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_order_size = _parse_minimum_order_size(d.pop("minimumOrderSize", UNSET))

        def _parse_minimum_order_increment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_order_increment = _parse_minimum_order_increment(
            d.pop("minimumOrderIncrement", UNSET)
        )

        com_hellopublic_userapigateway_api_rest_marketdata_bonddetails_bond_details_response = cls(
            cusip=cusip,
            issuer=issuer,
            issuer_symbol=issuer_symbol,
            symbol=symbol,
            description=description,
            description_short=description_short,
            bond_type=bond_type,
            treasury_subtype=treasury_subtype,
            treasury_duration=treasury_duration,
            bond_status=bond_status,
            issue_date=issue_date,
            issue_price=issue_price,
            issue_size=issue_size,
            maturity_date=maturity_date,
            rating=rating,
            rating_category=rating_category,
            coupon=coupon,
            coupon_frequency=coupon_frequency,
            next_coupon_date=next_coupon_date,
            par_value=par_value,
            accrued_interest=accrued_interest,
            callable_=callable_,
            next_call_date=next_call_date,
            next_call_price=next_call_price,
            current_yield=current_yield,
            current_price=current_price,
            sp_outlook=sp_outlook,
            sp_outlook_date=sp_outlook_date,
            sp_creditwatch=sp_creditwatch,
            sp_creditwatch_date=sp_creditwatch_date,
            perpetual=perpetual,
            country_issue=country_issue,
            country_domicile=country_domicile,
            days_until_maturity=days_until_maturity,
            liquidity_rating=liquidity_rating,
            seniority=seniority,
            partial_par=partial_par,
            minimum_order_size=minimum_order_size,
            minimum_order_increment=minimum_order_increment,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_bonddetails_bond_details_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_bonddetails_bond_details_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
