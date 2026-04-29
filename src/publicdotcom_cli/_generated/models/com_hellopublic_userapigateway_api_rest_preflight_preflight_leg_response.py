from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_leg_response_open_close_indicator import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseOpenCloseIndicator,
)
from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_leg_response_side import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseSide,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_option_details import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponse:
    """# PreflightLegResponse
    Response containing information about an individual leg in a multi-leg order preflight calculation.

    ## Fields

    ### Instrument Information
    - **instrument** - The trading instrument for this leg
    - **side** - The order side (BUY/SELL) for this leg
    - **openCloseIndicator** - Position effect for option legs (BUY_TO_OPEN, BUY_TO_CLOSE, etc.)
    - **ratioQuantity** - The ratio quantity for this leg in the strategy

    ### Cost and Fee Information
    - **estimatedCommission** - The estimated commission for this specific leg
    - **estimatedCost** - The estimated cost for this leg including fees
    - **estimatedProceeds** - The estimated proceeds for this leg (for sell legs)

    ### Option-Specific Information
    - **optionDetails** - Option-specific details like strike price, expiration, fees, and rebates

        Attributes:
            instrument (ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument):
            side (ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseSide):
            ratio_quantity (int):
            open_close_indicator (ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseOpenCloseIndicator |
                Unset):
            option_details (ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails | Unset):
    """

    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument
    side: ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseSide
    ratio_quantity: int
    open_close_indicator: (
        ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseOpenCloseIndicator | Unset
    ) = UNSET
    option_details: ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument.to_dict()

        side = self.side.value

        ratio_quantity = self.ratio_quantity

        open_close_indicator: str | Unset = UNSET
        if not isinstance(self.open_close_indicator, Unset):
            open_close_indicator = self.open_close_indicator.value

        option_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.option_details, Unset):
            option_details = self.option_details.to_dict()

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
        if option_details is not UNSET:
            field_dict["optionDetails"] = option_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_option_details import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails,
        )

        d = dict(src_dict)
        instrument = ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
            d.pop("instrument")
        )

        side = ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseSide(d.pop("side"))

        ratio_quantity = d.pop("ratioQuantity")

        _open_close_indicator = d.pop("openCloseIndicator", UNSET)
        open_close_indicator: (
            ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseOpenCloseIndicator
            | Unset
        )
        if isinstance(_open_close_indicator, Unset):
            open_close_indicator = UNSET
        else:
            open_close_indicator = (
                ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseOpenCloseIndicator(
                    _open_close_indicator
                )
            )

        _option_details = d.pop("optionDetails", UNSET)
        option_details: ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails | Unset
        if isinstance(_option_details, Unset):
            option_details = UNSET
        else:
            option_details = (
                ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails.from_dict(
                    _option_details
                )
            )

        com_hellopublic_userapigateway_api_rest_preflight_preflight_leg_response = cls(
            instrument=instrument,
            side=side,
            ratio_quantity=ratio_quantity,
            open_close_indicator=open_close_indicator,
            option_details=option_details,
        )

        com_hellopublic_userapigateway_api_rest_preflight_preflight_leg_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_preflight_leg_response

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
