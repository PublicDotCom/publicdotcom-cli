from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_contract_api_gateway_dto_predicted_outcome import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDtoPredictedOutcome,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDto",
)


@_attrs_define
class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDto:
    """
    Attributes:
        symbol (str): the unique identifier of the event contract. Example: "KALSHI.KXBALANCESHEET-EO26-6.6.Y".
        predicted_outcome (ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewa
            yDtoPredictedOutcome): the predicted outcome for this specific contract. YES or NO.
        bid (str | Unset): the bid price.
        ask (str | Unset): the ask price.
        last (str | Unset): the last price.
        open_interest (str | Unset): the open interest.
        daily_gain_value (str | Unset): the daily gain value.
        daily_gain_percentage (str | Unset): the daily gain in percentage.
        probability (str | Unset): is determined by the last price of the YES contract.
            If YES contract, it is the last price.
            If NO contract, it is 1 minus the last price of the YES contract.
    """

    symbol: str
    predicted_outcome: ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDtoPredictedOutcome
    bid: str | Unset = UNSET
    ask: str | Unset = UNSET
    last: str | Unset = UNSET
    open_interest: str | Unset = UNSET
    daily_gain_value: str | Unset = UNSET
    daily_gain_percentage: str | Unset = UNSET
    probability: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        predicted_outcome = self.predicted_outcome.value

        bid = self.bid

        ask = self.ask

        last = self.last

        open_interest = self.open_interest

        daily_gain_value = self.daily_gain_value

        daily_gain_percentage = self.daily_gain_percentage

        probability = self.probability

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "predictedOutcome": predicted_outcome,
            }
        )
        if bid is not UNSET:
            field_dict["bid"] = bid
        if ask is not UNSET:
            field_dict["ask"] = ask
        if last is not UNSET:
            field_dict["last"] = last
        if open_interest is not UNSET:
            field_dict["openInterest"] = open_interest
        if daily_gain_value is not UNSET:
            field_dict["dailyGainValue"] = daily_gain_value
        if daily_gain_percentage is not UNSET:
            field_dict["dailyGainPercentage"] = daily_gain_percentage
        if probability is not UNSET:
            field_dict["probability"] = probability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        predicted_outcome = ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDtoPredictedOutcome(
            d.pop("predictedOutcome")
        )

        bid = d.pop("bid", UNSET)

        ask = d.pop("ask", UNSET)

        last = d.pop("last", UNSET)

        open_interest = d.pop("openInterest", UNSET)

        daily_gain_value = d.pop("dailyGainValue", UNSET)

        daily_gain_percentage = d.pop("dailyGainPercentage", UNSET)

        probability = d.pop("probability", UNSET)

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_contract_api_gateway_dto = cls(
            symbol=symbol,
            predicted_outcome=predicted_outcome,
            bid=bid,
            ask=ask,
            last=last,
            open_interest=open_interest,
            daily_gain_value=daily_gain_value,
            daily_gain_percentage=daily_gain_percentage,
            probability=probability,
        )

        com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_contract_api_gateway_dto.additional_properties = d
        return com_hellopublic_holdingsystem_eventcontractservice_api_dto_response_apigateway_event_contract_api_gateway_dto

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
