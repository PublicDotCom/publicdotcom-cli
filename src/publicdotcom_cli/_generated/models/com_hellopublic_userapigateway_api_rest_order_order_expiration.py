from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration_time_in_force import (
    ComHellopublicUserapigatewayApiRestOrderOrderExpirationTimeInForce,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderOrderExpiration")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderOrderExpiration:
    """
    Attributes:
        time_in_force (ComHellopublicUserapigatewayApiRestOrderOrderExpirationTimeInForce): The time in for the order
        expiration_time (datetime.datetime | Unset): The expiration date. Only used when timeInForce is GTD, cannot be
            more than 90 days in the future
    """

    time_in_force: ComHellopublicUserapigatewayApiRestOrderOrderExpirationTimeInForce
    expiration_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_in_force = self.time_in_force.value

        expiration_time: str | Unset = UNSET
        if not isinstance(self.expiration_time, Unset):
            expiration_time = self.expiration_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeInForce": time_in_force,
            }
        )
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_in_force = ComHellopublicUserapigatewayApiRestOrderOrderExpirationTimeInForce(
            d.pop("timeInForce")
        )

        _expiration_time = d.pop("expirationTime", UNSET)
        expiration_time: datetime.datetime | Unset
        if isinstance(_expiration_time, Unset):
            expiration_time = UNSET
        else:
            expiration_time = isoparse(_expiration_time)

        com_hellopublic_userapigateway_api_rest_order_order_expiration = cls(
            time_in_force=time_in_force,
            expiration_time=expiration_time,
        )

        com_hellopublic_userapigateway_api_rest_order_order_expiration.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_order_expiration

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
