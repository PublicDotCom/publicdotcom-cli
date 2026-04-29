from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategyLeg")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategyLeg:
    """Represents a single leg of an option strategy

    Attributes:
        symbol (str): The symbol of the leg
        position_type (str): The position type (LONG or SHORT)
        ratio_quantity (str): The ratio quantity of this leg in the strategy
    """

    symbol: str
    position_type: str
    ratio_quantity: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        position_type = self.position_type

        ratio_quantity = self.ratio_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "positionType": position_type,
                "ratioQuantity": ratio_quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        position_type = d.pop("positionType")

        ratio_quantity = d.pop("ratioQuantity")

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy_leg = cls(
            symbol=symbol,
            position_type=position_type,
            ratio_quantity=ratio_quantity,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy_leg.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy_leg

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
