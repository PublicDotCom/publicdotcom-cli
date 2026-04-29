from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote import (
        ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteResponse:
    """
    Attributes:
        quotes (list[ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote] | Unset): List of quotes
    """

    quotes: list[ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotes, Unset):
            quotes = []
            for quotes_item_data in self.quotes:
                quotes_item = quotes_item_data.to_dict()
                quotes.append(quotes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quotes is not UNSET:
            field_dict["quotes"] = quotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote import (
            ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote,
        )

        d = dict(src_dict)
        _quotes = d.pop("quotes", UNSET)
        quotes: list[ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote] | Unset = UNSET
        if _quotes is not UNSET:
            quotes = []
            for quotes_item_data in _quotes:
                quotes_item = (
                    ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote.from_dict(
                        quotes_item_data
                    )
                )

                quotes.append(quotes_item)

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote_response = cls(
            quotes=quotes,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote_response

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
