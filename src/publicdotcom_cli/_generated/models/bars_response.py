from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.last_session_close import LastSessionClose
    from ..models.market_session_bars import MarketSessionBars
    from ..models.regular_session_closing_data import RegularSessionClosingData


T = TypeVar("T", bound="BarsResponse")


@_attrs_define
class BarsResponse:
    """
    Attributes:
        symbol (str):
        period (str):
        total_expected_bars (int):
        pre_market (MarketSessionBars):
        regular_market (MarketSessionBars):
        after_market (MarketSessionBars):
        previous_close_price (None | str | Unset):
        total_gain_loss (None | str | Unset):
        total_gain_loss_percentage (None | str | Unset):
        pre_market_overnight (MarketSessionBars | Unset):
        post_market_overnight (MarketSessionBars | Unset):
        last_trading_session_close (LastSessionClose | Unset):
        regular_session_closing_data (RegularSessionClosingData | Unset):
        last_regular_trading_session_close (LastSessionClose | Unset):
    """

    symbol: str
    period: str
    total_expected_bars: int
    pre_market: MarketSessionBars
    regular_market: MarketSessionBars
    after_market: MarketSessionBars
    previous_close_price: None | str | Unset = UNSET
    total_gain_loss: None | str | Unset = UNSET
    total_gain_loss_percentage: None | str | Unset = UNSET
    pre_market_overnight: MarketSessionBars | Unset = UNSET
    post_market_overnight: MarketSessionBars | Unset = UNSET
    last_trading_session_close: LastSessionClose | Unset = UNSET
    regular_session_closing_data: RegularSessionClosingData | Unset = UNSET
    last_regular_trading_session_close: LastSessionClose | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        period = self.period

        total_expected_bars = self.total_expected_bars

        pre_market = self.pre_market.to_dict()

        regular_market = self.regular_market.to_dict()

        after_market = self.after_market.to_dict()

        previous_close_price: None | str | Unset
        if isinstance(self.previous_close_price, Unset):
            previous_close_price = UNSET
        else:
            previous_close_price = self.previous_close_price

        total_gain_loss: None | str | Unset
        if isinstance(self.total_gain_loss, Unset):
            total_gain_loss = UNSET
        else:
            total_gain_loss = self.total_gain_loss

        total_gain_loss_percentage: None | str | Unset
        if isinstance(self.total_gain_loss_percentage, Unset):
            total_gain_loss_percentage = UNSET
        else:
            total_gain_loss_percentage = self.total_gain_loss_percentage

        pre_market_overnight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pre_market_overnight, Unset):
            pre_market_overnight = self.pre_market_overnight.to_dict()

        post_market_overnight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post_market_overnight, Unset):
            post_market_overnight = self.post_market_overnight.to_dict()

        last_trading_session_close: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_trading_session_close, Unset):
            last_trading_session_close = self.last_trading_session_close.to_dict()

        regular_session_closing_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.regular_session_closing_data, Unset):
            regular_session_closing_data = self.regular_session_closing_data.to_dict()

        last_regular_trading_session_close: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_regular_trading_session_close, Unset):
            last_regular_trading_session_close = self.last_regular_trading_session_close.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "period": period,
                "totalExpectedBars": total_expected_bars,
                "preMarket": pre_market,
                "regularMarket": regular_market,
                "afterMarket": after_market,
            }
        )
        if previous_close_price is not UNSET:
            field_dict["previousClosePrice"] = previous_close_price
        if total_gain_loss is not UNSET:
            field_dict["totalGainLoss"] = total_gain_loss
        if total_gain_loss_percentage is not UNSET:
            field_dict["totalGainLossPercentage"] = total_gain_loss_percentage
        if pre_market_overnight is not UNSET:
            field_dict["preMarketOvernight"] = pre_market_overnight
        if post_market_overnight is not UNSET:
            field_dict["postMarketOvernight"] = post_market_overnight
        if last_trading_session_close is not UNSET:
            field_dict["lastTradingSessionClose"] = last_trading_session_close
        if regular_session_closing_data is not UNSET:
            field_dict["regularSessionClosingData"] = regular_session_closing_data
        if last_regular_trading_session_close is not UNSET:
            field_dict["lastRegularTradingSessionClose"] = last_regular_trading_session_close

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.last_session_close import LastSessionClose
        from ..models.market_session_bars import MarketSessionBars
        from ..models.regular_session_closing_data import RegularSessionClosingData

        d = dict(src_dict)
        symbol = d.pop("symbol")

        period = d.pop("period")

        total_expected_bars = d.pop("totalExpectedBars")

        pre_market = MarketSessionBars.from_dict(d.pop("preMarket"))

        regular_market = MarketSessionBars.from_dict(d.pop("regularMarket"))

        after_market = MarketSessionBars.from_dict(d.pop("afterMarket"))

        def _parse_previous_close_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_close_price = _parse_previous_close_price(d.pop("previousClosePrice", UNSET))

        def _parse_total_gain_loss(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_gain_loss = _parse_total_gain_loss(d.pop("totalGainLoss", UNSET))

        def _parse_total_gain_loss_percentage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_gain_loss_percentage = _parse_total_gain_loss_percentage(
            d.pop("totalGainLossPercentage", UNSET)
        )

        _pre_market_overnight = d.pop("preMarketOvernight", UNSET)
        pre_market_overnight: MarketSessionBars | Unset
        if isinstance(_pre_market_overnight, Unset):
            pre_market_overnight = UNSET
        else:
            pre_market_overnight = MarketSessionBars.from_dict(_pre_market_overnight)

        _post_market_overnight = d.pop("postMarketOvernight", UNSET)
        post_market_overnight: MarketSessionBars | Unset
        if isinstance(_post_market_overnight, Unset):
            post_market_overnight = UNSET
        else:
            post_market_overnight = MarketSessionBars.from_dict(_post_market_overnight)

        _last_trading_session_close = d.pop("lastTradingSessionClose", UNSET)
        last_trading_session_close: LastSessionClose | Unset
        if isinstance(_last_trading_session_close, Unset):
            last_trading_session_close = UNSET
        else:
            last_trading_session_close = LastSessionClose.from_dict(_last_trading_session_close)

        _regular_session_closing_data = d.pop("regularSessionClosingData", UNSET)
        regular_session_closing_data: RegularSessionClosingData | Unset
        if isinstance(_regular_session_closing_data, Unset):
            regular_session_closing_data = UNSET
        else:
            regular_session_closing_data = RegularSessionClosingData.from_dict(
                _regular_session_closing_data
            )

        _last_regular_trading_session_close = d.pop("lastRegularTradingSessionClose", UNSET)
        last_regular_trading_session_close: LastSessionClose | Unset
        if isinstance(_last_regular_trading_session_close, Unset):
            last_regular_trading_session_close = UNSET
        else:
            last_regular_trading_session_close = LastSessionClose.from_dict(
                _last_regular_trading_session_close
            )

        bars_response = cls(
            symbol=symbol,
            period=period,
            total_expected_bars=total_expected_bars,
            pre_market=pre_market,
            regular_market=regular_market,
            after_market=after_market,
            previous_close_price=previous_close_price,
            total_gain_loss=total_gain_loss,
            total_gain_loss_percentage=total_gain_loss_percentage,
            pre_market_overnight=pre_market_overnight,
            post_market_overnight=post_market_overnight,
            last_trading_session_close=last_trading_session_close,
            regular_session_closing_data=regular_session_closing_data,
            last_regular_trading_session_close=last_regular_trading_session_close,
        )

        bars_response.additional_properties = d
        return bars_response

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
