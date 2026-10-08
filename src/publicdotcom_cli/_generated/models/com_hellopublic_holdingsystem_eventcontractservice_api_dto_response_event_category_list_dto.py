from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_category_dto import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryDto,
    )


T = TypeVar(
    "T", bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryListDto"
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryListDto:
    """
    Attributes:
        categories (list[ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryDto]):
    """

    categories: list[ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_category_dto import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryDto,
        )

        d = dict(src_dict)
        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryDto.from_dict(
                categories_item_data
            )

            categories.append(categories_item)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_category_list_dto = cls(
            categories=categories,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_category_list_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_event_category_list_dto

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
