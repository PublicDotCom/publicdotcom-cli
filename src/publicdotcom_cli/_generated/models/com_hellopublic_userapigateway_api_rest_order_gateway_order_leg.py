from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_leg_open_close_indicator import (
    ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegOpenCloseIndicator,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_leg_side import (
    ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegSide,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_leg_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayLegInstrument,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderGatewayOrderLeg:
    """Option or equity leg. There can never be more than 1 equity leg.

    Attributes:
        instrument (ComHellopublicUserapigatewayApiRestOrderGatewayLegInstrument):
        side (ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegSide):
        open_close_indicator (ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegOpenCloseIndicator | Unset):
            required when instrument.type = OPTION, used to determine if the leg is buy-to-open or buy-to-close
        ratio_quantity (int | Unset): The ratio between legs. Equity legs will typically be 100 shares, and option legs
            1 contract
    """

    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayLegInstrument
    side: ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegSide
    open_close_indicator: (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegOpenCloseIndicator | Unset
    ) = UNSET
    ratio_quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument.to_dict()

        side = self.side.value

        open_close_indicator: str | Unset = UNSET
        if not isinstance(self.open_close_indicator, Unset):
            open_close_indicator = self.open_close_indicator.value

        ratio_quantity = self.ratio_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "side": side,
            }
        )
        if open_close_indicator is not UNSET:
            field_dict["openCloseIndicator"] = open_close_indicator
        if ratio_quantity is not UNSET:
            field_dict["ratioQuantity"] = ratio_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_leg_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayLegInstrument,
        )

        d = dict(src_dict)
        instrument = ComHellopublicUserapigatewayApiRestOrderGatewayLegInstrument.from_dict(
            d.pop("instrument")
        )

        side = ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegSide(d.pop("side"))

        _open_close_indicator = d.pop("openCloseIndicator", UNSET)
        open_close_indicator: (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegOpenCloseIndicator | Unset
        )
        if isinstance(_open_close_indicator, Unset):
            open_close_indicator = UNSET
        else:
            open_close_indicator = (
                ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegOpenCloseIndicator(
                    _open_close_indicator
                )
            )

        ratio_quantity = d.pop("ratioQuantity", UNSET)

        com_hellopublic_userapigateway_api_rest_order_gateway_order_leg = cls(
            instrument=instrument,
            side=side,
            open_close_indicator=open_close_indicator,
            ratio_quantity=ratio_quantity,
        )

        com_hellopublic_userapigateway_api_rest_order_gateway_order_leg.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_gateway_order_leg

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
