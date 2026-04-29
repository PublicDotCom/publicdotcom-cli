from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gain_type_0 import (
        ComHellopublicUserapigatewayApiRestPortfolioGainType0,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis_type_0 import (
        ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy_leg import (
        ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategyLeg,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_price_type_0 import (
        ComHellopublicUserapigatewayApiRestPortfolioPriceType0,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy:
    """Represents a multi-leg option strategy in the portfolio

    Attributes:
        strategy_id (str): Unique identifier for the strategy
        display_name (str): Display name for the strategy (e.g., "$180/$185 Call Spread")
        quantity (str): Quantity of the strategy
        option_legs (list[ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategyLeg]): List of option legs that
            make up this strategy
        current_value (str | Unset): Current value of the strategy
        percent_of_portfolio (str | Unset): Percentage of the total portfolio this strategy represents
        last_price (ComHellopublicUserapigatewayApiRestPortfolioPriceType0 | None | Unset):
        position_daily_gain (ComHellopublicUserapigatewayApiRestPortfolioGainType0 | None | Unset):
        cost_basis (ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0 | None | Unset): Cost basis of a
            position. What the member paid for entering the position. The cost basis is
             based on tax lots and will factor in wash sales.
    """

    strategy_id: str
    display_name: str
    quantity: str
    option_legs: list[ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategyLeg]
    current_value: str | Unset = UNSET
    percent_of_portfolio: str | Unset = UNSET
    last_price: ComHellopublicUserapigatewayApiRestPortfolioPriceType0 | None | Unset = UNSET
    position_daily_gain: ComHellopublicUserapigatewayApiRestPortfolioGainType0 | None | Unset = (
        UNSET
    )
    cost_basis: ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gain_type_0 import (
            ComHellopublicUserapigatewayApiRestPortfolioGainType0,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis_type_0 import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_price_type_0 import (
            ComHellopublicUserapigatewayApiRestPortfolioPriceType0,
        )

        strategy_id = self.strategy_id

        display_name = self.display_name

        quantity = self.quantity

        option_legs = []
        for option_legs_item_data in self.option_legs:
            option_legs_item = option_legs_item_data.to_dict()
            option_legs.append(option_legs_item)

        current_value = self.current_value

        percent_of_portfolio = self.percent_of_portfolio

        last_price: dict[str, Any] | None | Unset
        if isinstance(self.last_price, Unset):
            last_price = UNSET
        elif isinstance(self.last_price, ComHellopublicUserapigatewayApiRestPortfolioPriceType0):
            last_price = self.last_price.to_dict()
        else:
            last_price = self.last_price

        position_daily_gain: dict[str, Any] | None | Unset
        if isinstance(self.position_daily_gain, Unset):
            position_daily_gain = UNSET
        elif isinstance(
            self.position_daily_gain, ComHellopublicUserapigatewayApiRestPortfolioGainType0
        ):
            position_daily_gain = self.position_daily_gain.to_dict()
        else:
            position_daily_gain = self.position_daily_gain

        cost_basis: dict[str, Any] | None | Unset
        if isinstance(self.cost_basis, Unset):
            cost_basis = UNSET
        elif isinstance(
            self.cost_basis, ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0
        ):
            cost_basis = self.cost_basis.to_dict()
        else:
            cost_basis = self.cost_basis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyId": strategy_id,
                "displayName": display_name,
                "quantity": quantity,
                "optionLegs": option_legs,
            }
        )
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if percent_of_portfolio is not UNSET:
            field_dict["percentOfPortfolio"] = percent_of_portfolio
        if last_price is not UNSET:
            field_dict["lastPrice"] = last_price
        if position_daily_gain is not UNSET:
            field_dict["positionDailyGain"] = position_daily_gain
        if cost_basis is not UNSET:
            field_dict["costBasis"] = cost_basis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gain_type_0 import (
            ComHellopublicUserapigatewayApiRestPortfolioGainType0,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis_type_0 import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy_leg import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategyLeg,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_price_type_0 import (
            ComHellopublicUserapigatewayApiRestPortfolioPriceType0,
        )

        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        display_name = d.pop("displayName")

        quantity = d.pop("quantity")

        option_legs = []
        _option_legs = d.pop("optionLegs")
        for option_legs_item_data in _option_legs:
            option_legs_item = (
                ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategyLeg.from_dict(
                    option_legs_item_data
                )
            )

            option_legs.append(option_legs_item)

        current_value = d.pop("currentValue", UNSET)

        percent_of_portfolio = d.pop("percentOfPortfolio", UNSET)

        def _parse_last_price(
            data: object,
        ) -> ComHellopublicUserapigatewayApiRestPortfolioPriceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascom_hellopublic_userapigateway_api_rest_portfolio_price_type_0 = (
                    ComHellopublicUserapigatewayApiRestPortfolioPriceType0.from_dict(data)
                )

                return (
                    componentsschemascom_hellopublic_userapigateway_api_rest_portfolio_price_type_0
                )
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ComHellopublicUserapigatewayApiRestPortfolioPriceType0 | None | Unset, data)

        last_price = _parse_last_price(d.pop("lastPrice", UNSET))

        def _parse_position_daily_gain(
            data: object,
        ) -> ComHellopublicUserapigatewayApiRestPortfolioGainType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascom_hellopublic_userapigateway_api_rest_portfolio_gain_type_0 = (
                    ComHellopublicUserapigatewayApiRestPortfolioGainType0.from_dict(data)
                )

                return (
                    componentsschemascom_hellopublic_userapigateway_api_rest_portfolio_gain_type_0
                )
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ComHellopublicUserapigatewayApiRestPortfolioGainType0 | None | Unset, data)

        position_daily_gain = _parse_position_daily_gain(d.pop("positionDailyGain", UNSET))

        def _parse_cost_basis(
            data: object,
        ) -> ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascom_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis_type_0 = ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0.from_dict(
                    data
                )

                return componentsschemascom_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasisType0 | None | Unset,
                data,
            )

        cost_basis = _parse_cost_basis(d.pop("costBasis", UNSET))

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy = cls(
            strategy_id=strategy_id,
            display_name=display_name,
            quantity=quantity,
            option_legs=option_legs,
            current_value=current_value,
            percent_of_portfolio=percent_of_portfolio,
            last_price=last_price,
            position_daily_gain=position_daily_gain,
            cost_basis=cost_basis,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy

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
