from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicHoldingsystemCoreTypesOptionPriceIncrement")


@_attrs_define
class ComHellopublicHoldingsystemCoreTypesOptionPriceIncrement:
    """Record representing price increments below and above $3.

    Attributes:
        increment_below_3 (str | Unset):
        increment_above_3 (str | Unset):
    """

    increment_below_3: str | Unset = UNSET
    increment_above_3: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        increment_below_3 = self.increment_below_3

        increment_above_3 = self.increment_above_3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if increment_below_3 is not UNSET:
            field_dict["incrementBelow3"] = increment_below_3
        if increment_above_3 is not UNSET:
            field_dict["incrementAbove3"] = increment_above_3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        increment_below_3 = d.pop("incrementBelow3", UNSET)

        increment_above_3 = d.pop("incrementAbove3", UNSET)

        com_hellopublic_holdingsystem_core_types_option_price_increment = cls(
            increment_below_3=increment_below_3,
            increment_above_3=increment_above_3,
        )

        com_hellopublic_holdingsystem_core_types_option_price_increment.additional_properties = d
        return com_hellopublic_holdingsystem_core_types_option_price_increment

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
