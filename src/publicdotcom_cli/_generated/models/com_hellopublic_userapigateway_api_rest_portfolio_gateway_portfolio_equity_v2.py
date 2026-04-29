from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_equity_v2_type import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2Type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2:
    """Portfolio equity summary

    Attributes:
        type_ (ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2Type): Type of asset.
        value (str): Total value for the given asset type.
        percentage_of_portfolio (None | str | Unset): The percentage of the portfolio this asset type constitutes.
                                          The percentage number is given with 2 decimals.
    """

    type_: ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2Type
    value: str
    percentage_of_portfolio: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        percentage_of_portfolio: None | str | Unset
        if isinstance(self.percentage_of_portfolio, Unset):
            percentage_of_portfolio = UNSET
        else:
            percentage_of_portfolio = self.percentage_of_portfolio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )
        if percentage_of_portfolio is not UNSET:
            field_dict["percentageOfPortfolio"] = percentage_of_portfolio

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2Type(
            d.pop("type")
        )

        value = d.pop("value")

        def _parse_percentage_of_portfolio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_portfolio = _parse_percentage_of_portfolio(
            d.pop("percentageOfPortfolio", UNSET)
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_equity_v2 = cls(
            type_=type_,
            value=value,
            percentage_of_portfolio=percentage_of_portfolio,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_equity_v2.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_equity_v2

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
