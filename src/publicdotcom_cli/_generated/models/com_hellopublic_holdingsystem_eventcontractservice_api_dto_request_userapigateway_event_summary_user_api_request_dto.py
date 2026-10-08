from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_request_dto_sorting_mode import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDtoSortingMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_filters import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters,
    )


T = TypeVar(
    "T",
    bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto",
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto:
    """
    Attributes:
        sorting_mode (ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiReque
            stDtoSortingMode): the sorting mode for the returned events.
        category (str | Unset): filter for a specific category.
        subcategory (str | Unset): filter for a specific subcategory.
        next_token (str | Unset): the next token for pagination.
        display_resolved_events (bool | Unset): whether to display resolved events.
        created_within_days (int | Unset): filter for events that have been created within the last x days.
        filters (ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters |
            Unset):
    """

    sorting_mode: ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDtoSortingMode
    category: str | Unset = UNSET
    subcategory: str | Unset = UNSET
    next_token: str | Unset = UNSET
    display_resolved_events: bool | Unset = UNSET
    created_within_days: int | Unset = UNSET
    filters: (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sorting_mode = self.sorting_mode.value

        category = self.category

        subcategory = self.subcategory

        next_token = self.next_token

        display_resolved_events = self.display_resolved_events

        created_within_days = self.created_within_days

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sortingMode": sorting_mode,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token
        if display_resolved_events is not UNSET:
            field_dict["displayResolvedEvents"] = display_resolved_events
        if created_within_days is not UNSET:
            field_dict["createdWithinDays"] = created_within_days
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_filters import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters,
        )

        d = dict(src_dict)
        sorting_mode = ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDtoSortingMode(
            d.pop("sortingMode")
        )

        category = d.pop("category", UNSET)

        subcategory = d.pop("subcategory", UNSET)

        next_token = d.pop("nextToken", UNSET)

        display_resolved_events = d.pop("displayResolvedEvents", UNSET)

        created_within_days = d.pop("createdWithinDays", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters
            | Unset
        )
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters.from_dict(
                _filters
            )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_request_dto = cls(
            sorting_mode=sorting_mode,
            category=category,
            subcategory=subcategory,
            next_token=next_token,
            display_resolved_events=display_resolved_events,
            created_within_days=created_within_days,
            filters=filters,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_request_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_request_userapigateway_event_summary_user_api_request_dto

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
