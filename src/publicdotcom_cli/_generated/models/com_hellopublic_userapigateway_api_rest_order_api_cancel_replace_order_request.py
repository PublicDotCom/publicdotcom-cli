from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_order_api_cancel_replace_order_request_order_type import (
    ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequestOrderType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration import (
        ComHellopublicUserapigatewayApiRestOrderOrderExpiration,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest:
    """Used for replacing orders placed via the UserApiGatewayService or other service
    Replaces should not be placed in parallel as ordering is not guaranteed for individual HTTP calls

        Attributes:
            order_id (UUID): This value identifies the order to be replaced; if reused on the same account, the operation is
                idempotent.
                If the order is re-submitted due to a read timeout, do not modify any properties. If the original request
                succeeded, altering fields will have no effect.
            request_id (UUID): Id of the new order in UUID-format conforming to RFC 4122 (standard 8-4-4-4-12 format, e.g.,
                0d2abd8d-3625-4c83-a806-98abf35567cc).
                The new orderId must be globally unique over time.
            order_type (ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequestOrderType): The Type of order
            expiration (ComHellopublicUserapigatewayApiRestOrderOrderExpiration):
            quantity (str | Unset): The order quantity. Used when buying/selling whole shares and when selling fractional.
            limit_price (str | Unset): The limit price. Used when orderType = LIMIT or orderType = STOP_LIMIT
            stop_price (str | Unset): The stop price. Used when orderType = STOP or orderType = STOP_LIMIT
    """

    order_id: UUID
    request_id: UUID
    order_type: ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequestOrderType
    expiration: ComHellopublicUserapigatewayApiRestOrderOrderExpiration
    quantity: str | Unset = UNSET
    limit_price: str | Unset = UNSET
    stop_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = str(self.order_id)

        request_id = str(self.request_id)

        order_type = self.order_type.value

        expiration = self.expiration.to_dict()

        quantity = self.quantity

        limit_price = self.limit_price

        stop_price = self.stop_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderId": order_id,
                "requestId": request_id,
                "orderType": order_type,
                "expiration": expiration,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if limit_price is not UNSET:
            field_dict["limitPrice"] = limit_price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration import (
            ComHellopublicUserapigatewayApiRestOrderOrderExpiration,
        )

        d = dict(src_dict)
        order_id = UUID(d.pop("orderId"))

        request_id = UUID(d.pop("requestId"))

        order_type = ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequestOrderType(
            d.pop("orderType")
        )

        expiration = ComHellopublicUserapigatewayApiRestOrderOrderExpiration.from_dict(
            d.pop("expiration")
        )

        quantity = d.pop("quantity", UNSET)

        limit_price = d.pop("limitPrice", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        com_hellopublic_userapigateway_api_rest_order_api_cancel_replace_order_request = cls(
            order_id=order_id,
            request_id=request_id,
            order_type=order_type,
            expiration=expiration,
            quantity=quantity,
            limit_price=limit_price,
            stop_price=stop_price,
        )

        com_hellopublic_userapigateway_api_rest_order_api_cancel_replace_order_request.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_api_cancel_replace_order_request

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
