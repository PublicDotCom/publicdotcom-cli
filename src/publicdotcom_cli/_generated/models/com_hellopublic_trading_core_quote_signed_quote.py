from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_trading_core_quote_signed_quote_uptick_rule import (
    ComHellopublicTradingCoreQuoteSignedQuoteUptickRule,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_trading_core_quote_bond_quote_detail import (
        ComHellopublicTradingCoreQuoteBondQuoteDetail,
    )


T = TypeVar("T", bound="ComHellopublicTradingCoreQuoteSignedQuote")


@_attrs_define
class ComHellopublicTradingCoreQuoteSignedQuote:
    """The original version did not allow null values for bid/ask data. This was relaxed later to allow equity to use
    super-quotes

        Attributes:
            symbol (str): The symbol identifying the instrument.
            timestamp (datetime.datetime): The timestamp were the server returned this message. This is not the timestamp of
                the bid/ask or the last trade
            signature (str): A hash of the properties, to make sure the app does not change any of the data when posting
                back the quote during order creation.
            last (str | Unset): The last trade for this instrument. May be <code>null</code> if the quote is for a symbol on
                the IPO date and the order type is LIMIT.
            bid (str | Unset): The last bid price for this instrument.
            bid_size (str | Unset): The number of units available at the given bid price.
            ask (str | Unset): The last ask price for this instrument.
            ask_size (str | Unset): The number of units available at the given ask price.
            collar_percentage (str | Unset): the collar percentage, used to calculate the markup/markdown for bid/ask which
                the app should use when placing extended hours limit orders
            buy_collar (str | Unset): Price used to buy with collar. This is collarPercentage higher than the current bid,
                to ensure that the order will execute unless the market moves more than collarPercentage up
            sell_collar (str | Unset): Price used to sell with collar. This is collarPercentage lower than the current ask,
                to ensure that the order will execute unless the market moves more than collarPercentage down
            open_interest (int | Unset): The total number of options contracts that are not closed or delivered on a
                particular day.
                 This will be null for non option quotes
            bid_collar (str | Unset):
            ask_collar (str | Unset):
            detail (ComHellopublicTradingCoreQuoteBondQuoteDetail | Unset):
            trading_halted (bool | Unset): Indicates if trading is currently halted on the symbol
            uptick_rule (ComHellopublicTradingCoreQuoteSignedQuoteUptickRule | Unset): The Uptick Rule is triggered for
                equities when the price today or yesterday has dropped at least 10 percent since previous days' closing price.
                The property is null when the rule is not applicable (for other security types than equity) or when it cannot be
                determined.
    """

    symbol: str
    timestamp: datetime.datetime
    signature: str
    last: str | Unset = UNSET
    bid: str | Unset = UNSET
    bid_size: str | Unset = UNSET
    ask: str | Unset = UNSET
    ask_size: str | Unset = UNSET
    collar_percentage: str | Unset = UNSET
    buy_collar: str | Unset = UNSET
    sell_collar: str | Unset = UNSET
    open_interest: int | Unset = UNSET
    bid_collar: str | Unset = UNSET
    ask_collar: str | Unset = UNSET
    detail: ComHellopublicTradingCoreQuoteBondQuoteDetail | Unset = UNSET
    trading_halted: bool | Unset = UNSET
    uptick_rule: ComHellopublicTradingCoreQuoteSignedQuoteUptickRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        timestamp = self.timestamp.isoformat()

        signature = self.signature

        last = self.last

        bid = self.bid

        bid_size = self.bid_size

        ask = self.ask

        ask_size = self.ask_size

        collar_percentage = self.collar_percentage

        buy_collar = self.buy_collar

        sell_collar = self.sell_collar

        open_interest = self.open_interest

        bid_collar = self.bid_collar

        ask_collar = self.ask_collar

        detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        trading_halted = self.trading_halted

        uptick_rule: str | Unset = UNSET
        if not isinstance(self.uptick_rule, Unset):
            uptick_rule = self.uptick_rule.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "timestamp": timestamp,
                "signature": signature,
            }
        )
        if last is not UNSET:
            field_dict["last"] = last
        if bid is not UNSET:
            field_dict["bid"] = bid
        if bid_size is not UNSET:
            field_dict["bidSize"] = bid_size
        if ask is not UNSET:
            field_dict["ask"] = ask
        if ask_size is not UNSET:
            field_dict["askSize"] = ask_size
        if collar_percentage is not UNSET:
            field_dict["collarPercentage"] = collar_percentage
        if buy_collar is not UNSET:
            field_dict["buyCollar"] = buy_collar
        if sell_collar is not UNSET:
            field_dict["sellCollar"] = sell_collar
        if open_interest is not UNSET:
            field_dict["openInterest"] = open_interest
        if bid_collar is not UNSET:
            field_dict["bidCollar"] = bid_collar
        if ask_collar is not UNSET:
            field_dict["askCollar"] = ask_collar
        if detail is not UNSET:
            field_dict["detail"] = detail
        if trading_halted is not UNSET:
            field_dict["tradingHalted"] = trading_halted
        if uptick_rule is not UNSET:
            field_dict["uptickRule"] = uptick_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_trading_core_quote_bond_quote_detail import (
            ComHellopublicTradingCoreQuoteBondQuoteDetail,
        )

        d = dict(src_dict)
        symbol = d.pop("symbol")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        signature = d.pop("signature")

        last = d.pop("last", UNSET)

        bid = d.pop("bid", UNSET)

        bid_size = d.pop("bidSize", UNSET)

        ask = d.pop("ask", UNSET)

        ask_size = d.pop("askSize", UNSET)

        collar_percentage = d.pop("collarPercentage", UNSET)

        buy_collar = d.pop("buyCollar", UNSET)

        sell_collar = d.pop("sellCollar", UNSET)

        open_interest = d.pop("openInterest", UNSET)

        bid_collar = d.pop("bidCollar", UNSET)

        ask_collar = d.pop("askCollar", UNSET)

        _detail = d.pop("detail", UNSET)
        detail: ComHellopublicTradingCoreQuoteBondQuoteDetail | Unset
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = ComHellopublicTradingCoreQuoteBondQuoteDetail.from_dict(_detail)

        trading_halted = d.pop("tradingHalted", UNSET)

        _uptick_rule = d.pop("uptickRule", UNSET)
        uptick_rule: ComHellopublicTradingCoreQuoteSignedQuoteUptickRule | Unset
        if isinstance(_uptick_rule, Unset):
            uptick_rule = UNSET
        else:
            uptick_rule = ComHellopublicTradingCoreQuoteSignedQuoteUptickRule(_uptick_rule)

        com_hellopublic_trading_core_quote_signed_quote = cls(
            symbol=symbol,
            timestamp=timestamp,
            signature=signature,
            last=last,
            bid=bid,
            bid_size=bid_size,
            ask=ask,
            ask_size=ask_size,
            collar_percentage=collar_percentage,
            buy_collar=buy_collar,
            sell_collar=sell_collar,
            open_interest=open_interest,
            bid_collar=bid_collar,
            ask_collar=ask_collar,
            detail=detail,
            trading_halted=trading_halted,
            uptick_rule=uptick_rule,
        )

        com_hellopublic_trading_core_quote_signed_quote.additional_properties = d
        return com_hellopublic_trading_core_quote_signed_quote

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
