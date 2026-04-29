from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_impact import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_requirement import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_price_increment import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_regulatory_fees import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_leg_response import (
        ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponse,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegResponse:
    """# PreflightMultiLegResponse
    Response containing estimated costs, fees, and other information needed before placing a multi-leg order.

    ## Fields

    ### Strategy Information
    - **baseSymbol** - The base symbol for the multi-leg strategy (e.g., "TSLA" for Tesla options)
    - **strategyName** - The name of the strategy (e.g., "Call Spread", "Iron Condor")
    - **legs** - List of individual leg details for the strategy

    ### Cost and Fee Information
    - **estimatedCommission** - The estimated commission amount that will be charged if the order executes
    - **regulatoryFees** - Gateway regulatory fees breakdown including SEC, TAF, ORF, OCC, CAT fees
    - **estimatedIndexOptionFee** - Estimated index option fees (if applicable)
    - **estimatedCost** - The total estimated cost including all fees and commissions
    - **buyingPowerRequirement** - The buying power required for this multi-leg order

    ### Order Details
    - **orderValue** - The estimated order value, excluding fees and commission
    - **estimatedQuantity** - The number of strategies that will be executed
    - **estimatedProceeds** - The estimated proceeds from the order (for credit spreads)

    ### Option-Specific Information
    - **marginRequirement** - Margin requirements for the multi-leg strategy
    - **marginImpact** - Impact on account margin usage
    - **priceIncrement** - Price increment information for option orders

        Attributes:
            base_symbol (str):
            legs (list[ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponse]):
            order_value (str):
            strategy_name (str | Unset):
            estimated_commission (str | Unset):
            regulatory_fees (ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees | Unset): #
                GatewayRegulatoryFees
                Represents various regulatory fees associated with trading orders.
                <br/>
                ## Fields
                - **secFee** - The SEC charges a regulatory fee for sell orders that execute. The fee is based on the dollar
                amount of the order.
                - **tafFee** - The Trading Activity Fee is a FINRA fee. The fee is based on the order quantity.
                - **orfFee** - The Options Regulatory Fee (ORF). This is the combined exchange fee rate for all exchanges.
                Changes monthly.
                - **exchangeFee** - The exchange charges a fee for executing orders for index options.
                - **occFee** - The Options Clearing Corporation Fee (OCC)
                - **catFee** - The Consolidated Audit Trail Fee (CAT)
            estimated_index_option_fee (str | Unset):
            estimated_quantity (str | Unset):
            estimated_cost (str | Unset):
            buying_power_requirement (str | Unset):
            estimated_proceeds (str | Unset):
            margin_requirement (ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement | Unset):
            margin_impact (ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact | Unset):
            price_increment (ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement | Unset): Price increment
                information for option orders.
    """

    base_symbol: str
    legs: list[ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponse]
    order_value: str
    strategy_name: str | Unset = UNSET
    estimated_commission: str | Unset = UNSET
    regulatory_fees: ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees | Unset = (
        UNSET
    )
    estimated_index_option_fee: str | Unset = UNSET
    estimated_quantity: str | Unset = UNSET
    estimated_cost: str | Unset = UNSET
    buying_power_requirement: str | Unset = UNSET
    estimated_proceeds: str | Unset = UNSET
    margin_requirement: (
        ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement | Unset
    ) = UNSET
    margin_impact: ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact | Unset = UNSET
    price_increment: ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_symbol = self.base_symbol

        legs = []
        for legs_item_data in self.legs:
            legs_item = legs_item_data.to_dict()
            legs.append(legs_item)

        order_value = self.order_value

        strategy_name = self.strategy_name

        estimated_commission = self.estimated_commission

        regulatory_fees: dict[str, Any] | Unset = UNSET
        if not isinstance(self.regulatory_fees, Unset):
            regulatory_fees = self.regulatory_fees.to_dict()

        estimated_index_option_fee = self.estimated_index_option_fee

        estimated_quantity = self.estimated_quantity

        estimated_cost = self.estimated_cost

        buying_power_requirement = self.buying_power_requirement

        estimated_proceeds = self.estimated_proceeds

        margin_requirement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_requirement, Unset):
            margin_requirement = self.margin_requirement.to_dict()

        margin_impact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_impact, Unset):
            margin_impact = self.margin_impact.to_dict()

        price_increment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price_increment, Unset):
            price_increment = self.price_increment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseSymbol": base_symbol,
                "legs": legs,
                "orderValue": order_value,
            }
        )
        if strategy_name is not UNSET:
            field_dict["strategyName"] = strategy_name
        if estimated_commission is not UNSET:
            field_dict["estimatedCommission"] = estimated_commission
        if regulatory_fees is not UNSET:
            field_dict["regulatoryFees"] = regulatory_fees
        if estimated_index_option_fee is not UNSET:
            field_dict["estimatedIndexOptionFee"] = estimated_index_option_fee
        if estimated_quantity is not UNSET:
            field_dict["estimatedQuantity"] = estimated_quantity
        if estimated_cost is not UNSET:
            field_dict["estimatedCost"] = estimated_cost
        if buying_power_requirement is not UNSET:
            field_dict["buyingPowerRequirement"] = buying_power_requirement
        if estimated_proceeds is not UNSET:
            field_dict["estimatedProceeds"] = estimated_proceeds
        if margin_requirement is not UNSET:
            field_dict["marginRequirement"] = margin_requirement
        if margin_impact is not UNSET:
            field_dict["marginImpact"] = margin_impact
        if price_increment is not UNSET:
            field_dict["priceIncrement"] = price_increment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_impact import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_requirement import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_price_increment import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_regulatory_fees import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_preflight_leg_response import (
            ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponse,
        )

        d = dict(src_dict)
        base_symbol = d.pop("baseSymbol")

        legs = []
        _legs = d.pop("legs")
        for legs_item_data in _legs:
            legs_item = ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponse.from_dict(
                legs_item_data
            )

            legs.append(legs_item)

        order_value = d.pop("orderValue")

        strategy_name = d.pop("strategyName", UNSET)

        estimated_commission = d.pop("estimatedCommission", UNSET)

        _regulatory_fees = d.pop("regulatoryFees", UNSET)
        regulatory_fees: ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees | Unset
        if isinstance(_regulatory_fees, Unset):
            regulatory_fees = UNSET
        else:
            regulatory_fees = (
                ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees.from_dict(
                    _regulatory_fees
                )
            )

        estimated_index_option_fee = d.pop("estimatedIndexOptionFee", UNSET)

        estimated_quantity = d.pop("estimatedQuantity", UNSET)

        estimated_cost = d.pop("estimatedCost", UNSET)

        buying_power_requirement = d.pop("buyingPowerRequirement", UNSET)

        estimated_proceeds = d.pop("estimatedProceeds", UNSET)

        _margin_requirement = d.pop("marginRequirement", UNSET)
        margin_requirement: (
            ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement | Unset
        )
        if isinstance(_margin_requirement, Unset):
            margin_requirement = UNSET
        else:
            margin_requirement = (
                ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement.from_dict(
                    _margin_requirement
                )
            )

        _margin_impact = d.pop("marginImpact", UNSET)
        margin_impact: ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact | Unset
        if isinstance(_margin_impact, Unset):
            margin_impact = UNSET
        else:
            margin_impact = (
                ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact.from_dict(
                    _margin_impact
                )
            )

        _price_increment = d.pop("priceIncrement", UNSET)
        price_increment: ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement | Unset
        if isinstance(_price_increment, Unset):
            price_increment = UNSET
        else:
            price_increment = (
                ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement.from_dict(
                    _price_increment
                )
            )

        com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_response = cls(
            base_symbol=base_symbol,
            legs=legs,
            order_value=order_value,
            strategy_name=strategy_name,
            estimated_commission=estimated_commission,
            regulatory_fees=regulatory_fees,
            estimated_index_option_fee=estimated_index_option_fee,
            estimated_quantity=estimated_quantity,
            estimated_cost=estimated_cost,
            buying_power_requirement=buying_power_requirement,
            estimated_proceeds=estimated_proceeds,
            margin_requirement=margin_requirement,
            margin_impact=margin_impact,
            price_increment=price_increment,
        )

        com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_preflight_multi_leg_response

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
