from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_v2_gateway_order_v2 import (
        ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders:
    """
    Attributes:
        orders (list[ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2] | Unset):
    """

    orders: list[ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_v2_gateway_order_v2 import (
            ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2,
        )

        d = dict(src_dict)
        _orders = d.pop("orders", UNSET)
        orders: list[ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2.from_dict(
                    orders_item_data
                )

                orders.append(orders_item)

        com_hellopublic_userapigateway_api_rest_order_v2_gateway_orders = cls(
            orders=orders,
        )

        com_hellopublic_userapigateway_api_rest_order_v2_gateway_orders.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_v2_gateway_orders

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
