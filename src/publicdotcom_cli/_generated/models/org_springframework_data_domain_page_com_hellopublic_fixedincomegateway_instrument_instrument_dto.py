from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_fixedincomegateway_instrument_instrument_dto import (
        ComHellopublicFixedincomegatewayInstrumentInstrumentDto,
    )
    from ..models.pageable_object import PageableObject
    from ..models.sort_object import SortObject


T = TypeVar(
    "T",
    bound="OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto",
)


@_attrs_define
class OrgSpringframeworkDataDomainPageComHellopublicFixedincomegatewayInstrumentInstrumentDto:
    """
    Attributes:
        total_elements (int | Unset):
        total_pages (int | Unset):
        size (int | Unset):
        content (list[ComHellopublicFixedincomegatewayInstrumentInstrumentDto] | Unset):
        number (int | Unset):
        number_of_elements (int | Unset):
        sort (SortObject | Unset):
        pageable (PageableObject | Unset):
        first (bool | Unset):
        last (bool | Unset):
        empty (bool | Unset):
    """

    total_elements: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    size: int | Unset = UNSET
    content: list[ComHellopublicFixedincomegatewayInstrumentInstrumentDto] | Unset = UNSET
    number: int | Unset = UNSET
    number_of_elements: int | Unset = UNSET
    sort: SortObject | Unset = UNSET
    pageable: PageableObject | Unset = UNSET
    first: bool | Unset = UNSET
    last: bool | Unset = UNSET
    empty: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_elements = self.total_elements

        total_pages = self.total_pages

        size = self.size

        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        number = self.number

        number_of_elements = self.number_of_elements

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        pageable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pageable, Unset):
            pageable = self.pageable.to_dict()

        first = self.first

        last = self.last

        empty = self.empty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if size is not UNSET:
            field_dict["size"] = size
        if content is not UNSET:
            field_dict["content"] = content
        if number is not UNSET:
            field_dict["number"] = number
        if number_of_elements is not UNSET:
            field_dict["numberOfElements"] = number_of_elements
        if sort is not UNSET:
            field_dict["sort"] = sort
        if pageable is not UNSET:
            field_dict["pageable"] = pageable
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_fixedincomegateway_instrument_instrument_dto import (
            ComHellopublicFixedincomegatewayInstrumentInstrumentDto,
        )
        from ..models.pageable_object import PageableObject
        from ..models.sort_object import SortObject

        d = dict(src_dict)
        total_elements = d.pop("totalElements", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        size = d.pop("size", UNSET)

        _content = d.pop("content", UNSET)
        content: list[ComHellopublicFixedincomegatewayInstrumentInstrumentDto] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = ComHellopublicFixedincomegatewayInstrumentInstrumentDto.from_dict(
                    content_item_data
                )

                content.append(content_item)

        number = d.pop("number", UNSET)

        number_of_elements = d.pop("numberOfElements", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: SortObject | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SortObject.from_dict(_sort)

        _pageable = d.pop("pageable", UNSET)
        pageable: PageableObject | Unset
        if isinstance(_pageable, Unset):
            pageable = UNSET
        else:
            pageable = PageableObject.from_dict(_pageable)

        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        empty = d.pop("empty", UNSET)

        org_springframework_data_domain_page_com_hellopublic_fixedincomegateway_instrument_instrument_dto = cls(
            total_elements=total_elements,
            total_pages=total_pages,
            size=size,
            content=content,
            number=number,
            number_of_elements=number_of_elements,
            sort=sort,
            pageable=pageable,
            first=first,
            last=last,
            empty=empty,
        )

        org_springframework_data_domain_page_com_hellopublic_fixedincomegateway_instrument_instrument_dto.additional_properties = d
        return org_springframework_data_domain_page_com_hellopublic_fixedincomegateway_instrument_instrument_dto

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
