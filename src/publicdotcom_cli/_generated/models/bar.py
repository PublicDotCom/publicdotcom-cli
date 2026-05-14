from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Bar")


@_attrs_define
class Bar:
    """
    Attributes:
        timestamp (str):
        open_ (str):
        close (str):
        high (str):
        low (str):
        value (str):
        volume (int):
        gain_amount (None | str | Unset):
        gain_percentage (None | str | Unset):
    """

    timestamp: str
    open_: str
    close: str
    high: str
    low: str
    value: str
    volume: int
    gain_amount: None | str | Unset = UNSET
    gain_percentage: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        open_ = self.open_

        close = self.close

        high = self.high

        low = self.low

        value = self.value

        volume = self.volume

        gain_amount: None | str | Unset
        if isinstance(self.gain_amount, Unset):
            gain_amount = UNSET
        else:
            gain_amount = self.gain_amount

        gain_percentage: None | str | Unset
        if isinstance(self.gain_percentage, Unset):
            gain_percentage = UNSET
        else:
            gain_percentage = self.gain_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "open": open_,
                "close": close,
                "high": high,
                "low": low,
                "value": value,
                "volume": volume,
            }
        )
        if gain_amount is not UNSET:
            field_dict["gainAmount"] = gain_amount
        if gain_percentage is not UNSET:
            field_dict["gainPercentage"] = gain_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        open_ = d.pop("open")

        close = d.pop("close")

        high = d.pop("high")

        low = d.pop("low")

        value = d.pop("value")

        volume = d.pop("volume")

        def _parse_gain_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gain_amount = _parse_gain_amount(d.pop("gainAmount", UNSET))

        def _parse_gain_percentage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gain_percentage = _parse_gain_percentage(d.pop("gainPercentage", UNSET))

        bar = cls(
            timestamp=timestamp,
            open_=open_,
            close=close,
            high=high,
            low=low,
            value=value,
            volume=volume,
            gain_amount=gain_amount,
            gain_percentage=gain_percentage,
        )

        bar.additional_properties = d
        return bar

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
