from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_dto import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiDto,
    )


T = TypeVar(
    "T",
    bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto",
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto:
    """
    Attributes:
        content
            (list[ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiDto]):
        next_token (str | Unset):
    """

    content: list[
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiDto
    ]
    next_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

        next_token = self.next_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_dto import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiDto,
        )

        d = dict(src_dict)
        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiDto.from_dict(
                content_item_data
            )

            content.append(content_item)

        next_token = d.pop("nextToken", UNSET)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_list_dto = cls(
            content=content,
            next_token=next_token,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_list_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_summary_user_api_list_dto

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
