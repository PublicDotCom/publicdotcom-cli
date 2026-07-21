from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_hstier_2_service_taxlots_api_option_specific_tax_lot_details import (
        ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails,
    )
    from ..models.com_hellopublic_hstier_2_service_taxlots_api_out_of_date_status import (
        ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatus,
    )


T = TypeVar("T", bound="ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotSummary")


@_attrs_define
class ComHellopublicHstier2ServiceTaxlotsApiUnrealizedLotSummary:
    """The lots sorted by openDate

    Attributes:
        account_number (str): Account number
        symbol (str): The ticker
        cusip (str): cusip
        company_name (str): Company name
        quantity (str): The total quantity owned
        cost_basis (str): The costBasis for the lot
        unit_cost (str): The total profit and loss
        current_price (str): The current price. This is calculated once (by Apex) and does not change intraday.
        current_value (str): The current value. This is calculated once (by Apex) and does not change intraday.
        gain_loss (str): The accumulated gain loss for the lots, does not change intraday
        short_term_gain_loss (str): The short term gain/loss including 40% of sixty-forty lots
        long_term_gain_loss (str): The long term gain/loss including 60% of sixty-forty lots
        details (ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails | Unset):
        lot_selection_id (str | Unset): Identifies the tax lot for selection for tax lot selling, `null` if it cannot be
            selected

            This can happen if the lot refers to a symbol undergoing a corporate action, or if the tax lot represents
            a position we did not get from Apex but deduced from the trade history on the account.

            Also, lot selection id can only ever be present if the lot summary refer to one specific lot.
        out_of_date_status (ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatus | Unset): Describes how an unrealized
            lot is out of date
    """

    account_number: str
    symbol: str
    cusip: str
    company_name: str
    quantity: str
    cost_basis: str
    unit_cost: str
    current_price: str
    current_value: str
    gain_loss: str
    short_term_gain_loss: str
    long_term_gain_loss: str
    details: ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails | Unset = UNSET
    lot_selection_id: str | Unset = UNSET
    out_of_date_status: ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        symbol = self.symbol

        cusip = self.cusip

        company_name = self.company_name

        quantity = self.quantity

        cost_basis = self.cost_basis

        unit_cost = self.unit_cost

        current_price = self.current_price

        current_value = self.current_value

        gain_loss = self.gain_loss

        short_term_gain_loss = self.short_term_gain_loss

        long_term_gain_loss = self.long_term_gain_loss

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        lot_selection_id = self.lot_selection_id

        out_of_date_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.out_of_date_status, Unset):
            out_of_date_status = self.out_of_date_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountNumber": account_number,
                "symbol": symbol,
                "cusip": cusip,
                "companyName": company_name,
                "quantity": quantity,
                "costBasis": cost_basis,
                "unitCost": unit_cost,
                "currentPrice": current_price,
                "currentValue": current_value,
                "gainLoss": gain_loss,
                "shortTermGainLoss": short_term_gain_loss,
                "longTermGainLoss": long_term_gain_loss,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if lot_selection_id is not UNSET:
            field_dict["lotSelectionId"] = lot_selection_id
        if out_of_date_status is not UNSET:
            field_dict["outOfDateStatus"] = out_of_date_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_hstier_2_service_taxlots_api_option_specific_tax_lot_details import (
            ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails,
        )
        from ..models.com_hellopublic_hstier_2_service_taxlots_api_out_of_date_status import (
            ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatus,
        )

        d = dict(src_dict)
        account_number = d.pop("accountNumber")

        symbol = d.pop("symbol")

        cusip = d.pop("cusip")

        company_name = d.pop("companyName")

        quantity = d.pop("quantity")

        cost_basis = d.pop("costBasis")

        unit_cost = d.pop("unitCost")

        current_price = d.pop("currentPrice")

        current_value = d.pop("currentValue")

        gain_loss = d.pop("gainLoss")

        short_term_gain_loss = d.pop("shortTermGainLoss")

        long_term_gain_loss = d.pop("longTermGainLoss")

        _details = d.pop("details", UNSET)
        details: ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetails.from_dict(
                _details
            )

        lot_selection_id = d.pop("lotSelectionId", UNSET)

        _out_of_date_status = d.pop("outOfDateStatus", UNSET)
        out_of_date_status: ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatus | Unset
        if isinstance(_out_of_date_status, Unset):
            out_of_date_status = UNSET
        else:
            out_of_date_status = ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatus.from_dict(
                _out_of_date_status
            )

        com_hellopublic_hstier_2_service_taxlots_api_unrealized_lot_summary = cls(
            account_number=account_number,
            symbol=symbol,
            cusip=cusip,
            company_name=company_name,
            quantity=quantity,
            cost_basis=cost_basis,
            unit_cost=unit_cost,
            current_price=current_price,
            current_value=current_value,
            gain_loss=gain_loss,
            short_term_gain_loss=short_term_gain_loss,
            long_term_gain_loss=long_term_gain_loss,
            details=details,
            lot_selection_id=lot_selection_id,
            out_of_date_status=out_of_date_status,
        )

        com_hellopublic_hstier_2_service_taxlots_api_unrealized_lot_summary.additional_properties = d
        return com_hellopublic_hstier_2_service_taxlots_api_unrealized_lot_summary

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
