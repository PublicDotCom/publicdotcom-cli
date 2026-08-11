from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LeadingFill")


@_attrs_define
class LeadingFill:
    """
    Attributes:
        start_timestamp (str): ISO-8601 start of the requested (visible) period — where the flat fill begins.
        end_timestamp (str): ISO-8601 timestamp of the first real data point — where the flat fill ends. Matches the
            first bar's timestamp.
        value (str): The value to draw the flat fill at (equal to the first real data point's value, so the fill meets
            the series).
        count (int): Number of leading grey bars to draw (same meaning for every timeframe). Index-based renderers use
            this to reserve/offset the leading width.
        included_in_total_expected_bars (bool): Whether `count` is already part of `totalExpectedBars`. false (non-DAY):
            additive — prepend `count` grey bars in front of the real series (total slots = count + totalExpectedBars). true
            (DAY): a subset of the fixed-session `totalExpectedBars` — the real bars start at index `count` (grey + real +
            trailing-empty = totalExpectedBars).
    """

    start_timestamp: str
    end_timestamp: str
    value: str
    count: int
    included_in_total_expected_bars: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_timestamp = self.start_timestamp

        end_timestamp = self.end_timestamp

        value = self.value

        count = self.count

        included_in_total_expected_bars = self.included_in_total_expected_bars

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startTimestamp": start_timestamp,
                "endTimestamp": end_timestamp,
                "value": value,
                "count": count,
                "includedInTotalExpectedBars": included_in_total_expected_bars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_timestamp = d.pop("startTimestamp")

        end_timestamp = d.pop("endTimestamp")

        value = d.pop("value")

        count = d.pop("count")

        included_in_total_expected_bars = d.pop("includedInTotalExpectedBars")

        leading_fill = cls(
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            value=value,
            count=count,
            included_in_total_expected_bars=included_in_total_expected_bars,
        )

        leading_fill.additional_properties = d
        return leading_fill

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
