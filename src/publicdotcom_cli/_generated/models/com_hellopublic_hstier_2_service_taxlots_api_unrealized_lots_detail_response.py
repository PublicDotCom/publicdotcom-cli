from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_hstier_2_service_taxlots_api_option_specific_tax_lot_details import (
        ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails,
    )
    from ..models.com_hellopublic_hstier_2_service_taxlots_api_unrealized_lot import (
        ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLot,
    )


T = TypeVar("T", bound="ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse")


@_attrs_define
class ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsDetailResponse:
    """Unrealised lots and information about the instrument

    Attributes:
        as_of (datetime.date): The trading session after which this summary was calculated
        symbol (str): The ticker
        company_name (str): Company name
        lots (list[ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLot] | Unset): The lots sorted by openDate
        details (ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails | Unset):
    """

    as_of: datetime.date
    symbol: str
    company_name: str
    lots: list[ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLot] | Unset = UNSET
    details: ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of.isoformat()

        symbol = self.symbol

        company_name = self.company_name

        lots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lots, Unset):
            lots = []
            for lots_item_data in self.lots:
                lots_item = lots_item_data.to_dict()
                lots.append(lots_item)

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asOf": as_of,
                "symbol": symbol,
                "companyName": company_name,
            }
        )
        if lots is not UNSET:
            field_dict["lots"] = lots
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_hstier_2_service_taxlots_api_option_specific_tax_lot_details import (
            ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails,
        )
        from ..models.com_hellopublic_hstier_2_service_taxlots_api_unrealized_lot import (
            ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLot,
        )

        d = dict(src_dict)
        as_of = datetime.date.fromisoformat(d.pop("asOf"))

        symbol = d.pop("symbol")

        company_name = d.pop("companyName")

        _lots = d.pop("lots", UNSET)
        lots: list[ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLot] | Unset = UNSET
        if _lots is not UNSET:
            lots = []
            for lots_item_data in _lots:
                lots_item = ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLot.from_dict(
                    lots_item_data
                )

                lots.append(lots_item)

        _details = d.pop("details", UNSET)
        details: ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails.from_dict(
                _details
            )

        com_hellopublic_hstier_2_service_taxlots_api_unrealized_lots_detail_response = cls(
            as_of=as_of,
            symbol=symbol,
            company_name=company_name,
            lots=lots,
            details=details,
        )

        com_hellopublic_hstier_2_service_taxlots_api_unrealized_lots_detail_response.additional_properties = d
        return com_hellopublic_hstier_2_service_taxlots_api_unrealized_lots_detail_response

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
