from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_frequency_dto import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDto,
    )


T = TypeVar(
    "T", bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryDto"
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryDto:
    """
    Attributes:
        category (str):
        subcategories (list[str]):
        event_frequency (ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDto):
    """

    category: str
    subcategories: list[str]
    event_frequency: ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        subcategories = self.subcategories

        event_frequency = self.event_frequency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "subcategories": subcategories,
                "eventFrequency": event_frequency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_frequency_dto import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDto,
        )

        d = dict(src_dict)
        category = d.pop("category")

        subcategories = cast(list[str], d.pop("subcategories"))

        event_frequency = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDto.from_dict(
            d.pop("eventFrequency")
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_category_dto = (
            cls(
                category=category,
                subcategories=subcategories,
                event_frequency=event_frequency,
            )
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_category_dto.additional_properties = d
        return (
            com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_category_dto
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
