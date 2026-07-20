from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gain import (
        ComHellopublicUserapigatewayApiRestPortfolioGain,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis import (
        ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasis,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_instrument import (
        ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrument,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_portfolio_price import (
        ComHellopublicUserapigatewayApiRestPortfolioPrice,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioPosition")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioPosition:
    """Position in portfolio

    Attributes:
        instrument (ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrument):
        quantity (str): The quantity of the position.
        strategy_ids (list[str]): List of strategy IDs this position is part of. Empty list for single-leg positions not
            part of any strategy.
        opened_at (datetime.datetime | None | Unset): When was this position opened. Null if unknown.
        current_value (None | str | Unset): How much the position is worth. Calculated from quantity * lastSalePrice.
        percent_of_portfolio (None | str | Unset): The percent that this position makes of the entire portfolio.
        last_price (ComHellopublicUserapigatewayApiRestPortfolioPrice | Unset):
        instrument_gain (ComHellopublicUserapigatewayApiRestPortfolioGain | Unset):
        position_daily_gain (ComHellopublicUserapigatewayApiRestPortfolioGain | Unset):
        cost_basis (ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasis | Unset): Cost basis of a position.
            What the member paid for entering the position. The cost basis is
             based on tax lots and will factor in wash sales.
    """

    instrument: ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrument
    quantity: str
    strategy_ids: list[str]
    opened_at: datetime.datetime | None | Unset = UNSET
    current_value: None | str | Unset = UNSET
    percent_of_portfolio: None | str | Unset = UNSET
    last_price: ComHellopublicUserapigatewayApiRestPortfolioPrice | Unset = UNSET
    instrument_gain: ComHellopublicUserapigatewayApiRestPortfolioGain | Unset = UNSET
    position_daily_gain: ComHellopublicUserapigatewayApiRestPortfolioGain | Unset = UNSET
    cost_basis: ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasis | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument.to_dict()

        quantity = self.quantity

        strategy_ids = self.strategy_ids

        opened_at: None | str | Unset
        if isinstance(self.opened_at, Unset):
            opened_at = UNSET
        elif isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        current_value: None | str | Unset
        if isinstance(self.current_value, Unset):
            current_value = UNSET
        else:
            current_value = self.current_value

        percent_of_portfolio: None | str | Unset
        if isinstance(self.percent_of_portfolio, Unset):
            percent_of_portfolio = UNSET
        else:
            percent_of_portfolio = self.percent_of_portfolio

        last_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_price, Unset):
            last_price = self.last_price.to_dict()

        instrument_gain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instrument_gain, Unset):
            instrument_gain = self.instrument_gain.to_dict()

        position_daily_gain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position_daily_gain, Unset):
            position_daily_gain = self.position_daily_gain.to_dict()

        cost_basis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost_basis, Unset):
            cost_basis = self.cost_basis.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "quantity": quantity,
                "strategyIds": strategy_ids,
            }
        )
        if opened_at is not UNSET:
            field_dict["openedAt"] = opened_at
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if percent_of_portfolio is not UNSET:
            field_dict["percentOfPortfolio"] = percent_of_portfolio
        if last_price is not UNSET:
            field_dict["lastPrice"] = last_price
        if instrument_gain is not UNSET:
            field_dict["instrumentGain"] = instrument_gain
        if position_daily_gain is not UNSET:
            field_dict["positionDailyGain"] = position_daily_gain
        if cost_basis is not UNSET:
            field_dict["costBasis"] = cost_basis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gain import (
            ComHellopublicUserapigatewayApiRestPortfolioGain,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasis,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_instrument import (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrument,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_portfolio_price import (
            ComHellopublicUserapigatewayApiRestPortfolioPrice,
        )

        d = dict(src_dict)
        instrument = (
            ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrument.from_dict(
                d.pop("instrument")
            )
        )

        quantity = d.pop("quantity")

        strategy_ids = cast(list[str], d.pop("strategyIds"))

        def _parse_opened_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)

                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        opened_at = _parse_opened_at(d.pop("openedAt", UNSET))

        def _parse_current_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_value = _parse_current_value(d.pop("currentValue", UNSET))

        def _parse_percent_of_portfolio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percent_of_portfolio = _parse_percent_of_portfolio(d.pop("percentOfPortfolio", UNSET))

        _last_price = d.pop("lastPrice", UNSET)
        last_price: ComHellopublicUserapigatewayApiRestPortfolioPrice | Unset
        if isinstance(_last_price, Unset):
            last_price = UNSET
        else:
            last_price = ComHellopublicUserapigatewayApiRestPortfolioPrice.from_dict(_last_price)

        _instrument_gain = d.pop("instrumentGain", UNSET)
        instrument_gain: ComHellopublicUserapigatewayApiRestPortfolioGain | Unset
        if isinstance(_instrument_gain, Unset):
            instrument_gain = UNSET
        else:
            instrument_gain = ComHellopublicUserapigatewayApiRestPortfolioGain.from_dict(
                _instrument_gain
            )

        _position_daily_gain = d.pop("positionDailyGain", UNSET)
        position_daily_gain: ComHellopublicUserapigatewayApiRestPortfolioGain | Unset
        if isinstance(_position_daily_gain, Unset):
            position_daily_gain = UNSET
        else:
            position_daily_gain = ComHellopublicUserapigatewayApiRestPortfolioGain.from_dict(
                _position_daily_gain
            )

        _cost_basis = d.pop("costBasis", UNSET)
        cost_basis: ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasis | Unset
        if isinstance(_cost_basis, Unset):
            cost_basis = UNSET
        else:
            cost_basis = ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasis.from_dict(
                _cost_basis
            )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_position = cls(
            instrument=instrument,
            quantity=quantity,
            strategy_ids=strategy_ids,
            opened_at=opened_at,
            current_value=current_value,
            percent_of_portfolio=percent_of_portfolio,
            last_price=last_price,
            instrument_gain=instrument_gain,
            position_daily_gain=position_daily_gain,
            cost_basis=cost_basis,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_position.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gateway_portfolio_position

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
