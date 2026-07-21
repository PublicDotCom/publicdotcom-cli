from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_matadorapp_shared_customerordergateway_dto_order_leg_type_0 import (
        ComMatadorappSharedCustomerordergatewayDtoOrderLegType0,
    )


T = TypeVar("T", bound="ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteRequest")


@_attrs_define
class ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteRequest:
    """Request quote for a multi leg strategy.

    Attributes:
        base_symbol (str): Base symbol for the strategy
        option_legs (list[ComMatadorappSharedCustomerordergatewayDtoOrderLegType0 | None]): Option legs for the order.
        equity_leg (ComMatadorappSharedCustomerordergatewayDtoOrderLegType0 | None | Unset): Leg definition for the
            strategy.
    """

    base_symbol: str
    option_legs: list[ComMatadorappSharedCustomerordergatewayDtoOrderLegType0 | None]
    equity_leg: ComMatadorappSharedCustomerordergatewayDtoOrderLegType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.com_matadorapp_shared_customerordergateway_dto_order_leg_type_0 import (
            ComMatadorappSharedCustomerordergatewayDtoOrderLegType0,
        )

        base_symbol = self.base_symbol

        option_legs = []
        for option_legs_item_data in self.option_legs:
            option_legs_item: dict[str, Any] | None
            if isinstance(
                option_legs_item_data, ComMatadorappSharedCustomerordergatewayDtoOrderLegType0
            ):
                option_legs_item = option_legs_item_data.to_dict()
            else:
                option_legs_item = option_legs_item_data
            option_legs.append(option_legs_item)

        equity_leg: dict[str, Any] | None | Unset
        if isinstance(self.equity_leg, Unset):
            equity_leg = UNSET
        elif isinstance(self.equity_leg, ComMatadorappSharedCustomerordergatewayDtoOrderLegType0):
            equity_leg = self.equity_leg.to_dict()
        else:
            equity_leg = self.equity_leg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseSymbol": base_symbol,
                "optionLegs": option_legs,
            }
        )
        if equity_leg is not UNSET:
            field_dict["equityLeg"] = equity_leg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_matadorapp_shared_customerordergateway_dto_order_leg_type_0 import (
            ComMatadorappSharedCustomerordergatewayDtoOrderLegType0,
        )

        d = dict(src_dict)
        base_symbol = d.pop("baseSymbol")

        option_legs = []
        _option_legs = d.pop("optionLegs")
        for option_legs_item_data in _option_legs:

            def _parse_option_legs_item(
                data: object,
            ) -> ComMatadorappSharedCustomerordergatewayDtoOrderLegType0 | None:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemascom_matadorapp_shared_customerordergateway_dto_order_leg_type_0 = ComMatadorappSharedCustomerordergatewayDtoOrderLegType0.from_dict(
                        data
                    )

                    return componentsschemascom_matadorapp_shared_customerordergateway_dto_order_leg_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(ComMatadorappSharedCustomerordergatewayDtoOrderLegType0 | None, data)

            option_legs_item = _parse_option_legs_item(option_legs_item_data)

            option_legs.append(option_legs_item)

        def _parse_equity_leg(
            data: object,
        ) -> ComMatadorappSharedCustomerordergatewayDtoOrderLegType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascom_matadorapp_shared_customerordergateway_dto_order_leg_type_0 = (
                    ComMatadorappSharedCustomerordergatewayDtoOrderLegType0.from_dict(data)
                )

                return (
                    componentsschemascom_matadorapp_shared_customerordergateway_dto_order_leg_type_0
                )
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ComMatadorappSharedCustomerordergatewayDtoOrderLegType0 | None | Unset, data
            )

        equity_leg = _parse_equity_leg(d.pop("equityLeg", UNSET))

        com_matadorapp_shared_customerordergateway_dto_strategy_quote_request = cls(
            base_symbol=base_symbol,
            option_legs=option_legs,
            equity_leg=equity_leg,
        )

        com_matadorapp_shared_customerordergateway_dto_strategy_quote_request.additional_properties = d
        return com_matadorapp_shared_customerordergateway_dto_strategy_quote_request

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
