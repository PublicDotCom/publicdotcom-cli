from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_account_v2_account_type import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2AccountType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrder,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_buying_power import (
        ComHellopublicUserapigatewayApiRestPortfolioGatewayBuyingPower,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_equity_v2 import (
        ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_position import (
        ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioPosition,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy import (
        ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2:
    """Portfolio for the account

    Attributes:
        account_id (str): Id of the account
        account_type (ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2AccountType): Type of the
            account
        buying_power (ComHellopublicUserapigatewayApiRestPortfolioGatewayBuyingPower):
        equity (list[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2]): List of equity summaries
        positions (list[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioPosition]): List of positions
        orders (list[ComHellopublicUserapigatewayApiRestOrderGatewayOrder]):
        strategies (list[ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy] | None | Unset): List of multi-leg
            option strategies. Null if backend doesn't support strategies.
    """

    account_id: str
    account_type: ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2AccountType
    buying_power: ComHellopublicUserapigatewayApiRestPortfolioGatewayBuyingPower
    equity: list[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2]
    positions: list[ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioPosition]
    orders: list[ComHellopublicUserapigatewayApiRestOrderGatewayOrder]
    strategies: list[ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy] | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        account_type = self.account_type.value

        buying_power = self.buying_power.to_dict()

        equity = []
        for equity_item_data in self.equity:
            equity_item = equity_item_data.to_dict()
            equity.append(equity_item)

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()
            orders.append(orders_item)

        strategies: list[dict[str, Any]] | None | Unset
        if isinstance(self.strategies, Unset):
            strategies = UNSET
        elif isinstance(self.strategies, list):
            strategies = []
            for strategies_type_0_item_data in self.strategies:
                strategies_type_0_item = strategies_type_0_item_data.to_dict()
                strategies.append(strategies_type_0_item)

        else:
            strategies = self.strategies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "accountType": account_type,
                "buyingPower": buying_power,
                "equity": equity,
                "positions": positions,
                "orders": orders,
            }
        )
        if strategies is not UNSET:
            field_dict["strategies"] = strategies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrder,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_buying_power import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayBuyingPower,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_equity_v2 import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_position import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioPosition,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_strategy import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy,
        )

        d = dict(src_dict)
        account_id = d.pop("accountId")

        account_type = (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2AccountType(
                d.pop("accountType")
            )
        )

        buying_power = ComHellopublicUserapigatewayApiRestPortfolioGatewayBuyingPower.from_dict(
            d.pop("buyingPower")
        )

        equity = []
        _equity = d.pop("equity")
        for equity_item_data in _equity:
            equity_item = (
                ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2.from_dict(
                    equity_item_data
                )
            )

            equity.append(equity_item)

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = (
                ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioPosition.from_dict(
                    positions_item_data
                )
            )

            positions.append(positions_item)

        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = ComHellopublicUserapigatewayApiRestOrderGatewayOrder.from_dict(
                orders_item_data
            )

            orders.append(orders_item)

        def _parse_strategies(
            data: object,
        ) -> list[ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                strategies_type_0 = []
                _strategies_type_0 = data
                for strategies_type_0_item_data in _strategies_type_0:
                    strategies_type_0_item = (
                        ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy.from_dict(
                            strategies_type_0_item_data
                        )
                    )

                    strategies_type_0.append(strategies_type_0_item)

                return strategies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[ComHellopublicUserapigatewayApiRestPortfolioGatewayStrategy] | None | Unset,
                data,
            )

        strategies = _parse_strategies(d.pop("strategies", UNSET))

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_account_v2 = cls(
            account_id=account_id,
            account_type=account_type,
            buying_power=buying_power,
            equity=equity,
            positions=positions,
            orders=orders,
            strategies=strategies,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_account_v2.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_account_v2

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
