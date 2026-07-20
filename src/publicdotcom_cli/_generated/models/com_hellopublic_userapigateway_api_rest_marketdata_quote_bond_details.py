from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteBondDetails")


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteBondDetails:
    """Bond-specific details for a quote.

    Attributes:
        ask_min_size (str | Unset): Minimum trade size for asks in par value
        bid_min_size (str | Unset): Minimum trade size for bids in par value
        ask_markup (str | Unset): Ask markup percentage
        bid_markup (str | Unset): Bid markup percentage
        suggested_buy_price (str | Unset): Suggested buy price for this bond
        suggested_sell_price (str | Unset): Suggested sell price for this bond
        min_buy_amount (str | Unset): Minimum buy amount in dollars
        min_buy_increment_amount (str | Unset): Minimum buy increment amount in dollars
    """

    ask_min_size: str | Unset = UNSET
    bid_min_size: str | Unset = UNSET
    ask_markup: str | Unset = UNSET
    bid_markup: str | Unset = UNSET
    suggested_buy_price: str | Unset = UNSET
    suggested_sell_price: str | Unset = UNSET
    min_buy_amount: str | Unset = UNSET
    min_buy_increment_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ask_min_size = self.ask_min_size

        bid_min_size = self.bid_min_size

        ask_markup = self.ask_markup

        bid_markup = self.bid_markup

        suggested_buy_price = self.suggested_buy_price

        suggested_sell_price = self.suggested_sell_price

        min_buy_amount = self.min_buy_amount

        min_buy_increment_amount = self.min_buy_increment_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ask_min_size is not UNSET:
            field_dict["askMinSize"] = ask_min_size
        if bid_min_size is not UNSET:
            field_dict["bidMinSize"] = bid_min_size
        if ask_markup is not UNSET:
            field_dict["askMarkup"] = ask_markup
        if bid_markup is not UNSET:
            field_dict["bidMarkup"] = bid_markup
        if suggested_buy_price is not UNSET:
            field_dict["suggestedBuyPrice"] = suggested_buy_price
        if suggested_sell_price is not UNSET:
            field_dict["suggestedSellPrice"] = suggested_sell_price
        if min_buy_amount is not UNSET:
            field_dict["minBuyAmount"] = min_buy_amount
        if min_buy_increment_amount is not UNSET:
            field_dict["minBuyIncrementAmount"] = min_buy_increment_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ask_min_size = d.pop("askMinSize", UNSET)

        bid_min_size = d.pop("bidMinSize", UNSET)

        ask_markup = d.pop("askMarkup", UNSET)

        bid_markup = d.pop("bidMarkup", UNSET)

        suggested_buy_price = d.pop("suggestedBuyPrice", UNSET)

        suggested_sell_price = d.pop("suggestedSellPrice", UNSET)

        min_buy_amount = d.pop("minBuyAmount", UNSET)

        min_buy_increment_amount = d.pop("minBuyIncrementAmount", UNSET)

        com_hellopublic_userapigateway_api_rest_marketdata_quote_bond_details = cls(
            ask_min_size=ask_min_size,
            bid_min_size=bid_min_size,
            ask_markup=ask_markup,
            bid_markup=bid_markup,
            suggested_buy_price=suggested_buy_price,
            suggested_sell_price=suggested_sell_price,
            min_buy_amount=min_buy_amount,
            min_buy_increment_amount=min_buy_increment_amount,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_bond_details.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_quote_bond_details

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
