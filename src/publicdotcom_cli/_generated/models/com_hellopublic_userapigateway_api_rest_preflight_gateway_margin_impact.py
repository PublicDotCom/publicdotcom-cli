from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact:
    """
    Attributes:
        margin_usage_impact (str | Unset):
        initial_margin_requirement (str | Unset):
    """

    margin_usage_impact: str | Unset = UNSET
    initial_margin_requirement: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        margin_usage_impact = self.margin_usage_impact

        initial_margin_requirement = self.initial_margin_requirement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if margin_usage_impact is not UNSET:
            field_dict["marginUsageImpact"] = margin_usage_impact
        if initial_margin_requirement is not UNSET:
            field_dict["initialMarginRequirement"] = initial_margin_requirement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        margin_usage_impact = d.pop("marginUsageImpact", UNSET)

        initial_margin_requirement = d.pop("initialMarginRequirement", UNSET)

        com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_impact = cls(
            margin_usage_impact=margin_usage_impact,
            initial_margin_requirement=initial_margin_requirement,
        )

        com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_impact.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_impact

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
