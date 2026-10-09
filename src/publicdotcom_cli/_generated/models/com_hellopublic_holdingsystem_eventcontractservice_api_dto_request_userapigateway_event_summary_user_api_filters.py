from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_filters_frequencies_item import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFiltersFrequenciesItem,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters",
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters:
    """
    Attributes:
        event_symbols (list[str]):
        frequencies (list[ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiF
            iltersFrequenciesItem]):
        resolution_time_start (datetime.datetime | Unset):
        resolution_time_end (datetime.datetime | Unset):
    """

    event_symbols: list[str]
    frequencies: list[
        ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFiltersFrequenciesItem
    ]
    resolution_time_start: datetime.datetime | Unset = UNSET
    resolution_time_end: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_symbols = self.event_symbols

        frequencies = []
        for frequencies_item_data in self.frequencies:
            frequencies_item = frequencies_item_data.value
            frequencies.append(frequencies_item)

        resolution_time_start: str | Unset = UNSET
        if not isinstance(self.resolution_time_start, Unset):
            resolution_time_start = self.resolution_time_start.isoformat()

        resolution_time_end: str | Unset = UNSET
        if not isinstance(self.resolution_time_end, Unset):
            resolution_time_end = self.resolution_time_end.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventSymbols": event_symbols,
                "frequencies": frequencies,
            }
        )
        if resolution_time_start is not UNSET:
            field_dict["resolutionTimeStart"] = resolution_time_start
        if resolution_time_end is not UNSET:
            field_dict["resolutionTimeEnd"] = resolution_time_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_symbols = cast(list[str], d.pop("eventSymbols"))

        frequencies = []
        _frequencies = d.pop("frequencies")
        for frequencies_item_data in _frequencies:
            frequencies_item = ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFiltersFrequenciesItem(
                frequencies_item_data
            )

            frequencies.append(frequencies_item)

        _resolution_time_start = d.pop("resolutionTimeStart", UNSET)
        resolution_time_start: datetime.datetime | Unset
        if isinstance(_resolution_time_start, Unset):
            resolution_time_start = UNSET
        else:
            resolution_time_start = datetime.datetime.fromisoformat(_resolution_time_start)

        _resolution_time_end = d.pop("resolutionTimeEnd", UNSET)
        resolution_time_end: datetime.datetime | Unset
        if isinstance(_resolution_time_end, Unset):
            resolution_time_end = UNSET
        else:
            resolution_time_end = datetime.datetime.fromisoformat(_resolution_time_end)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_filters = cls(
            event_symbols=event_symbols,
            frequencies=frequencies,
            resolution_time_start=resolution_time_start,
            resolution_time_end=resolution_time_end,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_filters.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_filters

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
