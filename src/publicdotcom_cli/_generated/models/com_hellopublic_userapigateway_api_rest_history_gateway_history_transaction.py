from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction_direction import (
    ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionDirection,
)
from ..models.com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction_security_type import (
    ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSecurityType,
)
from ..models.com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction_side import (
    ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSide,
)
from ..models.com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction_sub_type import (
    ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSubType,
)
from ..models.com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction_type import (
    ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransaction")


@_attrs_define
class ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransaction:
    """Represents a transaction in the history of an account

    Attributes:
        timestamp (datetime.datetime | Unset): The timestamp when the transaction happened
        id (str | Unset): The id of the transaction
        type_ (ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionType | Unset): The type of the
            transaction
        sub_type (ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSubType | Unset): The subtype of
            the transaction
        account_number (str | Unset): The account the transaction happened on
        symbol (str | Unset): The symbol of the transaction
        security_type (ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSecurityType | Unset): The
            security type of the transaction
        side (ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSide | Unset): The side of the
            transaction - relevant for trades
        description (str | Unset): The description of the transaction
        net_amount (str | Unset): The net amount of the transaction
        principal_amount (str | Unset): The principal amount of the transaction
        quantity (str | Unset): The quantity of the transaction
        direction (ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionDirection | Unset): The direction
            of the transaction
        fees (str | Unset): The fees of the transaction
    """

    timestamp: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    type_: ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionType | Unset = UNSET
    sub_type: ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSubType | Unset = (
        UNSET
    )
    account_number: str | Unset = UNSET
    symbol: str | Unset = UNSET
    security_type: (
        ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSecurityType | Unset
    ) = UNSET
    side: ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSide | Unset = UNSET
    description: str | Unset = UNSET
    net_amount: str | Unset = UNSET
    principal_amount: str | Unset = UNSET
    quantity: str | Unset = UNSET
    direction: (
        ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionDirection | Unset
    ) = UNSET
    fees: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        sub_type: str | Unset = UNSET
        if not isinstance(self.sub_type, Unset):
            sub_type = self.sub_type.value

        account_number = self.account_number

        symbol = self.symbol

        security_type: str | Unset = UNSET
        if not isinstance(self.security_type, Unset):
            security_type = self.security_type.value

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        description = self.description

        net_amount = self.net_amount

        principal_amount = self.principal_amount

        quantity = self.quantity

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        fees = self.fees

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if security_type is not UNSET:
            field_dict["securityType"] = security_type
        if side is not UNSET:
            field_dict["side"] = side
        if description is not UNSET:
            field_dict["description"] = description
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount
        if principal_amount is not UNSET:
            field_dict["principalAmount"] = principal_amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if direction is not UNSET:
            field_dict["direction"] = direction
        if fees is not UNSET:
            field_dict["fees"] = fees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionType(_type_)

        _sub_type = d.pop("subType", UNSET)
        sub_type: ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSubType | Unset
        if isinstance(_sub_type, Unset):
            sub_type = UNSET
        else:
            sub_type = ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSubType(
                _sub_type
            )

        account_number = d.pop("accountNumber", UNSET)

        symbol = d.pop("symbol", UNSET)

        _security_type = d.pop("securityType", UNSET)
        security_type: (
            ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSecurityType | Unset
        )
        if isinstance(_security_type, Unset):
            security_type = UNSET
        else:
            security_type = (
                ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSecurityType(
                    _security_type
                )
            )

        _side = d.pop("side", UNSET)
        side: ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSide(_side)

        description = d.pop("description", UNSET)

        net_amount = d.pop("netAmount", UNSET)

        principal_amount = d.pop("principalAmount", UNSET)

        quantity = d.pop("quantity", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: (
            ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionDirection | Unset
        )
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = (
                ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionDirection(
                    _direction
                )
            )

        fees = d.pop("fees", UNSET)

        com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction = cls(
            timestamp=timestamp,
            id=id,
            type_=type_,
            sub_type=sub_type,
            account_number=account_number,
            symbol=symbol,
            security_type=security_type,
            side=side,
            description=description,
            net_amount=net_amount,
            principal_amount=principal_amount,
            quantity=quantity,
            direction=direction,
            fees=fees,
        )

        com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction

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
