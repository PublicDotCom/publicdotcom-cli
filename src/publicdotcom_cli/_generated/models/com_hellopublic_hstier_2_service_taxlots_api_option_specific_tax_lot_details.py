from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_hstier_2_service_taxlots_api_option_specific_tax_lot_details_option_type import (
    ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetailsOptionType,
)

T = TypeVar("T", bound="ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails")


@_attrs_define
class ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails:
    """
    Attributes:
        payload_type (str):
        root_symbol (str):
        strike_price (str):
        expiration_date (datetime.date):
        option_type (ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetailsOptionType):
    """

    payload_type: str
    root_symbol: str
    strike_price: str
    expiration_date: datetime.date
    option_type: ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetailsOptionType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload_type = self.payload_type

        root_symbol = self.root_symbol

        strike_price = self.strike_price

        expiration_date = self.expiration_date.isoformat()

        option_type = self.option_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payloadType": payload_type,
                "rootSymbol": root_symbol,
                "strikePrice": strike_price,
                "expirationDate": expiration_date,
                "optionType": option_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payload_type = d.pop("payloadType")

        root_symbol = d.pop("rootSymbol")

        strike_price = d.pop("strikePrice")

        expiration_date = datetime.date.fromisoformat(d.pop("expirationDate"))

        option_type = ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetailsOptionType(
            d.pop("optionType")
        )

        com_hellopublic_hstier_2_service_taxlots_api_option_specific_tax_lot_details = cls(
            payload_type=payload_type,
            root_symbol=root_symbol,
            strike_price=strike_price,
            expiration_date=expiration_date,
            option_type=option_type,
        )

        com_hellopublic_hstier_2_service_taxlots_api_option_specific_tax_lot_details.additional_properties = d
        return com_hellopublic_hstier_2_service_taxlots_api_option_specific_tax_lot_details

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
