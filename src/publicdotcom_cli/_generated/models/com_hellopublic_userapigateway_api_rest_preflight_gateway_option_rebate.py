from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightGatewayOptionRebate")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightGatewayOptionRebate:
    """
    Attributes:
        estimated_option_rebate (str | Unset):
        option_rebate_percent (int | Unset):
        per_contract_rebate (str | Unset):
    """

    estimated_option_rebate: str | Unset = UNSET
    option_rebate_percent: int | Unset = UNSET
    per_contract_rebate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        estimated_option_rebate = self.estimated_option_rebate

        option_rebate_percent = self.option_rebate_percent

        per_contract_rebate = self.per_contract_rebate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if estimated_option_rebate is not UNSET:
            field_dict["estimatedOptionRebate"] = estimated_option_rebate
        if option_rebate_percent is not UNSET:
            field_dict["optionRebatePercent"] = option_rebate_percent
        if per_contract_rebate is not UNSET:
            field_dict["perContractRebate"] = per_contract_rebate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        estimated_option_rebate = d.pop("estimatedOptionRebate", UNSET)

        option_rebate_percent = d.pop("optionRebatePercent", UNSET)

        per_contract_rebate = d.pop("perContractRebate", UNSET)

        com_hellopublic_userapigateway_api_rest_preflight_gateway_option_rebate = cls(
            estimated_option_rebate=estimated_option_rebate,
            option_rebate_percent=option_rebate_percent,
            per_contract_rebate=per_contract_rebate,
        )

        com_hellopublic_userapigateway_api_rest_preflight_gateway_option_rebate.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_gateway_option_rebate

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
