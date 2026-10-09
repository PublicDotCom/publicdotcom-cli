from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiDto",
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiDto:
    """This specific class does intentionally not have any outcomes.

    Attributes:
        title (str):
        event_symbol (str):
        volume (str):
        category (str):
        subcategories (list[str]):
        symbols (list[str]):
        resolution_time (datetime.datetime | Unset):
        resolved (bool | Unset):
        halted (bool | Unset):
    """

    title: str
    event_symbol: str
    volume: str
    category: str
    subcategories: list[str]
    symbols: list[str]
    resolution_time: datetime.datetime | Unset = UNSET
    resolved: bool | Unset = UNSET
    halted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        event_symbol = self.event_symbol

        volume = self.volume

        category = self.category

        subcategories = self.subcategories

        symbols = self.symbols

        resolution_time: str | Unset = UNSET
        if not isinstance(self.resolution_time, Unset):
            resolution_time = self.resolution_time.isoformat()

        resolved = self.resolved

        halted = self.halted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "eventSymbol": event_symbol,
                "volume": volume,
                "category": category,
                "subcategories": subcategories,
                "symbols": symbols,
            }
        )
        if resolution_time is not UNSET:
            field_dict["resolutionTime"] = resolution_time
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if halted is not UNSET:
            field_dict["halted"] = halted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        event_symbol = d.pop("eventSymbol")

        volume = d.pop("volume")

        category = d.pop("category")

        subcategories = cast(list[str], d.pop("subcategories"))

        symbols = cast(list[str], d.pop("symbols"))

        _resolution_time = d.pop("resolutionTime", UNSET)
        resolution_time: datetime.datetime | Unset
        if isinstance(_resolution_time, Unset):
            resolution_time = UNSET
        else:
            resolution_time = datetime.datetime.fromisoformat(_resolution_time)

        resolved = d.pop("resolved", UNSET)

        halted = d.pop("halted", UNSET)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_dto = cls(
            title=title,
            event_symbol=event_symbol,
            volume=volume,
            category=category,
            subcategories=subcategories,
            symbols=symbols,
            resolution_time=resolution_time,
            resolved=resolved,
            halted=halted,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_dto

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
