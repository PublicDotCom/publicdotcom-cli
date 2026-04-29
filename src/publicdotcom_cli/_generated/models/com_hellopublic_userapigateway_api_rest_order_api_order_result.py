from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderApiOrderResult")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderApiOrderResult:
    """
    Attributes:
        order_id (UUID | Unset):
    """

    order_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id: str | Unset = UNSET
        if not isinstance(self.order_id, Unset):
            order_id = str(self.order_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["orderId"] = order_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _order_id = d.pop("orderId", UNSET)
        order_id: UUID | Unset
        if isinstance(_order_id, Unset):
            order_id = UNSET
        else:
            order_id = UUID(_order_id)

        com_hellopublic_userapigateway_api_rest_order_api_order_result = cls(
            order_id=order_id,
        )

        com_hellopublic_userapigateway_api_rest_order_api_order_result.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_api_order_result

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
