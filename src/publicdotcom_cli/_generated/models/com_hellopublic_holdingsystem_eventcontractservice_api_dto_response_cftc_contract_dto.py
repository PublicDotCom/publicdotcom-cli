from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_resolution_source_dto import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseResolutionSourceDto,
    )


T = TypeVar(
    "T", bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseCftcContractDto"
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseCftcContractDto:
    """
    Attributes:
        prohibitions (list[str]): the list of who are not allowed to trade this.
        resolution_sources (list[ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseResolutionSourceDto]): the
            list of resolution sources.
        contract_terms_url (str | Unset): the URL for the contract terms.
    """

    prohibitions: list[str]
    resolution_sources: list[
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseResolutionSourceDto
    ]
    contract_terms_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prohibitions = self.prohibitions

        resolution_sources = []
        for resolution_sources_item_data in self.resolution_sources:
            resolution_sources_item = resolution_sources_item_data.to_dict()
            resolution_sources.append(resolution_sources_item)

        contract_terms_url = self.contract_terms_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prohibitions": prohibitions,
                "resolutionSources": resolution_sources,
            }
        )
        if contract_terms_url is not UNSET:
            field_dict["contractTermsUrl"] = contract_terms_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_resolution_source_dto import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseResolutionSourceDto,
        )

        d = dict(src_dict)
        prohibitions = cast(list[str], d.pop("prohibitions"))

        resolution_sources = []
        _resolution_sources = d.pop("resolutionSources")
        for resolution_sources_item_data in _resolution_sources:
            resolution_sources_item = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseResolutionSourceDto.from_dict(
                resolution_sources_item_data
            )

            resolution_sources.append(resolution_sources_item)

        contract_terms_url = d.pop("contractTermsUrl", UNSET)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_cftc_contract_dto = cls(
            prohibitions=prohibitions,
            resolution_sources=resolution_sources,
            contract_terms_url=contract_terms_url,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_cftc_contract_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_cftc_contract_dto

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
