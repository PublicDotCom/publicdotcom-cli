from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bar import Bar


T = TypeVar("T", bound="EventContractChart")


@_attrs_define
class EventContractChart:
    """Prices/OHLC are in dollars (0.00 to 1.00) for the side the symbol names, so a .N symbol carries the NO prices. The
    price is the implied probability, so multiply by 100 for cents/percent. Bars start at the first period with a price,
    so charts in one response can start at different timestamps and are aligned by timestamp, not by index.

        Attributes:
            symbol (str | Unset):
            previous_close_price (None | str | Unset):
            current_price (None | str | Unset):
            total_gain_loss (None | str | Unset):
            total_gain_loss_percentage (None | str | Unset):
            bars (list[Bar] | Unset):
    """

    symbol: str | Unset = UNSET
    previous_close_price: None | str | Unset = UNSET
    current_price: None | str | Unset = UNSET
    total_gain_loss: None | str | Unset = UNSET
    total_gain_loss_percentage: None | str | Unset = UNSET
    bars: list[Bar] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        previous_close_price: None | str | Unset
        if isinstance(self.previous_close_price, Unset):
            previous_close_price = UNSET
        else:
            previous_close_price = self.previous_close_price

        current_price: None | str | Unset
        if isinstance(self.current_price, Unset):
            current_price = UNSET
        else:
            current_price = self.current_price

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

        bars: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bars, Unset):
            bars = []
            for bars_item_data in self.bars:
                bars_item = bars_item_data.to_dict()
                bars.append(bars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if previous_close_price is not UNSET:
            field_dict["previousClosePrice"] = previous_close_price
        if current_price is not UNSET:
            field_dict["currentPrice"] = current_price
        if total_gain_loss is not UNSET:
            field_dict["totalGainLoss"] = total_gain_loss
        if total_gain_loss_percentage is not UNSET:
            field_dict["totalGainLossPercentage"] = total_gain_loss_percentage
        if bars is not UNSET:
            field_dict["bars"] = bars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bar import Bar

        d = dict(src_dict)
        symbol = d.pop("symbol", UNSET)

        def _parse_previous_close_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_close_price = _parse_previous_close_price(d.pop("previousClosePrice", UNSET))

        def _parse_current_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_price = _parse_current_price(d.pop("currentPrice", UNSET))

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

        _bars = d.pop("bars", UNSET)
        bars: list[Bar] | Unset = UNSET
        if _bars is not UNSET:
            bars = []
            for bars_item_data in _bars:
                bars_item = Bar.from_dict(bars_item_data)

                bars.append(bars_item)

        event_contract_chart = cls(
            symbol=symbol,
            previous_close_price=previous_close_price,
            current_price=current_price,
            total_gain_loss=total_gain_loss,
            total_gain_loss_percentage=total_gain_loss_percentage,
            bars=bars,
        )

        event_contract_chart.additional_properties = d
        return event_contract_chart

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
