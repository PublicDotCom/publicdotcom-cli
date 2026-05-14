from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LastSessionClose")


@_attrs_define
class LastSessionClose:
    """
    Attributes:
        close (str):
        close_date (str):
        change (None | str | Unset):
        percent_change (None | str | Unset):
    """

    close: str
    close_date: str
    change: None | str | Unset = UNSET
    percent_change: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        close = self.close

        close_date = self.close_date

        change: None | str | Unset
        if isinstance(self.change, Unset):
            change = UNSET
        else:
            change = self.change

        percent_change: None | str | Unset
        if isinstance(self.percent_change, Unset):
            percent_change = UNSET
        else:
            percent_change = self.percent_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "close": close,
                "closeDate": close_date,
            }
        )
        if change is not UNSET:
            field_dict["change"] = change
        if percent_change is not UNSET:
            field_dict["percentChange"] = percent_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        close = d.pop("close")

        close_date = d.pop("closeDate")

        def _parse_change(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        change = _parse_change(d.pop("change", UNSET))

        def _parse_percent_change(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percent_change = _parse_percent_change(d.pop("percentChange", UNSET))

        last_session_close = cls(
            close=close,
            close_date=close_date,
            change=change,
            percent_change=percent_change,
        )

        last_session_close.additional_properties = d
        return last_session_close

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
