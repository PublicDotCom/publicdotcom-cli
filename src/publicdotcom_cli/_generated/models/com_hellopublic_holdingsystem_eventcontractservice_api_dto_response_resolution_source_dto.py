from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseResolutionSourceDto"
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseResolutionSourceDto:
    """
    Attributes:
        name (str | Unset):
        url (str | Unset):
    """

    name: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_resolution_source_dto = cls(
            name=name,
            url=url,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_resolution_source_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_resolution_source_dto

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
