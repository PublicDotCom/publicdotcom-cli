from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGainType0")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGainType0:
    """
    Attributes:
        gain_value (str | Unset):
        gain_percentage (str | Unset):
        timestamp (datetime.datetime | Unset):
    """

    gain_value: str | Unset = UNSET
    gain_percentage: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gain_value = self.gain_value

        gain_percentage = self.gain_percentage

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gain_value is not UNSET:
            field_dict["gainValue"] = gain_value
        if gain_percentage is not UNSET:
            field_dict["gainPercentage"] = gain_percentage
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gain_value = d.pop("gainValue", UNSET)

        gain_percentage = d.pop("gainPercentage", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        com_hellopublic_userapigateway_api_rest_portfolio_gain_type_0 = cls(
            gain_value=gain_value,
            gain_percentage=gain_percentage,
            timestamp=timestamp,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gain_type_0.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gain_type_0

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
