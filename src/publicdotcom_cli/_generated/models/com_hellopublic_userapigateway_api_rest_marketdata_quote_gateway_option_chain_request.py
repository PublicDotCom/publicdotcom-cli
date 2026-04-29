from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )


T = TypeVar(
    "T", bound="ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest"
)


@_attrs_define
class ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayOptionChainRequest:
    """
    Attributes:
        instrument (ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument):
        expiration_date (datetime.date): The expiration date of the option chain.
    """

    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument
    expiration_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument.to_dict()

        expiration_date = self.expiration_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "expirationDate": expiration_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )

        d = dict(src_dict)
        instrument = ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
            d.pop("instrument")
        )

        expiration_date = isoparse(d.pop("expirationDate")).date()

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_chain_request = cls(
            instrument=instrument,
            expiration_date=expiration_date,
        )

        com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_chain_request.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_marketdata_quote_gateway_option_chain_request

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
