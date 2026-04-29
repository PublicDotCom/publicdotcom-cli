from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsCrypto"
)


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsCrypto:
    """
    Attributes:
        payload_type (str):
        crypto_quantity_precision (int | Unset):
        crypto_price_precision (int | Unset):
        tradable_in_new_york (bool | Unset):
    """

    payload_type: str
    crypto_quantity_precision: int | Unset = UNSET
    crypto_price_precision: int | Unset = UNSET
    tradable_in_new_york: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload_type = self.payload_type

        crypto_quantity_precision = self.crypto_quantity_precision

        crypto_price_precision = self.crypto_price_precision

        tradable_in_new_york = self.tradable_in_new_york

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payloadType": payload_type,
            }
        )
        if crypto_quantity_precision is not UNSET:
            field_dict["cryptoQuantityPrecision"] = crypto_quantity_precision
        if crypto_price_precision is not UNSET:
            field_dict["cryptoPricePrecision"] = crypto_price_precision
        if tradable_in_new_york is not UNSET:
            field_dict["tradableInNewYork"] = tradable_in_new_york

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payload_type = d.pop("payloadType")

        crypto_quantity_precision = d.pop("cryptoQuantityPrecision", UNSET)

        crypto_price_precision = d.pop("cryptoPricePrecision", UNSET)

        tradable_in_new_york = d.pop("tradableInNewYork", UNSET)

        com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_crypto = cls(
            payload_type=payload_type,
            crypto_quantity_precision=crypto_quantity_precision,
            crypto_price_precision=crypto_price_precision,
            tradable_in_new_york=tradable_in_new_york,
        )

        com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_crypto.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_crypto

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
