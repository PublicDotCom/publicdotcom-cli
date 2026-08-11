from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sort_object import SortObject


T = TypeVar("T", bound="PageableObject")


@_attrs_define
class PageableObject:
    """
    Attributes:
        offset (int | Unset):
        page_size (int | Unset):
        sort (SortObject | Unset):
        paged (bool | Unset):
        unpaged (bool | Unset):
        page_number (int | Unset):
    """

    offset: int | Unset = UNSET
    page_size: int | Unset = UNSET
    sort: SortObject | Unset = UNSET
    paged: bool | Unset = UNSET
    unpaged: bool | Unset = UNSET
    page_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        page_size = self.page_size

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        paged = self.paged

        unpaged = self.unpaged

        page_number = self.page_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if sort is not UNSET:
            field_dict["sort"] = sort
        if paged is not UNSET:
            field_dict["paged"] = paged
        if unpaged is not UNSET:
            field_dict["unpaged"] = unpaged
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sort_object import SortObject

        d = dict(src_dict)
        offset = d.pop("offset", UNSET)

        page_size = d.pop("pageSize", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: SortObject | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SortObject.from_dict(_sort)

        paged = d.pop("paged", UNSET)

        unpaged = d.pop("unpaged", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        pageable_object = cls(
            offset=offset,
            page_size=page_size,
            sort=sort,
            paged=paged,
            unpaged=unpaged,
            page_number=page_number,
        )

        pageable_object.additional_properties = d
        return pageable_object

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
