from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote import (
        ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote,
    )


T = TypeVar(
    "T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse"
)


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainResponse:
    """
    Attributes:
        base_symbol (str): The base symbol for which the option chain belongs.
        calls (list[ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote]): List of call quotes for the given
            option chain.
        puts (list[ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote]): List of put quotes for the given
            option chain.
    """

    base_symbol: str
    calls: list[ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote]
    puts: list[ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_symbol = self.base_symbol

        calls = []
        for calls_item_data in self.calls:
            calls_item = calls_item_data.to_dict()
            calls.append(calls_item)

        puts = []
        for puts_item_data in self.puts:
            puts_item = puts_item_data.to_dict()
            puts.append(puts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseSymbol": base_symbol,
                "calls": calls,
                "puts": puts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote import (
            ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote,
        )

        d = dict(src_dict)
        base_symbol = d.pop("baseSymbol")

        calls = []
        _calls = d.pop("calls")
        for calls_item_data in _calls:
            calls_item = ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote.from_dict(
                calls_item_data
            )

            calls.append(calls_item)

        puts = []
        _puts = d.pop("puts")
        for puts_item_data in _puts:
            puts_item = ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote.from_dict(
                puts_item_data
            )

            puts.append(puts_item)

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_chain_response = (
            cls(
                base_symbol=base_symbol,
                calls=calls,
                puts=puts,
            )
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_chain_response.additional_properties = d
        return (
            com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_chain_response
        )

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
