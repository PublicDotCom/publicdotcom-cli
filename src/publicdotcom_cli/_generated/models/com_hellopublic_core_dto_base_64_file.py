from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicCoreDtoBase64File")


@_attrs_define
class ComHellopublicCoreDtoBase64File:
    """
    Attributes:
        file_name (str | Unset):
        base_64_data (str | Unset):
    """

    file_name: str | Unset = UNSET
    base_64_data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        base_64_data = self.base_64_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if base_64_data is not UNSET:
            field_dict["base64Data"] = base_64_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName", UNSET)

        base_64_data = d.pop("base64Data", UNSET)

        com_hellopublic_core_dto_base_64_file = cls(
            file_name=file_name,
            base_64_data=base_64_data,
        )

        com_hellopublic_core_dto_base_64_file.additional_properties = d
        return com_hellopublic_core_dto_base_64_file

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
