from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicFixedincomegatewayInstrumentInstrumentDto")


@_attrs_define
class ComHellopublicFixedincomegatewayInstrumentInstrumentDto:
    """
    Attributes:
        cusip (str | Unset):
        issuer (str | Unset):
        issuer_symbol (str | Unset):
        symbol (str | Unset):
        description (str | Unset):
        description_short (str | Unset):
        bond_type (str | Unset):
        treasury_subtype (str | Unset):
        treasury_duration (str | Unset):
        bond_status (str | Unset):
        issue_date (datetime.date | Unset):
        issue_price (str | Unset):
        issue_size (str | Unset):
        maturity_date (datetime.date | Unset):
        rating (str | Unset):
        rating_category (str | Unset):
        coupon (str | Unset):
        coupon_frequency (str | Unset):
        next_coupon_date (datetime.date | Unset):
        par_value (str | Unset):
        accrued_interest (str | Unset):
        callable_ (bool | Unset):
        next_call_date (datetime.date | Unset):
        next_call_price (str | Unset):
        current_yield (str | Unset):
        current_price (str | Unset):
        sp_outlook (str | Unset):
        sp_outlook_date (datetime.date | Unset):
        sp_creditwatch (str | Unset):
        sp_creditwatch_date (datetime.date | Unset):
        perpetual (bool | Unset):
        country_issue (str | Unset):
        country_domicile (str | Unset):
        days_until_maturity (int | Unset):
        liquidity_rating (str | Unset):
        seniority (str | Unset):
        partial_par (bool | Unset):
        minimum_order_size (str | Unset):
        minimum_order_increment (str | Unset):
    """

    cusip: str | Unset = UNSET
    issuer: str | Unset = UNSET
    issuer_symbol: str | Unset = UNSET
    symbol: str | Unset = UNSET
    description: str | Unset = UNSET
    description_short: str | Unset = UNSET
    bond_type: str | Unset = UNSET
    treasury_subtype: str | Unset = UNSET
    treasury_duration: str | Unset = UNSET
    bond_status: str | Unset = UNSET
    issue_date: datetime.date | Unset = UNSET
    issue_price: str | Unset = UNSET
    issue_size: str | Unset = UNSET
    maturity_date: datetime.date | Unset = UNSET
    rating: str | Unset = UNSET
    rating_category: str | Unset = UNSET
    coupon: str | Unset = UNSET
    coupon_frequency: str | Unset = UNSET
    next_coupon_date: datetime.date | Unset = UNSET
    par_value: str | Unset = UNSET
    accrued_interest: str | Unset = UNSET
    callable_: bool | Unset = UNSET
    next_call_date: datetime.date | Unset = UNSET
    next_call_price: str | Unset = UNSET
    current_yield: str | Unset = UNSET
    current_price: str | Unset = UNSET
    sp_outlook: str | Unset = UNSET
    sp_outlook_date: datetime.date | Unset = UNSET
    sp_creditwatch: str | Unset = UNSET
    sp_creditwatch_date: datetime.date | Unset = UNSET
    perpetual: bool | Unset = UNSET
    country_issue: str | Unset = UNSET
    country_domicile: str | Unset = UNSET
    days_until_maturity: int | Unset = UNSET
    liquidity_rating: str | Unset = UNSET
    seniority: str | Unset = UNSET
    partial_par: bool | Unset = UNSET
    minimum_order_size: str | Unset = UNSET
    minimum_order_increment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cusip = self.cusip

        issuer = self.issuer

        issuer_symbol = self.issuer_symbol

        symbol = self.symbol

        description = self.description

        description_short = self.description_short

        bond_type = self.bond_type

        treasury_subtype = self.treasury_subtype

        treasury_duration = self.treasury_duration

        bond_status = self.bond_status

        issue_date: str | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        issue_price = self.issue_price

        issue_size = self.issue_size

        maturity_date: str | Unset = UNSET
        if not isinstance(self.maturity_date, Unset):
            maturity_date = self.maturity_date.isoformat()

        rating = self.rating

        rating_category = self.rating_category

        coupon = self.coupon

        coupon_frequency = self.coupon_frequency

        next_coupon_date: str | Unset = UNSET
        if not isinstance(self.next_coupon_date, Unset):
            next_coupon_date = self.next_coupon_date.isoformat()

        par_value = self.par_value

        accrued_interest = self.accrued_interest

        callable_ = self.callable_

        next_call_date: str | Unset = UNSET
        if not isinstance(self.next_call_date, Unset):
            next_call_date = self.next_call_date.isoformat()

        next_call_price = self.next_call_price

        current_yield = self.current_yield

        current_price = self.current_price

        sp_outlook = self.sp_outlook

        sp_outlook_date: str | Unset = UNSET
        if not isinstance(self.sp_outlook_date, Unset):
            sp_outlook_date = self.sp_outlook_date.isoformat()

        sp_creditwatch = self.sp_creditwatch

        sp_creditwatch_date: str | Unset = UNSET
        if not isinstance(self.sp_creditwatch_date, Unset):
            sp_creditwatch_date = self.sp_creditwatch_date.isoformat()

        perpetual = self.perpetual

        country_issue = self.country_issue

        country_domicile = self.country_domicile

        days_until_maturity = self.days_until_maturity

        liquidity_rating = self.liquidity_rating

        seniority = self.seniority

        partial_par = self.partial_par

        minimum_order_size = self.minimum_order_size

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

        issuer = d.pop("issuer", UNSET)

        issuer_symbol = d.pop("issuerSymbol", UNSET)

        symbol = d.pop("symbol", UNSET)

        description = d.pop("description", UNSET)

        description_short = d.pop("descriptionShort", UNSET)

        bond_type = d.pop("bondType", UNSET)

        treasury_subtype = d.pop("treasurySubtype", UNSET)

        treasury_duration = d.pop("treasuryDuration", UNSET)

        bond_status = d.pop("bondStatus", UNSET)

        _issue_date = d.pop("issueDate", UNSET)
        issue_date: datetime.date | Unset
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = datetime.date.fromisoformat(_issue_date)

        issue_price = d.pop("issuePrice", UNSET)

        issue_size = d.pop("issueSize", UNSET)

        _maturity_date = d.pop("maturityDate", UNSET)
        maturity_date: datetime.date | Unset
        if isinstance(_maturity_date, Unset):
            maturity_date = UNSET
        else:
            maturity_date = datetime.date.fromisoformat(_maturity_date)

        rating = d.pop("rating", UNSET)

        rating_category = d.pop("ratingCategory", UNSET)

        coupon = d.pop("coupon", UNSET)

        coupon_frequency = d.pop("couponFrequency", UNSET)

        _next_coupon_date = d.pop("nextCouponDate", UNSET)
        next_coupon_date: datetime.date | Unset
        if isinstance(_next_coupon_date, Unset):
            next_coupon_date = UNSET
        else:
            next_coupon_date = datetime.date.fromisoformat(_next_coupon_date)

        par_value = d.pop("parValue", UNSET)

        accrued_interest = d.pop("accruedInterest", UNSET)

        callable_ = d.pop("callable", UNSET)

        _next_call_date = d.pop("nextCallDate", UNSET)
        next_call_date: datetime.date | Unset
        if isinstance(_next_call_date, Unset):
            next_call_date = UNSET
        else:
            next_call_date = datetime.date.fromisoformat(_next_call_date)

        next_call_price = d.pop("nextCallPrice", UNSET)

        current_yield = d.pop("currentYield", UNSET)

        current_price = d.pop("currentPrice", UNSET)

        sp_outlook = d.pop("spOutlook", UNSET)

        _sp_outlook_date = d.pop("spOutlookDate", UNSET)
        sp_outlook_date: datetime.date | Unset
        if isinstance(_sp_outlook_date, Unset):
            sp_outlook_date = UNSET
        else:
            sp_outlook_date = datetime.date.fromisoformat(_sp_outlook_date)

        sp_creditwatch = d.pop("spCreditwatch", UNSET)

        _sp_creditwatch_date = d.pop("spCreditwatchDate", UNSET)
        sp_creditwatch_date: datetime.date | Unset
        if isinstance(_sp_creditwatch_date, Unset):
            sp_creditwatch_date = UNSET
        else:
            sp_creditwatch_date = datetime.date.fromisoformat(_sp_creditwatch_date)

        perpetual = d.pop("perpetual", UNSET)

        country_issue = d.pop("countryIssue", UNSET)

        country_domicile = d.pop("countryDomicile", UNSET)

        days_until_maturity = d.pop("daysUntilMaturity", UNSET)

        liquidity_rating = d.pop("liquidityRating", UNSET)

        seniority = d.pop("seniority", UNSET)

        partial_par = d.pop("partialPar", UNSET)

        minimum_order_size = d.pop("minimumOrderSize", UNSET)

        minimum_order_increment = d.pop("minimumOrderIncrement", UNSET)

        com_hellopublic_fixedincomegateway_instrument_instrument_dto = cls(
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

        com_hellopublic_fixedincomegateway_instrument_instrument_dto.additional_properties = d
        return com_hellopublic_fixedincomegateway_instrument_instrument_dto

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
