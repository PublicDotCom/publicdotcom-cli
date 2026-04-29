from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_short_selling_availability import (
    ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingAvailability,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_short_selling_uptick_rule import (
    ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingUptickRule,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderGatewayShortSelling")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderGatewayShortSelling:
    """Short-selling information for the given instrument.

    Attributes:
        availability (ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingAvailability): the availability of
            short-selling for this instrument.
        uptick_rule (ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingUptickRule): the Uptick Rule is
            triggered for equities when the price today or yesterday has dropped at least 10 percent since previous days'
            closing price.
        hard_to_borrow_percentage_rate (str | Unset): the hard to borrow rate as a percentage value.
        initial_margin_requirement_percentage (str | Unset): the initial margin requirement as a percentage value.
        maintenance_margin_requirement_percentage (str | Unset): the maintenance margin requirement as a percentage
            value.
        max_quantity_for_locate (int | Unset): the maximum quantity that we can request to locate for all hard-to-borrow
            stocks. The actual number we can locate can be lower for concrete stocks.
    """

    availability: ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingAvailability
    uptick_rule: ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingUptickRule
    hard_to_borrow_percentage_rate: str | Unset = UNSET
    initial_margin_requirement_percentage: str | Unset = UNSET
    maintenance_margin_requirement_percentage: str | Unset = UNSET
    max_quantity_for_locate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability = self.availability.value

        uptick_rule = self.uptick_rule.value

        hard_to_borrow_percentage_rate = self.hard_to_borrow_percentage_rate

        initial_margin_requirement_percentage = self.initial_margin_requirement_percentage

        maintenance_margin_requirement_percentage = self.maintenance_margin_requirement_percentage

        max_quantity_for_locate = self.max_quantity_for_locate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availability": availability,
                "uptickRule": uptick_rule,
            }
        )
        if hard_to_borrow_percentage_rate is not UNSET:
            field_dict["hardToBorrowPercentageRate"] = hard_to_borrow_percentage_rate
        if initial_margin_requirement_percentage is not UNSET:
            field_dict["initialMarginRequirementPercentage"] = initial_margin_requirement_percentage
        if maintenance_margin_requirement_percentage is not UNSET:
            field_dict["maintenanceMarginRequirementPercentage"] = (
                maintenance_margin_requirement_percentage
            )
        if max_quantity_for_locate is not UNSET:
            field_dict["maxQuantityForLocate"] = max_quantity_for_locate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability = ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingAvailability(
            d.pop("availability")
        )

        uptick_rule = ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingUptickRule(
            d.pop("uptickRule")
        )

        hard_to_borrow_percentage_rate = d.pop("hardToBorrowPercentageRate", UNSET)

        initial_margin_requirement_percentage = d.pop("initialMarginRequirementPercentage", UNSET)

        maintenance_margin_requirement_percentage = d.pop(
            "maintenanceMarginRequirementPercentage", UNSET
        )

        max_quantity_for_locate = d.pop("maxQuantityForLocate", UNSET)

        com_hellopublic_userapigateway_api_rest_order_gateway_short_selling = cls(
            availability=availability,
            uptick_rule=uptick_rule,
            hard_to_borrow_percentage_rate=hard_to_borrow_percentage_rate,
            initial_margin_requirement_percentage=initial_margin_requirement_percentage,
            maintenance_margin_requirement_percentage=maintenance_margin_requirement_percentage,
            max_quantity_for_locate=max_quantity_for_locate,
        )

        com_hellopublic_userapigateway_api_rest_order_gateway_short_selling.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_gateway_short_selling

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
