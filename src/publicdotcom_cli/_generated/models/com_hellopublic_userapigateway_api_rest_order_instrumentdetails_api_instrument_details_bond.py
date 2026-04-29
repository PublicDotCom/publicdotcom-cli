from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond"
)


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond:
    """
    Attributes:
        payload_type (str):
        has_outstanding (bool | Unset):
    """

    payload_type: str
    has_outstanding: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload_type = self.payload_type

        has_outstanding = self.has_outstanding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payloadType": payload_type,
            }
        )
        if has_outstanding is not UNSET:
            field_dict["hasOutstanding"] = has_outstanding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payload_type = d.pop("payloadType")

        has_outstanding = d.pop("hasOutstanding", UNSET)

        com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_bond = cls(
            payload_type=payload_type,
            has_outstanding=has_outstanding,
        )

        com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_bond.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_bond

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
