from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_matadorapp_shared_customerordergateway_dto_order_leg_type_0_open_close_indicator import (
    ComMatadorappSharedCustomerordergatewayDtoOrderLegType0OpenCloseIndicator,
)
from ..models.com_matadorapp_shared_customerordergateway_dto_order_leg_type_0_side import (
    ComMatadorappSharedCustomerordergatewayDtoOrderLegType0Side,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComMatadorappSharedCustomerordergatewayDtoOrderLegType0")


@_attrs_define
class ComMatadorappSharedCustomerordergatewayDtoOrderLegType0:
    """Leg definition for the strategy.

    Attributes:
        symbol (str): Symbol for the leg.
        side (ComMatadorappSharedCustomerordergatewayDtoOrderLegType0Side): Side for the leg.
        ratio_quantity (int): Ratio quantity for the leg.
        open_close_indicator (ComMatadorappSharedCustomerordergatewayDtoOrderLegType0OpenCloseIndicator | Unset):
            Position effect for the leg. Will be null for equity leg.
    """

    symbol: str
    side: ComMatadorappSharedCustomerordergatewayDtoOrderLegType0Side
    ratio_quantity: int
    open_close_indicator: (
        ComMatadorappSharedCustomerordergatewayDtoOrderLegType0OpenCloseIndicator | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        side = self.side.value

        ratio_quantity = self.ratio_quantity

        open_close_indicator: str | Unset = UNSET
        if not isinstance(self.open_close_indicator, Unset):
            open_close_indicator = self.open_close_indicator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "side": side,
                "ratioQuantity": ratio_quantity,
            }
        )
        if open_close_indicator is not UNSET:
            field_dict["openCloseIndicator"] = open_close_indicator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        side = ComMatadorappSharedCustomerordergatewayDtoOrderLegType0Side(d.pop("side"))

        ratio_quantity = d.pop("ratioQuantity")

        _open_close_indicator = d.pop("openCloseIndicator", UNSET)
        open_close_indicator: (
            ComMatadorappSharedCustomerordergatewayDtoOrderLegType0OpenCloseIndicator | Unset
        )
        if isinstance(_open_close_indicator, Unset):
            open_close_indicator = UNSET
        else:
            open_close_indicator = (
                ComMatadorappSharedCustomerordergatewayDtoOrderLegType0OpenCloseIndicator(
                    _open_close_indicator
                )
            )

        com_matadorapp_shared_customerordergateway_dto_order_leg_type_0 = cls(
            symbol=symbol,
            side=side,
            ratio_quantity=ratio_quantity,
            open_close_indicator=open_close_indicator,
        )

        com_matadorapp_shared_customerordergateway_dto_order_leg_type_0.additional_properties = d
        return com_matadorapp_shared_customerordergateway_dto_order_leg_type_0

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
