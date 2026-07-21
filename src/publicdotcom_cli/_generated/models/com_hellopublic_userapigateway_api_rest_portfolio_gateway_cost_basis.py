from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasis")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayCostBasis:
    """Cost basis of a position. What the member paid for entering the position. The cost basis is
    based on tax lots and will factor in wash sales.

       Attributes:
           total_cost (None | str | Unset): What is the dollars paid for entering this position
           unit_cost (None | str | Unset): Totalcost divided by the quantity.
           gain_value (None | str | Unset): Amount of dollars this position gained or lost. Current value - total cost
           gain_percentage (None | str | Unset): 100*gainValue/totalcost
           last_update (datetime.datetime | None | Unset): When was the cost cases last updated.
    """

    total_cost: None | str | Unset = UNSET
    unit_cost: None | str | Unset = UNSET
    gain_value: None | str | Unset = UNSET
    gain_percentage: None | str | Unset = UNSET
    last_update: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_cost: None | str | Unset
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        else:
            total_cost = self.total_cost

        unit_cost: None | str | Unset
        if isinstance(self.unit_cost, Unset):
            unit_cost = UNSET
        else:
            unit_cost = self.unit_cost

        gain_value: None | str | Unset
        if isinstance(self.gain_value, Unset):
            gain_value = UNSET
        else:
            gain_value = self.gain_value

        gain_percentage: None | str | Unset
        if isinstance(self.gain_percentage, Unset):
            gain_percentage = UNSET
        else:
            gain_percentage = self.gain_percentage

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        elif isinstance(self.last_update, datetime.datetime):
            last_update = self.last_update.isoformat()
        else:
            last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost
        if gain_value is not UNSET:
            field_dict["gainValue"] = gain_value
        if gain_percentage is not UNSET:
            field_dict["gainPercentage"] = gain_percentage
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_total_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_cost = _parse_total_cost(d.pop("totalCost", UNSET))

        def _parse_unit_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_cost = _parse_unit_cost(d.pop("unitCost", UNSET))

        def _parse_gain_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gain_value = _parse_gain_value(d.pop("gainValue", UNSET))

        def _parse_gain_percentage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gain_percentage = _parse_gain_percentage(d.pop("gainPercentage", UNSET))

        def _parse_last_update(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_update_type_0 = datetime.datetime.fromisoformat(data)

                return last_update_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_update = _parse_last_update(d.pop("lastUpdate", UNSET))

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis = cls(
            total_cost=total_cost,
            unit_cost=unit_cost,
            gain_value=gain_value,
            gain_percentage=gain_percentage,
            last_update=last_update,
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_portfolio_gateway_cost_basis

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
