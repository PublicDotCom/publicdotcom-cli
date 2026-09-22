from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_order_v2_gateway_trade_side import (
    ComHellopublicUserapigatewayApiRestOrderV2GatewayTradeSide,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderV2GatewayTrade")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderV2GatewayTrade:
    """
    Attributes:
        instrument (ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument | Unset):
        quantity (str | Unset):
        price (str | Unset):
        side (ComHellopublicUserapigatewayApiRestOrderV2GatewayTradeSide | Unset):
        trade_id (str | Unset):
        timestamp (datetime.datetime | Unset):
    """

    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument | Unset = UNSET
    quantity: str | Unset = UNSET
    price: str | Unset = UNSET
    side: ComHellopublicUserapigatewayApiRestOrderV2GatewayTradeSide | Unset = UNSET
    trade_id: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instrument, Unset):
            instrument = self.instrument.to_dict()

        quantity = self.quantity

        price = self.price

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        trade_id = self.trade_id

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if price is not UNSET:
            field_dict["price"] = price
        if side is not UNSET:
            field_dict["side"] = side
        if trade_id is not UNSET:
            field_dict["tradeId"] = trade_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )

        d = dict(src_dict)
        _instrument = d.pop("instrument", UNSET)
        instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument | Unset
        if isinstance(_instrument, Unset):
            instrument = UNSET
        else:
            instrument = ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
                _instrument
            )

        quantity = d.pop("quantity", UNSET)

        price = d.pop("price", UNSET)

        _side = d.pop("side", UNSET)
        side: ComHellopublicUserapigatewayApiRestOrderV2GatewayTradeSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = ComHellopublicUserapigatewayApiRestOrderV2GatewayTradeSide(_side)

        trade_id = d.pop("tradeId", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        com_hellopublic_userapigateway_api_rest_order_v2_gateway_trade = cls(
            instrument=instrument,
            quantity=quantity,
            price=price,
            side=side,
            trade_id=trade_id,
            timestamp=timestamp,
        )

        com_hellopublic_userapigateway_api_rest_order_v2_gateway_trade.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_v2_gateway_trade

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
