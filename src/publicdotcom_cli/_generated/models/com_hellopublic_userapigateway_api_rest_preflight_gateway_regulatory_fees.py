from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees:
    """# GatewayRegulatoryFees
    Represents various regulatory fees associated with trading orders.
    <br/>
    ## Fields
    - **secFee** - The SEC charges a regulatory fee for sell orders that execute. The fee is based on the dollar amount
    of the order.
    - **tafFee** - The Trading Activity Fee is a FINRA fee. The fee is based on the order quantity.
    - **orfFee** - The Options Regulatory Fee (ORF). This is the combined exchange fee rate for all exchanges. Changes
    monthly.
    - **exchangeFee** - The exchange charges a fee for executing orders for index options.
    - **occFee** - The Options Clearing Corporation Fee (OCC)
    - **catFee** - The Consolidated Audit Trail Fee (CAT)

        Attributes:
            sec_fee (str | Unset):
            taf_fee (str | Unset):
            orf_fee (str | Unset):
            exchange_fee (str | Unset):
            occ_fee (str | Unset):
            cat_fee (str | Unset):
    """

    sec_fee: str | Unset = UNSET
    taf_fee: str | Unset = UNSET
    orf_fee: str | Unset = UNSET
    exchange_fee: str | Unset = UNSET
    occ_fee: str | Unset = UNSET
    cat_fee: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sec_fee = self.sec_fee

        taf_fee = self.taf_fee

        orf_fee = self.orf_fee

        exchange_fee = self.exchange_fee

        occ_fee = self.occ_fee

        cat_fee = self.cat_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sec_fee is not UNSET:
            field_dict["secFee"] = sec_fee
        if taf_fee is not UNSET:
            field_dict["tafFee"] = taf_fee
        if orf_fee is not UNSET:
            field_dict["orfFee"] = orf_fee
        if exchange_fee is not UNSET:
            field_dict["exchangeFee"] = exchange_fee
        if occ_fee is not UNSET:
            field_dict["occFee"] = occ_fee
        if cat_fee is not UNSET:
            field_dict["catFee"] = cat_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sec_fee = d.pop("secFee", UNSET)

        taf_fee = d.pop("tafFee", UNSET)

        orf_fee = d.pop("orfFee", UNSET)

        exchange_fee = d.pop("exchangeFee", UNSET)

        occ_fee = d.pop("occFee", UNSET)

        cat_fee = d.pop("catFee", UNSET)

        com_hellopublic_userapigateway_api_rest_preflight_gateway_regulatory_fees = cls(
            sec_fee=sec_fee,
            taf_fee=taf_fee,
            orf_fee=orf_fee,
            exchange_fee=exchange_fee,
            occ_fee=occ_fee,
            cat_fee=cat_fee,
        )

        com_hellopublic_userapigateway_api_rest_preflight_gateway_regulatory_fees.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_gateway_regulatory_fees

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
