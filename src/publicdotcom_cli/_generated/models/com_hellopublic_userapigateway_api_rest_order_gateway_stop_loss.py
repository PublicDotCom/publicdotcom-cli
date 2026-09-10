from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderGatewayStopLoss")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderGatewayStopLoss:
    """The stop-loss leg of a bracket order. Placed as a STOP order when only `stopPrice` is present, or as a
    STOP_LIMIT order when `limitPrice` is also present.

        Attributes:
            stop_price (str): the stop price that activates the stop-loss order
            limit_price (str | Unset): optional limit price; when present the stop-loss is placed as a STOP_LIMIT order
    """

    stop_price: str
    limit_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop_price = self.stop_price

        limit_price = self.limit_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stopPrice": stop_price,
            }
        )
        if limit_price is not UNSET:
            field_dict["limitPrice"] = limit_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stop_price = d.pop("stopPrice")

        limit_price = d.pop("limitPrice", UNSET)

        com_hellopublic_userapigateway_api_rest_order_gateway_stop_loss = cls(
            stop_price=stop_price,
            limit_price=limit_price,
        )

        com_hellopublic_userapigateway_api_rest_order_gateway_stop_loss.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_gateway_stop_loss

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
