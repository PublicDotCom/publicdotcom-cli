from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_option_details_type import (
    ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetailsType,
)

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails:
    """
    Attributes:
        base_symbol (str):
        type_ (ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetailsType):
        strike_price (str):
        option_expire_date (datetime.date):
    """

    base_symbol: str
    type_: ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetailsType
    strike_price: str
    option_expire_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_symbol = self.base_symbol

        type_ = self.type_.value

        strike_price = self.strike_price

        option_expire_date = self.option_expire_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseSymbol": base_symbol,
                "type": type_,
                "strikePrice": strike_price,
                "optionExpireDate": option_expire_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_symbol = d.pop("baseSymbol")

        type_ = ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetailsType(d.pop("type"))

        strike_price = d.pop("strikePrice")

        option_expire_date = isoparse(d.pop("optionExpireDate")).date()

        com_hellopublic_userapigateway_api_rest_preflight_gateway_option_details = cls(
            base_symbol=base_symbol,
            type_=type_,
            strike_price=strike_price,
            option_expire_date=option_expire_date,
        )

        com_hellopublic_userapigateway_api_rest_preflight_gateway_option_details.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_gateway_option_details

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
