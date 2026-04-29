from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_api_instrument_dto import (
        ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderApiInstrumentResponse:
    """
    Attributes:
        instruments (list[ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto] | Unset):
    """

    instruments: list[ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instruments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instruments, Unset):
            instruments = []
            for instruments_item_data in self.instruments:
                instruments_item = instruments_item_data.to_dict()
                instruments.append(instruments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instruments is not UNSET:
            field_dict["instruments"] = instruments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_api_instrument_dto import (
            ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto,
        )

        d = dict(src_dict)
        _instruments = d.pop("instruments", UNSET)
        instruments: list[ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto] | Unset = UNSET
        if _instruments is not UNSET:
            instruments = []
            for instruments_item_data in _instruments:
                instruments_item = (
                    ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto.from_dict(
                        instruments_item_data
                    )
                )

                instruments.append(instruments_item)

        com_hellopublic_userapigateway_api_rest_order_api_instrument_response = cls(
            instruments=instruments,
        )

        com_hellopublic_userapigateway_api_rest_order_api_instrument_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_api_instrument_response

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
