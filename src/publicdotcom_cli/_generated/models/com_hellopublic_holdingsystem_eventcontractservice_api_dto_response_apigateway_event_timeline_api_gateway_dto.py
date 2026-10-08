from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventTimelineApiGatewayDto",
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventTimelineApiGatewayDto:
    """
    Attributes:
        open_time (datetime.datetime): the time when the event opens for trading.
        close_time (datetime.datetime): the time when this event closes for trading.
        expected_expiration_time (datetime.datetime | Unset): the expected expiration time in UTC.
        latest_expiration_time (datetime.datetime | Unset): the latest expiration time in UTC.
        settlement_time (datetime.datetime | Unset): the expected expiration time and settlement delay.
        settlement_delay_seconds (int | Unset): the duration to wait after settlement before payout occurs.
    """

    open_time: datetime.datetime
    close_time: datetime.datetime
    expected_expiration_time: datetime.datetime | Unset = UNSET
    latest_expiration_time: datetime.datetime | Unset = UNSET
    settlement_time: datetime.datetime | Unset = UNSET
    settlement_delay_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_time = self.open_time.isoformat()

        close_time = self.close_time.isoformat()

        expected_expiration_time: str | Unset = UNSET
        if not isinstance(self.expected_expiration_time, Unset):
            expected_expiration_time = self.expected_expiration_time.isoformat()

        latest_expiration_time: str | Unset = UNSET
        if not isinstance(self.latest_expiration_time, Unset):
            latest_expiration_time = self.latest_expiration_time.isoformat()

        settlement_time: str | Unset = UNSET
        if not isinstance(self.settlement_time, Unset):
            settlement_time = self.settlement_time.isoformat()

        settlement_delay_seconds = self.settlement_delay_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "openTime": open_time,
                "closeTime": close_time,
            }
        )
        if expected_expiration_time is not UNSET:
            field_dict["expectedExpirationTime"] = expected_expiration_time
        if latest_expiration_time is not UNSET:
            field_dict["latestExpirationTime"] = latest_expiration_time
        if settlement_time is not UNSET:
            field_dict["settlementTime"] = settlement_time
        if settlement_delay_seconds is not UNSET:
            field_dict["settlementDelaySeconds"] = settlement_delay_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_time = datetime.datetime.fromisoformat(d.pop("openTime"))

        close_time = datetime.datetime.fromisoformat(d.pop("closeTime"))

        _expected_expiration_time = d.pop("expectedExpirationTime", UNSET)
        expected_expiration_time: datetime.datetime | Unset
        if isinstance(_expected_expiration_time, Unset):
            expected_expiration_time = UNSET
        else:
            expected_expiration_time = datetime.datetime.fromisoformat(_expected_expiration_time)

        _latest_expiration_time = d.pop("latestExpirationTime", UNSET)
        latest_expiration_time: datetime.datetime | Unset
        if isinstance(_latest_expiration_time, Unset):
            latest_expiration_time = UNSET
        else:
            latest_expiration_time = datetime.datetime.fromisoformat(_latest_expiration_time)

        _settlement_time = d.pop("settlementTime", UNSET)
        settlement_time: datetime.datetime | Unset
        if isinstance(_settlement_time, Unset):
            settlement_time = UNSET
        else:
            settlement_time = datetime.datetime.fromisoformat(_settlement_time)

        settlement_delay_seconds = d.pop("settlementDelaySeconds", UNSET)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_timeline_api_gateway_dto = cls(
            open_time=open_time,
            close_time=close_time,
            expected_expiration_time=expected_expiration_time,
            latest_expiration_time=latest_expiration_time,
            settlement_time=settlement_time,
            settlement_delay_seconds=settlement_delay_seconds,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_timeline_api_gateway_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_timeline_api_gateway_dto

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
