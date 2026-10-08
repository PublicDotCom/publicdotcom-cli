from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_outcome_api_gateway_dto_settled_outcome import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoSettledOutcome,
)
from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_outcome_api_gateway_dto_state import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoState,
)
from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_outcome_api_gateway_dto_trading import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoTrading,
)

if TYPE_CHECKING:
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_contract_api_gateway_dto import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDto,
    )
    from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_timeline_api_gateway_dto import (
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventTimelineApiGatewayDto,
    )


T = TypeVar(
    "T",
    bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDto",
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDto:
    """
    Attributes:
        outcome_id (str): the unique identifier for the event outcome. Example: "KALSHI.KXBALANCESHEET-EO26-6.6".
        title (str): the title/subtitle of the outcome. Example: "ABOVE $6.6 TRILLION".
        rules (str): the rules of the outcome that describes the conditions for the outcome to be resolved to YES.
        volume (str): the combined volume of all event contracts within this outcome.
        state (ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoState):
            the state of the outcome and the event contracts within it.
        timeline (ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventTimelineApiGatewayDto):
        settled_outcome (ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDt
            oSettledOutcome): the settled outcome. Either YES or NO.
        trading
            (ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoTrading):
        contracts
            (list[ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDto]): the
            YES and NO event contracts within the outcome.
    """

    outcome_id: str
    title: str
    rules: str
    volume: str
    state: ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoState
    timeline: ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventTimelineApiGatewayDto
    settled_outcome: ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoSettledOutcome
    trading: ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoTrading
    contracts: list[
        ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDto
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outcome_id = self.outcome_id

        title = self.title

        rules = self.rules

        volume = self.volume

        state = self.state.value

        timeline = self.timeline.to_dict()

        settled_outcome = self.settled_outcome.value

        trading = self.trading.value

        contracts = []
        for contracts_item_data in self.contracts:
            contracts_item = contracts_item_data.to_dict()
            contracts.append(contracts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outcomeId": outcome_id,
                "title": title,
                "rules": rules,
                "volume": volume,
                "state": state,
                "timeline": timeline,
                "settledOutcome": settled_outcome,
                "trading": trading,
                "contracts": contracts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_contract_api_gateway_dto import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDto,
        )
        from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_timeline_api_gateway_dto import (
            ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventTimelineApiGatewayDto,
        )

        d = dict(src_dict)
        outcome_id = d.pop("outcomeId")

        title = d.pop("title")

        rules = d.pop("rules")

        volume = d.pop("volume")

        state = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoState(
            d.pop("state")
        )

        timeline = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventTimelineApiGatewayDto.from_dict(
            d.pop("timeline")
        )

        settled_outcome = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoSettledOutcome(
            d.pop("settledOutcome")
        )

        trading = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoTrading(
            d.pop("trading")
        )

        contracts = []
        _contracts = d.pop("contracts")
        for contracts_item_data in _contracts:
            contracts_item = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDto.from_dict(
                contracts_item_data
            )

            contracts.append(contracts_item)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_outcome_api_gateway_dto = cls(
            outcome_id=outcome_id,
            title=title,
            rules=rules,
            volume=volume,
            state=state,
            timeline=timeline,
            settled_outcome=settled_outcome,
            trading=trading,
            contracts=contracts,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_outcome_api_gateway_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_outcome_api_gateway_dto

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
