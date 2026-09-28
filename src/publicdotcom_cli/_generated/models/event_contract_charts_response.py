from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_contract_chart import EventContractChart


T = TypeVar("T", bound="EventContractChartsResponse")


@_attrs_define
class EventContractChartsResponse:
    """A symbol is omitted from charts when it is unknown, has no candles, or has no price in the requested period.

    Attributes:
        period (str | Unset):
        charts (list[EventContractChart] | Unset):
    """

    period: str | Unset = UNSET
    charts: list[EventContractChart] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period = self.period

        charts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.charts, Unset):
            charts = []
            for charts_item_data in self.charts:
                charts_item = charts_item_data.to_dict()
                charts.append(charts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if charts is not UNSET:
            field_dict["charts"] = charts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_contract_chart import EventContractChart

        d = dict(src_dict)
        period = d.pop("period", UNSET)

        _charts = d.pop("charts", UNSET)
        charts: list[EventContractChart] | Unset = UNSET
        if _charts is not UNSET:
            charts = []
            for charts_item_data in _charts:
                charts_item = EventContractChart.from_dict(charts_item_data)

                charts.append(charts_item)

        event_contract_charts_response = cls(
            period=period,
            charts=charts,
        )

        event_contract_charts_response.additional_properties = d
        return event_contract_charts_response

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
