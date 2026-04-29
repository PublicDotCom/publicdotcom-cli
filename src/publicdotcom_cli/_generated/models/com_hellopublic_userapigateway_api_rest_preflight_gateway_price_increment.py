from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement:
    """Price increment information for option orders.

    Attributes:
        increment_below_3 (str | Unset):
        increment_above_3 (str | Unset):
        current_increment (str | Unset):
    """

    increment_below_3: str | Unset = UNSET
    increment_above_3: str | Unset = UNSET
    current_increment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        increment_below_3 = self.increment_below_3

        increment_above_3 = self.increment_above_3

        current_increment = self.current_increment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if increment_below_3 is not UNSET:
            field_dict["incrementBelow3"] = increment_below_3
        if increment_above_3 is not UNSET:
            field_dict["incrementAbove3"] = increment_above_3
        if current_increment is not UNSET:
            field_dict["currentIncrement"] = current_increment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        increment_below_3 = d.pop("incrementBelow3", UNSET)

        increment_above_3 = d.pop("incrementAbove3", UNSET)

        current_increment = d.pop("currentIncrement", UNSET)

        com_hellopublic_userapigateway_api_rest_preflight_gateway_price_increment = cls(
            increment_below_3=increment_below_3,
            increment_above_3=increment_above_3,
            current_increment=current_increment,
        )

        com_hellopublic_userapigateway_api_rest_preflight_gateway_price_increment.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_gateway_price_increment

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
