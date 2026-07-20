from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComHellopublicHstier2ServiceTaxlotsApiInstrumentSpecificTaxLotDetails")


@_attrs_define
class ComHellopublicHstier2ServiceTaxlotsApiInstrumentSpecificTaxLotDetails:
    """
    Attributes:
        payload_type (str):
    """

    payload_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload_type = self.payload_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payloadType": payload_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payload_type = d.pop("payloadType")

        com_hellopublic_hstier_2_service_taxlots_api_instrument_specific_tax_lot_details = cls(
            payload_type=payload_type,
        )

        com_hellopublic_hstier_2_service_taxlots_api_instrument_specific_tax_lot_details.additional_properties = d
        return com_hellopublic_hstier_2_service_taxlots_api_instrument_specific_tax_lot_details

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
