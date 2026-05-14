from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bar import Bar


T = TypeVar("T", bound="MarketSessionBars")


@_attrs_define
class MarketSessionBars:
    """
    Attributes:
        expected_bars (int):
        bars (list[Bar]):
    """

    expected_bars: int
    bars: list[Bar]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_bars = self.expected_bars

        bars = []
        for bars_item_data in self.bars:
            bars_item = bars_item_data.to_dict()
            bars.append(bars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expectedBars": expected_bars,
                "bars": bars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bar import Bar

        d = dict(src_dict)
        expected_bars = d.pop("expectedBars")

        bars = []
        _bars = d.pop("bars")
        for bars_item_data in _bars:
            bars_item = Bar.from_dict(bars_item_data)

            bars.append(bars_item)

        market_session_bars = cls(
            expected_bars=expected_bars,
            bars=bars,
        )

        market_session_bars.additional_properties = d
        return market_session_bars

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
