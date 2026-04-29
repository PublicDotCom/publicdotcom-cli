from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_options_option_greeks_type_0 import (
        ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOptionsGreekResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOptionsGreekResponse:
    """
    Attributes:
        symbol (str): The OSI-normalized format of the option symbol
        greeks (ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0 | None | Unset):
    """

    symbol: str
    greeks: ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.com_hellopublic_userapigateway_api_rest_options_option_greeks_type_0 import (
            ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0,
        )

        symbol = self.symbol

        greeks: dict[str, Any] | None | Unset
        if isinstance(self.greeks, Unset):
            greeks = UNSET
        elif isinstance(self.greeks, ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0):
            greeks = self.greeks.to_dict()
        else:
            greeks = self.greeks

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
        from ..models.com_hellopublic_userapigateway_api_rest_options_option_greeks_type_0 import (
            ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0,
        )

        d = dict(src_dict)
        symbol = d.pop("symbol")

        def _parse_greeks(
            data: object,
        ) -> ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascom_hellopublic_userapigateway_api_rest_options_option_greeks_type_0 = ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0.from_dict(
                    data
                )

                return componentsschemascom_hellopublic_userapigateway_api_rest_options_option_greeks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0 | None | Unset, data
            )

        greeks = _parse_greeks(d.pop("greeks", UNSET))

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
