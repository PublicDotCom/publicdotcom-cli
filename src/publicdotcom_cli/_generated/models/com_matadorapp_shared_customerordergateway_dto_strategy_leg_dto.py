from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_matadorapp_shared_customerordergateway_dto_strategy_leg_dto_open_close_indicator import (
    ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoOpenCloseIndicator,
)
from ..models.com_matadorapp_shared_customerordergateway_dto_strategy_leg_dto_side import (
    ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoSide,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_trading_core_quote_signed_quote import (
        ComHellopublicTradingCoreQuoteSignedQuote,
    )
    from ..models.com_matadorapp_shared_customerordergateway_dto_strategy_leg_instrument_dto import (
        ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDto,
    )


T = TypeVar("T", bound="ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto")


@_attrs_define
class ComMatadorappSharedCustomerordergatewayDtoStrategyLegDto:
    """
    Attributes:
        instrument (ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDto): Defines the leg instrument.
        side (ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoSide): Order side for the leg
        ratio_quantity (int): Ratio quantity for the leg
        open_close_indicator (ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoOpenCloseIndicator | Unset): Open
            close indicator for the leg. Null for equity leg
        quote (ComHellopublicTradingCoreQuoteSignedQuote | Unset): The original version did not allow null values for
            bid/ask data. This was relaxed later to allow equity to use super-quotes
    """

    instrument: ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDto
    side: ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoSide
    ratio_quantity: int
    open_close_indicator: (
        ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoOpenCloseIndicator | Unset
    ) = UNSET
    quote: ComHellopublicTradingCoreQuoteSignedQuote | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument.to_dict()

        side = self.side.value

        ratio_quantity = self.ratio_quantity

        open_close_indicator: str | Unset = UNSET
        if not isinstance(self.open_close_indicator, Unset):
            open_close_indicator = self.open_close_indicator.value

        quote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "side": side,
                "ratioQuantity": ratio_quantity,
            }
        )
        if open_close_indicator is not UNSET:
            field_dict["openCloseIndicator"] = open_close_indicator
        if quote is not UNSET:
            field_dict["quote"] = quote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_trading_core_quote_signed_quote import (
            ComHellopublicTradingCoreQuoteSignedQuote,
        )
        from ..models.com_matadorapp_shared_customerordergateway_dto_strategy_leg_instrument_dto import (
            ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDto,
        )

        d = dict(src_dict)
        instrument = ComMatadorappSharedCustomerordergatewayDtoStrategyLegInstrumentDto.from_dict(
            d.pop("instrument")
        )

        side = ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoSide(d.pop("side"))

        ratio_quantity = d.pop("ratioQuantity")

        _open_close_indicator = d.pop("openCloseIndicator", UNSET)
        open_close_indicator: (
            ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoOpenCloseIndicator | Unset
        )
        if isinstance(_open_close_indicator, Unset):
            open_close_indicator = UNSET
        else:
            open_close_indicator = (
                ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoOpenCloseIndicator(
                    _open_close_indicator
                )
            )

        _quote = d.pop("quote", UNSET)
        quote: ComHellopublicTradingCoreQuoteSignedQuote | Unset
        if isinstance(_quote, Unset):
            quote = UNSET
        else:
            quote = ComHellopublicTradingCoreQuoteSignedQuote.from_dict(_quote)

        com_matadorapp_shared_customerordergateway_dto_strategy_leg_dto = cls(
            instrument=instrument,
            side=side,
            ratio_quantity=ratio_quantity,
            open_close_indicator=open_close_indicator,
            quote=quote,
        )

        com_matadorapp_shared_customerordergateway_dto_strategy_leg_dto.additional_properties = d
        return com_matadorapp_shared_customerordergateway_dto_strategy_leg_dto

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
