from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.com_hellopublic_hstier_2_service_taxlots_api_unrealized_lot_summary import (
        ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotSummary,
    )


T = TypeVar("T", bound="ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse")


@_attrs_define
class ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotsSummaryResponse:
    """An overview of the unrealized tax lots

    Attributes:
        as_of (datetime.date): The trading session after which this summary was calculated
        lots (list[ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotSummary]): The lots sorted by openDate
        short_term (str): The short term profit or loss
        long_term (str): The long term profit or loss
        sixty_forty_term (str): The 60/40 profit loss.
        total_profit_loss (str): The total profit or loss
    """

    as_of: datetime.date
    lots: list[ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotSummary]
    short_term: str
    long_term: str
    sixty_forty_term: str
    total_profit_loss: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of.isoformat()

        lots = []
        for lots_item_data in self.lots:
            lots_item = lots_item_data.to_dict()
            lots.append(lots_item)

        short_term = self.short_term

        long_term = self.long_term

        sixty_forty_term = self.sixty_forty_term

        total_profit_loss = self.total_profit_loss

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asOf": as_of,
                "lots": lots,
                "shortTerm": short_term,
                "longTerm": long_term,
                "sixtyFortyTerm": sixty_forty_term,
                "totalProfitLoss": total_profit_loss,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_hstier_2_service_taxlots_api_unrealized_lot_summary import (
            ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotSummary,
        )

        d = dict(src_dict)
        as_of = datetime.date.fromisoformat(d.pop("asOf"))

        lots = []
        _lots = d.pop("lots")
        for lots_item_data in _lots:
            lots_item = ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotSummary.from_dict(
                lots_item_data
            )

            lots.append(lots_item)

        short_term = d.pop("shortTerm")

        long_term = d.pop("longTerm")

        sixty_forty_term = d.pop("sixtyFortyTerm")

        total_profit_loss = d.pop("totalProfitLoss")

        com_hellopublic_hstier_2_service_taxlots_api_unrealized_lots_summary_response = cls(
            as_of=as_of,
            lots=lots,
            short_term=short_term,
            long_term=long_term,
            sixty_forty_term=sixty_forty_term,
            total_profit_loss=total_profit_loss,
        )

        com_hellopublic_hstier_2_service_taxlots_api_unrealized_lots_summary_response.additional_properties = d
        return com_hellopublic_hstier_2_service_taxlots_api_unrealized_lots_summary_response

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
