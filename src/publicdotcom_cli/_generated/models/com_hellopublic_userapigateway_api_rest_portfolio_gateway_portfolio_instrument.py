from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_instrument_type import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrumentType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrument")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrument:
    """
    Attributes:
        symbol (str | Unset):
        name (str | Unset):
        type_ (ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrumentType | Unset):
    """

    symbol: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrumentType | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrumentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrumentType(
                _type_
            )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_instrument = cls(
            symbol=symbol,
            name=name,
            type_=type_,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_instrument.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_instrument

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
