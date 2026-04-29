from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_options_greek_response import (
        ComHellopublicUserapigatewayApiRestOptionsGreekResponse,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOptionsGreeksResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOptionsGreeksResponse:
    """
    Attributes:
        greeks (list[ComHellopublicUserapigatewayApiRestOptionsGreekResponse] | Unset): List of greeks for each symbol
            in the request
    """

    greeks: list[ComHellopublicUserapigatewayApiRestOptionsGreekResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        greeks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.greeks, Unset):
            greeks = []
            for greeks_item_data in self.greeks:
                greeks_item = greeks_item_data.to_dict()
                greeks.append(greeks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if greeks is not UNSET:
            field_dict["greeks"] = greeks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_options_greek_response import (
            ComHellopublicUserapigatewayApiRestOptionsGreekResponse,
        )

        d = dict(src_dict)
        _greeks = d.pop("greeks", UNSET)
        greeks: list[ComHellopublicUserapigatewayApiRestOptionsGreekResponse] | Unset = UNSET
        if _greeks is not UNSET:
            greeks = []
            for greeks_item_data in _greeks:
                greeks_item = ComHellopublicUserapigatewayApiRestOptionsGreekResponse.from_dict(
                    greeks_item_data
                )

                greeks.append(greeks_item)

        com_hellopublic_userapigateway_api_rest_options_greeks_response = cls(
            greeks=greeks,
        )

        com_hellopublic_userapigateway_api_rest_options_greeks_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_options_greeks_response

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
