from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_request_order_type import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequestOrderType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_leg import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration import (
        ComHellopublicUserapigatewayApiRestOrderOrderExpiration,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequest:
    """# PreflightMultiLegRequest
    Request for preflight calculations on multi-leg orders.

    ## Fields
    - **orderType** - The type of order (only LIMIT orders are allowed for multi-leg)
    - **expiration** - The order expiration configuration
    - **quantity** - The order quantity (number of strategies)
    - **limitPrice** - The limit price for the order (required for LIMIT orders)
    - **legs** - List of order legs (2-6 legs allowed, at most 1 equity leg)
    - **equityMarketSession** - The market session for equity legs
    - **validateOrder** - If true, the order will be validated against current account state. Defaults to true.

        Attributes:
            order_type (ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequestOrderType):
            expiration (ComHellopublicUserapigatewayApiRestOrderOrderExpiration):
            quantity (str):
            limit_price (str):
            legs (list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg]):
            validate_order (bool | Unset):
    """

    order_type: ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequestOrderType
    expiration: ComHellopublicUserapigatewayApiRestOrderOrderExpiration
    quantity: str
    limit_price: str
    legs: list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg]
    validate_order: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_type = self.order_type.value

        expiration = self.expiration.to_dict()

        quantity = self.quantity

        limit_price = self.limit_price

        legs = []
        for legs_item_data in self.legs:
            legs_item = legs_item_data.to_dict()
            legs.append(legs_item)

        validate_order = self.validate_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderType": order_type,
                "expiration": expiration,
                "quantity": quantity,
                "limitPrice": limit_price,
                "legs": legs,
            }
        )
        if validate_order is not UNSET:
            field_dict["validateOrder"] = validate_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_leg import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration import (
            ComHellopublicUserapigatewayApiRestOrderOrderExpiration,
        )

        d = dict(src_dict)
        order_type = ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequestOrderType(
            d.pop("orderType")
        )

        expiration = ComHellopublicUserapigatewayApiRestOrderOrderExpiration.from_dict(
            d.pop("expiration")
        )

        quantity = d.pop("quantity")

        limit_price = d.pop("limitPrice")

        legs = []
        _legs = d.pop("legs")
        for legs_item_data in _legs:
            legs_item = ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg.from_dict(
                legs_item_data
            )

            legs.append(legs_item)

        validate_order = d.pop("validateOrder", UNSET)

        com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_request = cls(
            order_type=order_type,
            expiration=expiration,
            quantity=quantity,
            limit_price=limit_price,
            legs=legs,
            validate_order=validate_order,
        )

        com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_request.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_request

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
