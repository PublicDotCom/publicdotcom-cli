from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement:
    """
    Attributes:
        long_maintenance_requirement (str | Unset):
        long_initial_requirement (str | Unset):
    """

    long_maintenance_requirement: str | Unset = UNSET
    long_initial_requirement: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        long_maintenance_requirement = self.long_maintenance_requirement

        long_initial_requirement = self.long_initial_requirement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if long_maintenance_requirement is not UNSET:
            field_dict["longMaintenanceRequirement"] = long_maintenance_requirement
        if long_initial_requirement is not UNSET:
            field_dict["longInitialRequirement"] = long_initial_requirement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        long_maintenance_requirement = d.pop("longMaintenanceRequirement", UNSET)

        long_initial_requirement = d.pop("longInitialRequirement", UNSET)

        com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_requirement = cls(
            long_maintenance_requirement=long_maintenance_requirement,
            long_initial_requirement=long_initial_requirement,
        )

        com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_requirement.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_requirement

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
