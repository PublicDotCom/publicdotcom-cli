from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote_outcome import (
    ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteOutcome,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_bond_details import (
        ComHellopublicUserapigatewayApiRestMarketdataQuoteBondDetails,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_one_day_change import (
        ComHellopublicUserapigatewayApiRestMarketdataQuoteOneDayChange,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_option_details import (
        ComHellopublicUserapigatewayApiRestMarketdataQuoteOptionDetails,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote")


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuote:
    """
    Attributes:
        instrument (ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument):
        outcome (ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteOutcome): The outcome status of the quote
            request.
        last (str | Unset): The last traded price of the instrument. Can be null if no trades have occurred.
        last_timestamp (datetime.datetime | Unset): Timestamp of when the last trade occurred. Can be null if no trades
            have occurred.
        bid (str | Unset): The current bid price (sell-side price) in the market. Can be null if no bid exists.
        bid_size (int | Unset): Number of shares, contracts, or units available at the given bid price.
        bid_timestamp (datetime.datetime | Unset): Timestamp of when the bid price was last updated. Can be null if no
            bid exists.
        ask (str | Unset): The current ask price (buy-side price) in the market. Can be null if no ask exists.
        ask_size (int | Unset): Number of shares, contracts, or units available at the given ask price.
        ask_timestamp (datetime.datetime | Unset): Timestamp of when the ask price was last updated. Can be null if no
            ask exists.
        volume (int | Unset): The total volume traded on the date of the last trade.
        open_interest (int | Unset): The total number of options contracts that are not closed or delivered on a
            particular day.
        previous_close (str | Unset): The previous day's close price from the last trading session.
        one_day_change (ComHellopublicUserapigatewayApiRestMarketdataQuoteOneDayChange | Unset): Represents the one-day
            price change data for a quote.

            The change values are provided by the data source (e.g., Xignite) and may differ from simple subtraction
            of current price minus previous close due to corporate actions, stock splits, or other adjustments.
        option_details (ComHellopublicUserapigatewayApiRestMarketdataQuoteOptionDetails | Unset): Option-specific
            details including Greeks, strike price, and mid price.
        bond_details (ComHellopublicUserapigatewayApiRestMarketdataQuoteBondDetails | Unset): Bond-specific details for
            a quote.
    """

    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument
    outcome: ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteOutcome
    last: str | Unset = UNSET
    last_timestamp: datetime.datetime | Unset = UNSET
    bid: str | Unset = UNSET
    bid_size: int | Unset = UNSET
    bid_timestamp: datetime.datetime | Unset = UNSET
    ask: str | Unset = UNSET
    ask_size: int | Unset = UNSET
    ask_timestamp: datetime.datetime | Unset = UNSET
    volume: int | Unset = UNSET
    open_interest: int | Unset = UNSET
    previous_close: str | Unset = UNSET
    one_day_change: ComHellopublicUserapigatewayApiRestMarketdataQuoteOneDayChange | Unset = UNSET
    option_details: ComHellopublicUserapigatewayApiRestMarketdataQuoteOptionDetails | Unset = UNSET
    bond_details: ComHellopublicUserapigatewayApiRestMarketdataQuoteBondDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument.to_dict()

        outcome = self.outcome.value

        last = self.last

        last_timestamp: str | Unset = UNSET
        if not isinstance(self.last_timestamp, Unset):
            last_timestamp = self.last_timestamp.isoformat()

        bid = self.bid

        bid_size = self.bid_size

        bid_timestamp: str | Unset = UNSET
        if not isinstance(self.bid_timestamp, Unset):
            bid_timestamp = self.bid_timestamp.isoformat()

        ask = self.ask

        ask_size = self.ask_size

        ask_timestamp: str | Unset = UNSET
        if not isinstance(self.ask_timestamp, Unset):
            ask_timestamp = self.ask_timestamp.isoformat()

        volume = self.volume

        open_interest = self.open_interest

        previous_close = self.previous_close

        one_day_change: dict[str, Any] | Unset = UNSET
        if not isinstance(self.one_day_change, Unset):
            one_day_change = self.one_day_change.to_dict()

        option_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.option_details, Unset):
            option_details = self.option_details.to_dict()

        bond_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bond_details, Unset):
            bond_details = self.bond_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "outcome": outcome,
            }
        )
        if last is not UNSET:
            field_dict["last"] = last
        if last_timestamp is not UNSET:
            field_dict["lastTimestamp"] = last_timestamp
        if bid is not UNSET:
            field_dict["bid"] = bid
        if bid_size is not UNSET:
            field_dict["bidSize"] = bid_size
        if bid_timestamp is not UNSET:
            field_dict["bidTimestamp"] = bid_timestamp
        if ask is not UNSET:
            field_dict["ask"] = ask
        if ask_size is not UNSET:
            field_dict["askSize"] = ask_size
        if ask_timestamp is not UNSET:
            field_dict["askTimestamp"] = ask_timestamp
        if volume is not UNSET:
            field_dict["volume"] = volume
        if open_interest is not UNSET:
            field_dict["openInterest"] = open_interest
        if previous_close is not UNSET:
            field_dict["previousClose"] = previous_close
        if one_day_change is not UNSET:
            field_dict["oneDayChange"] = one_day_change
        if option_details is not UNSET:
            field_dict["optionDetails"] = option_details
        if bond_details is not UNSET:
            field_dict["bondDetails"] = bond_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_bond_details import (
            ComHellopublicUserapigatewayApiRestMarketdataQuoteBondDetails,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_one_day_change import (
            ComHellopublicUserapigatewayApiRestMarketdataQuoteOneDayChange,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_marketdata_quote_option_details import (
            ComHellopublicUserapigatewayApiRestMarketdataQuoteOptionDetails,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )

        d = dict(src_dict)
        instrument = ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
            d.pop("instrument")
        )

        outcome = ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteOutcome(
            d.pop("outcome")
        )

        last = d.pop("last", UNSET)

        _last_timestamp = d.pop("lastTimestamp", UNSET)
        last_timestamp: datetime.datetime | Unset
        if isinstance(_last_timestamp, Unset):
            last_timestamp = UNSET
        else:
            last_timestamp = datetime.datetime.fromisoformat(_last_timestamp)

        bid = d.pop("bid", UNSET)

        bid_size = d.pop("bidSize", UNSET)

        _bid_timestamp = d.pop("bidTimestamp", UNSET)
        bid_timestamp: datetime.datetime | Unset
        if isinstance(_bid_timestamp, Unset):
            bid_timestamp = UNSET
        else:
            bid_timestamp = datetime.datetime.fromisoformat(_bid_timestamp)

        ask = d.pop("ask", UNSET)

        ask_size = d.pop("askSize", UNSET)

        _ask_timestamp = d.pop("askTimestamp", UNSET)
        ask_timestamp: datetime.datetime | Unset
        if isinstance(_ask_timestamp, Unset):
            ask_timestamp = UNSET
        else:
            ask_timestamp = datetime.datetime.fromisoformat(_ask_timestamp)

        volume = d.pop("volume", UNSET)

        open_interest = d.pop("openInterest", UNSET)

        previous_close = d.pop("previousClose", UNSET)

        _one_day_change = d.pop("oneDayChange", UNSET)
        one_day_change: ComHellopublicUserapigatewayApiRestMarketdataQuoteOneDayChange | Unset
        if isinstance(_one_day_change, Unset):
            one_day_change = UNSET
        else:
            one_day_change = (
                ComHellopublicUserapigatewayApiRestMarketdataQuoteOneDayChange.from_dict(
                    _one_day_change
                )
            )

        _option_details = d.pop("optionDetails", UNSET)
        option_details: ComHellopublicUserapigatewayApiRestMarketdataQuoteOptionDetails | Unset
        if isinstance(_option_details, Unset):
            option_details = UNSET
        else:
            option_details = (
                ComHellopublicUserapigatewayApiRestMarketdataQuoteOptionDetails.from_dict(
                    _option_details
                )
            )

        _bond_details = d.pop("bondDetails", UNSET)
        bond_details: ComHellopublicUserapigatewayApiRestMarketdataQuoteBondDetails | Unset
        if isinstance(_bond_details, Unset):
            bond_details = UNSET
        else:
            bond_details = ComHellopublicUserapigatewayApiRestMarketdataQuoteBondDetails.from_dict(
                _bond_details
            )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote = cls(
            instrument=instrument,
            outcome=outcome,
            last=last,
            last_timestamp=last_timestamp,
            bid=bid,
            bid_size=bid_size,
            bid_timestamp=bid_timestamp,
            ask=ask,
            ask_size=ask_size,
            ask_timestamp=ask_timestamp,
            volume=volume,
            open_interest=open_interest,
            previous_close=previous_close,
            one_day_change=one_day_change,
            option_details=option_details,
            bond_details=bond_details,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_quote

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
