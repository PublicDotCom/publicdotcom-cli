from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_request_equity_market_session import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestEquityMarketSession,
)
from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_request_open_close_indicator import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOpenCloseIndicator,
)
from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_request_order_side import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderSide,
)
from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_request_order_type import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration import (
        ComHellopublicUserapigatewayApiRestOrderOrderExpiration,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequest:
    """
    Attributes:
        instrument (ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument):
        order_side (ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderSide): The Order Side
            BUY/SELL. For Options also include the openCloseIndicator
        order_type (ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderType): The Type of order
        expiration (ComHellopublicUserapigatewayApiRestOrderOrderExpiration):
        quantity (str | Unset): The order quantity. Used when buying/selling whole shares and when selling fractional.
            Mutually exclusive with `amount`
        amount (str | Unset): The order amount. Used when buying/selling shares for a specific notional value
        limit_price (str | Unset): The limit price. Used when orderType = LIMIT or orderType = STOP_LIMIT
        stop_price (str | Unset): The stop price. Used when orderType = STOP or orderType = STOP_LIMIT
        equity_market_session (ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestEquityMarketSession
            | Unset): The market session in which the order may execute.
            Extended hours are available only for DAY time-in-force equity orders and can execute any time from 4:00 a.m. ET
            through 8:00 p.m. ET.
            If omitted, the session defaults to CORE.
        open_close_indicator (ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOpenCloseIndicator |
            Unset): Used for options to indicate if this is BUY to OPEN/CLOSE. Also used for shorting equities to indicate
            SELL-to-OPEN (opening a short position) or BUY-to-CLOSE (closing a short position).
        validate_order (bool | Unset): If true, the order will be validated against current account state. Defaults to
            true.
    """

    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument
    order_side: ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderSide
    order_type: ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderType
    expiration: ComHellopublicUserapigatewayApiRestOrderOrderExpiration
    quantity: str | Unset = UNSET
    amount: str | Unset = UNSET
    limit_price: str | Unset = UNSET
    stop_price: str | Unset = UNSET
    equity_market_session: (
        ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestEquityMarketSession
        | Unset
    ) = UNSET
    open_close_indicator: (
        ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOpenCloseIndicator
        | Unset
    ) = UNSET
    validate_order: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument.to_dict()

        order_side = self.order_side.value

        order_type = self.order_type.value

        expiration = self.expiration.to_dict()

        quantity = self.quantity

        amount = self.amount

        limit_price = self.limit_price

        stop_price = self.stop_price

        equity_market_session: str | Unset = UNSET
        if not isinstance(self.equity_market_session, Unset):
            equity_market_session = self.equity_market_session.value

        open_close_indicator: str | Unset = UNSET
        if not isinstance(self.open_close_indicator, Unset):
            open_close_indicator = self.open_close_indicator.value

        validate_order = self.validate_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "orderSide": order_side,
                "orderType": order_type,
                "expiration": expiration,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if amount is not UNSET:
            field_dict["amount"] = amount
        if limit_price is not UNSET:
            field_dict["limitPrice"] = limit_price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if equity_market_session is not UNSET:
            field_dict["equityMarketSession"] = equity_market_session
        if open_close_indicator is not UNSET:
            field_dict["openCloseIndicator"] = open_close_indicator
        if validate_order is not UNSET:
            field_dict["validateOrder"] = validate_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_order_expiration import (
            ComHellopublicUserapigatewayApiRestOrderOrderExpiration,
        )

        d = dict(src_dict)
        instrument = ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
            d.pop("instrument")
        )

        order_side = ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderSide(
            d.pop("orderSide")
        )

        order_type = ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderType(
            d.pop("orderType")
        )

        expiration = ComHellopublicUserapigatewayApiRestOrderOrderExpiration.from_dict(
            d.pop("expiration")
        )

        quantity = d.pop("quantity", UNSET)

        amount = d.pop("amount", UNSET)

        limit_price = d.pop("limitPrice", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        _equity_market_session = d.pop("equityMarketSession", UNSET)
        equity_market_session: (
            ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestEquityMarketSession
            | Unset
        )
        if isinstance(_equity_market_session, Unset):
            equity_market_session = UNSET
        else:
            equity_market_session = ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestEquityMarketSession(
                _equity_market_session
            )

        _open_close_indicator = d.pop("openCloseIndicator", UNSET)
        open_close_indicator: (
            ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOpenCloseIndicator
            | Unset
        )
        if isinstance(_open_close_indicator, Unset):
            open_close_indicator = UNSET
        else:
            open_close_indicator = ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOpenCloseIndicator(
                _open_close_indicator
            )

        validate_order = d.pop("validateOrder", UNSET)

        com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_request = cls(
            instrument=instrument,
            order_side=order_side,
            order_type=order_type,
            expiration=expiration,
            quantity=quantity,
            amount=amount,
            limit_price=limit_price,
            stop_price=stop_price,
            equity_market_session=equity_market_session,
            open_close_indicator=open_close_indicator,
            validate_order=validate_order,
        )

        com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_request.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_request

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
