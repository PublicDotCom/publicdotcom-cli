from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_open_close_indicator import (
    ComHellopublicUserapigatewayApiRestOrderGatewayOrderOpenCloseIndicator,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_side import (
    ComHellopublicUserapigatewayApiRestOrderGatewayOrderSide,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_status import (
    ComHellopublicUserapigatewayApiRestOrderGatewayOrderStatus,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_type import (
    ComHellopublicUserapigatewayApiRestOrderGatewayOrderType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_leg import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration import (
        ComHellopublicUserapigatewayApiRestOrderOrderExpiration,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderGatewayOrder")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderGatewayOrder:
    """
    Attributes:
        order_id (UUID | Unset):
        instrument (ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument | Unset):
        created_at (datetime.datetime | Unset): Creation time of the order
        type_ (ComHellopublicUserapigatewayApiRestOrderGatewayOrderType | Unset):
        side (ComHellopublicUserapigatewayApiRestOrderGatewayOrderSide | Unset):
        status (ComHellopublicUserapigatewayApiRestOrderGatewayOrderStatus | Unset):
        quantity (str | Unset): Quantity of the order, mutually exclusive with notional value
        notional_value (str | Unset): Notional value (dollar amount) of the order, mutually exclusive with quantity
        expiration (ComHellopublicUserapigatewayApiRestOrderOrderExpiration | Unset):
        limit_price (str | Unset): Present if type = LIMIT
        stop_price (str | Unset): Present if type = STOP
        closed_at (datetime.datetime | Unset): The time the order reached a terminal state, like CANCELLED, FILLED,
            REJECTED, REPLACED
        open_close_indicator (ComHellopublicUserapigatewayApiRestOrderGatewayOrderOpenCloseIndicator | Unset): Present
            if the order is a single-leg option order, or if the order is a shorting order (sell-to-open or buy-to-close)
        filled_quantity (str | Unset): The filled quantity of the order, present if the order had at least one trade
        average_price (str | Unset): The average price per unit, present if the order had at least one trade
        legs (list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg] | Unset): If instrument.type =
            MULTI_LEG_INSTRUMENT, this contains the list of legs
        reject_reason (str | Unset):
    """

    order_id: UUID | Unset = UNSET
    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    type_: ComHellopublicUserapigatewayApiRestOrderGatewayOrderType | Unset = UNSET
    side: ComHellopublicUserapigatewayApiRestOrderGatewayOrderSide | Unset = UNSET
    status: ComHellopublicUserapigatewayApiRestOrderGatewayOrderStatus | Unset = UNSET
    quantity: str | Unset = UNSET
    notional_value: str | Unset = UNSET
    expiration: ComHellopublicUserapigatewayApiRestOrderOrderExpiration | Unset = UNSET
    limit_price: str | Unset = UNSET
    stop_price: str | Unset = UNSET
    closed_at: datetime.datetime | Unset = UNSET
    open_close_indicator: (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderOpenCloseIndicator | Unset
    ) = UNSET
    filled_quantity: str | Unset = UNSET
    average_price: str | Unset = UNSET
    legs: list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg] | Unset = UNSET
    reject_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id: str | Unset = UNSET
        if not isinstance(self.order_id, Unset):
            order_id = str(self.order_id)

        instrument: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instrument, Unset):
            instrument = self.instrument.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        quantity = self.quantity

        notional_value = self.notional_value

        expiration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.to_dict()

        limit_price = self.limit_price

        stop_price = self.stop_price

        closed_at: str | Unset = UNSET
        if not isinstance(self.closed_at, Unset):
            closed_at = self.closed_at.isoformat()

        open_close_indicator: str | Unset = UNSET
        if not isinstance(self.open_close_indicator, Unset):
            open_close_indicator = self.open_close_indicator.value

        filled_quantity = self.filled_quantity

        average_price = self.average_price

        legs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.legs, Unset):
            legs = []
            for legs_item_data in self.legs:
                legs_item = legs_item_data.to_dict()
                legs.append(legs_item)

        reject_reason = self.reject_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if side is not UNSET:
            field_dict["side"] = side
        if status is not UNSET:
            field_dict["status"] = status
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if notional_value is not UNSET:
            field_dict["notionalValue"] = notional_value
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if limit_price is not UNSET:
            field_dict["limitPrice"] = limit_price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if open_close_indicator is not UNSET:
            field_dict["openCloseIndicator"] = open_close_indicator
        if filled_quantity is not UNSET:
            field_dict["filledQuantity"] = filled_quantity
        if average_price is not UNSET:
            field_dict["averagePrice"] = average_price
        if legs is not UNSET:
            field_dict["legs"] = legs
        if reject_reason is not UNSET:
            field_dict["rejectReason"] = reject_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_leg import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration import (
            ComHellopublicUserapigatewayApiRestOrderOrderExpiration,
        )

        d = dict(src_dict)
        _order_id = d.pop("orderId", UNSET)
        order_id: UUID | Unset
        if isinstance(_order_id, Unset):
            order_id = UNSET
        else:
            order_id = UUID(_order_id)

        _instrument = d.pop("instrument", UNSET)
        instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument | Unset
        if isinstance(_instrument, Unset):
            instrument = UNSET
        else:
            instrument = ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
                _instrument
            )

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _type_ = d.pop("type", UNSET)
        type_: ComHellopublicUserapigatewayApiRestOrderGatewayOrderType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ComHellopublicUserapigatewayApiRestOrderGatewayOrderType(_type_)

        _side = d.pop("side", UNSET)
        side: ComHellopublicUserapigatewayApiRestOrderGatewayOrderSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = ComHellopublicUserapigatewayApiRestOrderGatewayOrderSide(_side)

        _status = d.pop("status", UNSET)
        status: ComHellopublicUserapigatewayApiRestOrderGatewayOrderStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ComHellopublicUserapigatewayApiRestOrderGatewayOrderStatus(_status)

        quantity = d.pop("quantity", UNSET)

        notional_value = d.pop("notionalValue", UNSET)

        _expiration = d.pop("expiration", UNSET)
        expiration: ComHellopublicUserapigatewayApiRestOrderOrderExpiration | Unset
        if isinstance(_expiration, Unset):
            expiration = UNSET
        else:
            expiration = ComHellopublicUserapigatewayApiRestOrderOrderExpiration.from_dict(
                _expiration
            )

        limit_price = d.pop("limitPrice", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        _closed_at = d.pop("closedAt", UNSET)
        closed_at: datetime.datetime | Unset
        if isinstance(_closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = isoparse(_closed_at)

        _open_close_indicator = d.pop("openCloseIndicator", UNSET)
        open_close_indicator: (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderOpenCloseIndicator | Unset
        )
        if isinstance(_open_close_indicator, Unset):
            open_close_indicator = UNSET
        else:
            open_close_indicator = (
                ComHellopublicUserapigatewayApiRestOrderGatewayOrderOpenCloseIndicator(
                    _open_close_indicator
                )
            )

        filled_quantity = d.pop("filledQuantity", UNSET)

        average_price = d.pop("averagePrice", UNSET)

        _legs = d.pop("legs", UNSET)
        legs: list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg] | Unset = UNSET
        if _legs is not UNSET:
            legs = []
            for legs_item_data in _legs:
                legs_item = ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg.from_dict(
                    legs_item_data
                )

                legs.append(legs_item)

        reject_reason = d.pop("rejectReason", UNSET)

        com_hellopublic_userapigateway_api_rest_order_gateway_order = cls(
            order_id=order_id,
            instrument=instrument,
            created_at=created_at,
            type_=type_,
            side=side,
            status=status,
            quantity=quantity,
            notional_value=notional_value,
            expiration=expiration,
            limit_price=limit_price,
            stop_price=stop_price,
            closed_at=closed_at,
            open_close_indicator=open_close_indicator,
            filled_quantity=filled_quantity,
            average_price=average_price,
            legs=legs,
            reject_reason=reject_reason,
        )

        com_hellopublic_userapigateway_api_rest_order_gateway_order.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_gateway_order

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
