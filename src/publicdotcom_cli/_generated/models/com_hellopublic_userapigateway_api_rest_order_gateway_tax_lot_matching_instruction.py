from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderGatewayTaxLotMatchingInstruction")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderGatewayTaxLotMatchingInstruction:
    """Tax lot matching instruction for an order.

    Tax lot matching instructions must follow these rules:
    - There can only be at most 8 tax lot matching instructions per request. If the list of tax lot instructions is
    present (non-null), it must have at least one and at most eight elements.
    - Tax lot instructions can only be specified for orders to SELL equity with open/close indicator CLOSE.
    - The tax lot instructions must be for the same symbol as this order sells.
    - Tax lot instructions can only be specified for MARKET orders or good for the day LIMIT orders.
    - The total quantity of the tax lot instructions must sum to the quantity of this order.
    - Tax lot instructions can only be specified if the tax lot information has been updated today.

    There is no guarantee that the tax lot instructions are applied exactly as specified.

        Attributes:
            tax_lot_id (str): The tax lot id in the format: symbol;tradeDate;price;quantity (e.g.,
                "AAPL;2024-01-15;150.00;10")
            quantity (str): The quantity of the equity. Must be greater than 0 and not exceed the quantity of the tax lot.
    """

    tax_lot_id: str
    quantity: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tax_lot_id = self.tax_lot_id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxLotId": tax_lot_id,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tax_lot_id = d.pop("taxLotId")

        quantity = d.pop("quantity")

        com_hellopublic_userapigateway_api_rest_order_gateway_tax_lot_matching_instruction = cls(
            tax_lot_id=tax_lot_id,
            quantity=quantity,
        )

        com_hellopublic_userapigateway_api_rest_order_gateway_tax_lot_matching_instruction.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_gateway_tax_lot_matching_instruction

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
