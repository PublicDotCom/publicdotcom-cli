from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicTradingCoreQuoteBondQuoteDetail")


@_attrs_define
class ComHellopublicTradingCoreQuoteBondQuoteDetail:
    """
    Attributes:
        type_ (str):
        ask_min_size (str | Unset):
        bid_min_size (str | Unset):
        ask_markup (str | Unset):
        bid_markup (str | Unset):
    """

    type_: str
    ask_min_size: str | Unset = UNSET
    bid_min_size: str | Unset = UNSET
    ask_markup: str | Unset = UNSET
    bid_markup: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ask_min_size = self.ask_min_size

        bid_min_size = self.bid_min_size

        ask_markup = self.ask_markup

        bid_markup = self.bid_markup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if ask_min_size is not UNSET:
            field_dict["askMinSize"] = ask_min_size
        if bid_min_size is not UNSET:
            field_dict["bidMinSize"] = bid_min_size
        if ask_markup is not UNSET:
            field_dict["askMarkup"] = ask_markup
        if bid_markup is not UNSET:
            field_dict["bidMarkup"] = bid_markup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        ask_min_size = d.pop("askMinSize", UNSET)

        bid_min_size = d.pop("bidMinSize", UNSET)

        ask_markup = d.pop("askMarkup", UNSET)

        bid_markup = d.pop("bidMarkup", UNSET)

        com_hellopublic_trading_core_quote_bond_quote_detail = cls(
            type_=type_,
            ask_min_size=ask_min_size,
            bid_min_size=bid_min_size,
            ask_markup=ask_markup,
            bid_markup=bid_markup,
        )

        com_hellopublic_trading_core_quote_bond_quote_detail.additional_properties = d
        return com_hellopublic_trading_core_quote_bond_quote_detail

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
