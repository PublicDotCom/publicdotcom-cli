from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_options_option_greeks import (
        ComHellopublicUserapigatewayApiRestOptionsOptionGreeks,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOptionsGreekResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOptionsGreekResponse:
    """
    Attributes:
        symbol (str): The OSI-normalized format of the option symbol
        greeks (ComHellopublicUserapigatewayApiRestOptionsOptionGreeks | Unset):
    """

    symbol: str
    greeks: ComHellopublicUserapigatewayApiRestOptionsOptionGreeks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        greeks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.greeks, Unset):
            greeks = self.greeks.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
            }
        )
        if greeks is not UNSET:
            field_dict["greeks"] = greeks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_options_option_greeks import (
            ComHellopublicUserapigatewayApiRestOptionsOptionGreeks,
        )

        d = dict(src_dict)
        symbol = d.pop("symbol")

        _greeks = d.pop("greeks", UNSET)
        greeks: ComHellopublicUserapigatewayApiRestOptionsOptionGreeks | Unset
        if isinstance(_greeks, Unset):
            greeks = UNSET
        else:
            greeks = ComHellopublicUserapigatewayApiRestOptionsOptionGreeks.from_dict(_greeks)

        com_hellopublic_userapigateway_api_rest_options_greek_response = cls(
            symbol=symbol,
            greeks=greeks,
        )

        com_hellopublic_userapigateway_api_rest_options_greek_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_options_greek_response

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
