from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_frequency_dto_frequencies_item import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDtoFrequenciesItem,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDto"
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDto:
    """
    Attributes:
        frequencies
            (list[ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDtoFrequenciesItem]):
        show (bool | Unset):
    """

    frequencies: list[
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDtoFrequenciesItem
    ]
    show: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frequencies = []
        for frequencies_item_data in self.frequencies:
            frequencies_item = frequencies_item_data.value
            frequencies.append(frequencies_item)

        show = self.show

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frequencies": frequencies,
            }
        )
        if show is not UNSET:
            field_dict["show"] = show

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frequencies = []
        _frequencies = d.pop("frequencies")
        for frequencies_item_data in _frequencies:
            frequencies_item = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDtoFrequenciesItem(
                frequencies_item_data
            )

            frequencies.append(frequencies_item)

        show = d.pop("show", UNSET)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_frequency_dto = (
            cls(
                frequencies=frequencies,
                show=show,
            )
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_frequency_dto.additional_properties = d
        return (
            com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_frequency_dto
        )

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
