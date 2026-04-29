from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteOneDayChange")


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteOneDayChange:
    """Represents the one-day price change data for a quote.

    The change values are provided by the data source (e.g., Xignite) and may differ from simple subtraction
    of current price minus previous close due to corporate actions, stock splits, or other adjustments.

        Attributes:
            change (str | Unset): The one-day price change in dollars
            percent_change (str | Unset): The one-day price change as a percentage
    """

    change: str | Unset = UNSET
    percent_change: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change = self.change

        percent_change = self.percent_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change is not UNSET:
            field_dict["change"] = change
        if percent_change is not UNSET:
            field_dict["percentChange"] = percent_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        change = d.pop("change", UNSET)

        percent_change = d.pop("percentChange", UNSET)

        com_hellopublic_userapigateway_api_rest_marketdata_quote_one_day_change = cls(
            change=change,
            percent_change=percent_change,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_one_day_change.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_quote_one_day_change

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
