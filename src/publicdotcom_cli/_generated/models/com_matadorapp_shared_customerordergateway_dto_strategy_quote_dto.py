from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_matadorapp_shared_customerordergateway_dto_strategy_quote_dto_debit_credit import (
    ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteDtoDebitCredit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_matadorapp_shared_customerordergateway_dto_strategy_leg_dto import (
        ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto,
    )


T = TypeVar("T", bound="ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteDto")


@_attrs_define
class ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteDto:
    """Quote for multileg strategy.

    Attributes:
        strategy_legs (list[ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto]): Legs and their quotes.
        price (str): Strategy price.
        bid (str): Strategy bid (same value as price).
        ask (str): Strategy ask.
        strategy_name (str): Name of the strategy.
        debit_credit (ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteDtoDebitCredit | Unset): Flag to determine
            if the strategy is a debit or credit strategy. If the price is close to $0.00 or the spread
             is across $0.00, e.g. bid = -$0.10 and ask = $0.20 then UNKNOWN is returned.
        equity_quote (ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto | Unset):
        mark (str | Unset): Mark price, average of bid/ask
        expiration_date (datetime.date | Unset): Strategy expiration date. Null if legs expire on different dates or
            equity leg is part of strategy.
    """

    strategy_legs: list[ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto]
    price: str
    bid: str
    ask: str
    strategy_name: str
    debit_credit: ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteDtoDebitCredit | Unset = (
        UNSET
    )
    equity_quote: ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto | Unset = UNSET
    mark: str | Unset = UNSET
    expiration_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_legs = []
        for strategy_legs_item_data in self.strategy_legs:
            strategy_legs_item = strategy_legs_item_data.to_dict()
            strategy_legs.append(strategy_legs_item)

        price = self.price

        bid = self.bid

        ask = self.ask

        strategy_name = self.strategy_name

        debit_credit: str | Unset = UNSET
        if not isinstance(self.debit_credit, Unset):
            debit_credit = self.debit_credit.value

        equity_quote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.equity_quote, Unset):
            equity_quote = self.equity_quote.to_dict()

        mark = self.mark

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyLegs": strategy_legs,
                "price": price,
                "bid": bid,
                "ask": ask,
                "strategyName": strategy_name,
            }
        )
        if debit_credit is not UNSET:
            field_dict["debitCredit"] = debit_credit
        if equity_quote is not UNSET:
            field_dict["equityQuote"] = equity_quote
        if mark is not UNSET:
            field_dict["mark"] = mark
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_matadorapp_shared_customerordergateway_dto_strategy_leg_dto import (
            ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto,
        )

        d = dict(src_dict)
        strategy_legs = []
        _strategy_legs = d.pop("strategyLegs")
        for strategy_legs_item_data in _strategy_legs:
            strategy_legs_item = ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto.from_dict(
                strategy_legs_item_data
            )

            strategy_legs.append(strategy_legs_item)

        price = d.pop("price")

        bid = d.pop("bid")

        ask = d.pop("ask")

        strategy_name = d.pop("strategyName")

        _debit_credit = d.pop("debitCredit", UNSET)
        debit_credit: ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteDtoDebitCredit | Unset
        if isinstance(_debit_credit, Unset):
            debit_credit = UNSET
        else:
            debit_credit = ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteDtoDebitCredit(
                _debit_credit
            )

        _equity_quote = d.pop("equityQuote", UNSET)
        equity_quote: ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto | Unset
        if isinstance(_equity_quote, Unset):
            equity_quote = UNSET
        else:
            equity_quote = ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto.from_dict(
                _equity_quote
            )

        mark = d.pop("mark", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.date | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = datetime.date.fromisoformat(_expiration_date)

        com_matadorapp_shared_customerordergateway_dto_strategy_quote_dto = cls(
            strategy_legs=strategy_legs,
            price=price,
            bid=bid,
            ask=ask,
            strategy_name=strategy_name,
            debit_credit=debit_credit,
            equity_quote=equity_quote,
            mark=mark,
            expiration_date=expiration_date,
        )

        com_matadorapp_shared_customerordergateway_dto_strategy_quote_dto.additional_properties = d
        return com_matadorapp_shared_customerordergateway_dto_strategy_quote_dto

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
