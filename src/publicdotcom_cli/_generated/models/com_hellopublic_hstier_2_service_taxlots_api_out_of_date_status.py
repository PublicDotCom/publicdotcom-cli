from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_hstier_2_service_taxlots_api_out_of_date_status_type import (
    ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_hstier_2_service_taxlots_api_order_reference import (
        ComHellopublicHstier2ServiceTaxlotsApiOrderReference,
    )
    from ..models.com_hellopublic_hstier_2_service_taxlots_api_out_of_date_status_description import (
        ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusDescription,
    )


T = TypeVar("T", bound="ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatus")


@_attrs_define
class ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatus:
    """Describes how an unrealized lot is out of date

    Attributes:
        type_ (ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusType): The tax lot status type describes how the tax
            lot is not up-to-date
        order (ComHellopublicHstier2ServiceTaxlotsApiOrderReference | Unset): Reference to an order
        description (ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusDescription | Unset): Human-readable
            description of the tax lot status
    """

    type_: ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusType
    order: ComHellopublicHstier2ServiceTaxlotsApiOrderReference | Unset = UNSET
    description: ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusDescription | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        order: dict[str, Any] | Unset = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_hstier_2_service_taxlots_api_order_reference import (
            ComHellopublicHstier2ServiceTaxlotsApiOrderReference,
        )
        from ..models.com_hellopublic_hstier_2_service_taxlots_api_out_of_date_status_description import (
            ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusDescription,
        )

        d = dict(src_dict)
        type_ = ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusType(d.pop("type"))

        _order = d.pop("order", UNSET)
        order: ComHellopublicHstier2ServiceTaxlotsApiOrderReference | Unset
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = ComHellopublicHstier2ServiceTaxlotsApiOrderReference.from_dict(_order)

        _description = d.pop("description", UNSET)
        description: ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusDescription | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = (
                ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusDescription.from_dict(
                    _description
                )
            )

        com_hellopublic_hstier_2_service_taxlots_api_out_of_date_status = cls(
            type_=type_,
            order=order,
            description=description,
        )

        com_hellopublic_hstier_2_service_taxlots_api_out_of_date_status.additional_properties = d
        return com_hellopublic_hstier_2_service_taxlots_api_out_of_date_status

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
