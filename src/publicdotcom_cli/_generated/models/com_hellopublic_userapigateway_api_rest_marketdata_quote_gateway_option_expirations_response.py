from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse"
)


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionExpirationsResponse:
    """
    Attributes:
        base_symbol (str): The base symbol for which the option expirations belong.
        expirations (list[datetime.date]): List of option expirations for the given symbol.
    """

    base_symbol: str
    expirations: list[datetime.date]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_symbol = self.base_symbol

        expirations = []
        for expirations_item_data in self.expirations:
            expirations_item = expirations_item_data.isoformat()
            expirations.append(expirations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseSymbol": base_symbol,
                "expirations": expirations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_symbol = d.pop("baseSymbol")

        expirations = []
        _expirations = d.pop("expirations")
        for expirations_item_data in _expirations:
            expirations_item = datetime.date.fromisoformat(expirations_item_data)

            expirations.append(expirations_item)

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_expirations_response = cls(
            base_symbol=base_symbol,
            expirations=expirations,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_expirations_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_expirations_response

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
