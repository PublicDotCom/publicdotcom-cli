from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_options_option_greeks import (
        ComHellopublicUserapigatewayApiRestOptionsOptionGreeks,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteOptionDetails")


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteOptionDetails:
    """Option-specific details including Greeks, strike price, and mid price.

    Attributes:
        strike_price (str): The strike price for the option contract.
        greeks (ComHellopublicUserapigatewayApiRestOptionsOptionGreeks | Unset):
        mid_price (None | str | Unset): The mid price (average of bid and ask) for the option contract.
            Null if bid/ask data is not available.
    """

    strike_price: str
    greeks: ComHellopublicUserapigatewayApiRestOptionsOptionGreeks | Unset = UNSET
    mid_price: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strike_price = self.strike_price

        greeks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.greeks, Unset):
            greeks = self.greeks.to_dict()

        mid_price: None | str | Unset
        if isinstance(self.mid_price, Unset):
            mid_price = UNSET
        else:
            mid_price = self.mid_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strikePrice": strike_price,
            }
        )
        if greeks is not UNSET:
            field_dict["greeks"] = greeks
        if mid_price is not UNSET:
            field_dict["midPrice"] = mid_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_options_option_greeks import (
            ComHellopublicUserapigatewayApiRestOptionsOptionGreeks,
        )

        d = dict(src_dict)
        strike_price = d.pop("strikePrice")

        _greeks = d.pop("greeks", UNSET)
        greeks: ComHellopublicUserapigatewayApiRestOptionsOptionGreeks | Unset
        if isinstance(_greeks, Unset):
            greeks = UNSET
        else:
            greeks = ComHellopublicUserapigatewayApiRestOptionsOptionGreeks.from_dict(_greeks)

        def _parse_mid_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mid_price = _parse_mid_price(d.pop("midPrice", UNSET))

        com_hellopublic_userapigateway_api_rest_marketdata_quote_option_details = cls(
            strike_price=strike_price,
            greeks=greeks,
            mid_price=mid_price,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_option_details.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_quote_option_details

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
