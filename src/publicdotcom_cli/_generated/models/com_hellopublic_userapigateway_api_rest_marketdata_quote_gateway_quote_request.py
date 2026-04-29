from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteRequest")


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteRequest:
    """
    Attributes:
        instruments (list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument]): List of instruments to query
            quotes.
    """

    instruments: list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instruments = []
        for instruments_item_data in self.instruments:
            instruments_item = instruments_item_data.to_dict()
            instruments.append(instruments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instruments": instruments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )

        d = dict(src_dict)
        instruments = []
        _instruments = d.pop("instruments")
        for instruments_item_data in _instruments:
            instruments_item = (
                ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
                    instruments_item_data
                )
            )

            instruments.append(instruments_item)

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote_request = cls(
            instruments=instruments,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote_request.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote_request

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
