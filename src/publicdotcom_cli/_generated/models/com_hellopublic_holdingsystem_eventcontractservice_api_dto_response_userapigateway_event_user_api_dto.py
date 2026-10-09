from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_user_api_dto_exchange import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDtoExchange,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_outcome_api_gateway_dto import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDto,
    )
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_cftc_contract_dto import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseCftcContractDto,
    )


T = TypeVar(
    "T",
    bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto",
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto:
    """This is called a "Prediction Event" in the Apex structured API.

    Attributes:
        event_symbol (str): the unique identifier of the event. Example: "KALSHI.KXBALANCESHEET-EO26".
        exchange (ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDtoExchange):
            the exchange that provides the event.
        title (str): the title of the event. Example: "Size of Fed balance sheet at end of 2026".
        category (str): the category of the event. Example: "Economics".
        volume (str): the combined volume of all event contracts within this event.
        subcategories (list[str]): the subcategories/tags related to the event.
        cftc_contract (ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseCftcContractDto):
        outcome_count (int): the unfiltered number of outcomes within the event.
        outcomes
            (list[ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDto]): the
            outcomes of the event that consists of YES/NO event contracts. Might be filtered.
        resolved (bool | Unset): whether the event is resolved/inactive or not.
        halted (bool | Unset): whether trading is halted for all outcomes within the event.
    """

    event_symbol: str
    exchange: ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDtoExchange
    title: str
    category: str
    volume: str
    subcategories: list[str]
    cftc_contract: ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseCftcContractDto
    outcome_count: int
    outcomes: list[
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDto
    ]
    resolved: bool | Unset = UNSET
    halted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_symbol = self.event_symbol

        exchange = self.exchange.value

        title = self.title

        category = self.category

        volume = self.volume

        subcategories = self.subcategories

        cftc_contract = self.cftc_contract.to_dict()

        outcome_count = self.outcome_count

        outcomes = []
        for outcomes_item_data in self.outcomes:
            outcomes_item = outcomes_item_data.to_dict()
            outcomes.append(outcomes_item)

        resolved = self.resolved

        halted = self.halted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventSymbol": event_symbol,
                "exchange": exchange,
                "title": title,
                "category": category,
                "volume": volume,
                "subcategories": subcategories,
                "cftcContract": cftc_contract,
                "outcomeCount": outcome_count,
                "outcomes": outcomes,
            }
        )
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if halted is not UNSET:
            field_dict["halted"] = halted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_outcome_api_gateway_dto import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDto,
        )
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_cftc_contract_dto import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseCftcContractDto,
        )

        d = dict(src_dict)
        event_symbol = d.pop("eventSymbol")

        exchange = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDtoExchange(
            d.pop("exchange")
        )

        title = d.pop("title")

        category = d.pop("category")

        volume = d.pop("volume")

        subcategories = cast(list[str], d.pop("subcategories"))

        cftc_contract = (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseCftcContractDto.from_dict(
                d.pop("cftcContract")
            )
        )

        outcome_count = d.pop("outcomeCount")

        outcomes = []
        _outcomes = d.pop("outcomes")
        for outcomes_item_data in _outcomes:
            outcomes_item = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDto.from_dict(
                outcomes_item_data
            )

            outcomes.append(outcomes_item)

        resolved = d.pop("resolved", UNSET)

        halted = d.pop("halted", UNSET)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_user_api_dto = cls(
            event_symbol=event_symbol,
            exchange=exchange,
            title=title,
            category=category,
            volume=volume,
            subcategories=subcategories,
            cftc_contract=cftc_contract,
            outcome_count=outcome_count,
            outcomes=outcomes,
            resolved=resolved,
            halted=halted,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_user_api_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_userapigateway_event_user_api_dto

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
