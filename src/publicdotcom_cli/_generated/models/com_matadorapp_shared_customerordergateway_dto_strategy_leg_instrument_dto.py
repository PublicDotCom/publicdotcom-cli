from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_matadorapp_shared_customerordergateway_dto_strategy_leg_instrument_dto_type import (
    ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDtoType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDto")


@_attrs_define
class ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDto:
    """Defines the leg instrument.

    Attributes:
        symbol (str): Instrument symbol.
        base_symbol (str | Unset): Base symbol. Only available for option leg.
        type_ (ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDtoType | Unset): Type of option. Only
            available for option leg.
        strike_price (str | Unset): Option strike price. Only available for option leg.
        expiration_date (datetime.date | Unset): Option expiration date. Only available for option leg.
    """

    symbol: str
    base_symbol: str | Unset = UNSET
    type_: ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDtoType | Unset = UNSET
    strike_price: str | Unset = UNSET
    expiration_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        base_symbol = self.base_symbol

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        strike_price = self.strike_price

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
            }
        )
        if base_symbol is not UNSET:
            field_dict["baseSymbol"] = base_symbol
        if type_ is not UNSET:
            field_dict["type"] = type_
        if strike_price is not UNSET:
            field_dict["strikePrice"] = strike_price
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        base_symbol = d.pop("baseSymbol", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDtoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDtoType(_type_)

        strike_price = d.pop("strikePrice", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.date | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = datetime.date.fromisoformat(_expiration_date)

        com_matadorapp_shared_customerordergateway_dto_strategy_leg_instrument_dto = cls(
            symbol=symbol,
            base_symbol=base_symbol,
            type_=type_,
            strike_price=strike_price,
            expiration_date=expiration_date,
        )

        com_matadorapp_shared_customerordergateway_dto_strategy_leg_instrument_dto.additional_properties = d
        return com_matadorapp_shared_customerordergateway_dto_strategy_leg_instrument_dto

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
