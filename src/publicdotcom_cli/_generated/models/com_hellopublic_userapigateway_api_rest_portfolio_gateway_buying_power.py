from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayBuyingPower")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayBuyingPower:
    """
    Attributes:
        cash_only_buying_power (str): Buying power available for trading on cash only without taking loans.
        buying_power (str): Buying power available for trading marginable assets.
        options_buying_power (str): Buying power available for trading options.
    """

    cash_only_buying_power: str
    buying_power: str
    options_buying_power: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cash_only_buying_power = self.cash_only_buying_power

        buying_power = self.buying_power

        options_buying_power = self.options_buying_power

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cashOnlyBuyingPower": cash_only_buying_power,
                "buyingPower": buying_power,
                "optionsBuyingPower": options_buying_power,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cash_only_buying_power = d.pop("cashOnlyBuyingPower")

        buying_power = d.pop("buyingPower")

        options_buying_power = d.pop("optionsBuyingPower")

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_buying_power = cls(
            cash_only_buying_power=cash_only_buying_power,
            buying_power=buying_power,
            options_buying_power=options_buying_power,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_buying_power.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gateway_buying_power

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
