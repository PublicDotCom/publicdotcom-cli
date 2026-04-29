from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_short_selling import (
        ComHellopublicUserapigatewayApiRestOrderGatewayShortSelling,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_impact import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_requirement import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_option_details import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_option_rebate import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayOptionRebate,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_price_increment import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_regulatory_fees import (
        ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegResponse:
    """# PreflightSingleLegResponse
    Response containing estimated costs, fees, and other information needed before placing a single-leg order.

    ## Fields

    ### Instrument Information
    - **symbol** - The trading symbol for the instrument
    - **cusip** - The CUSIP identifier for the instrument (if applicable)
    - **securityType** - The type of security (EQUITY, OPTION, BOND, etc.)
    - **rootSymbol** - The root symbol for options and other derivatives
    - **rootOptionSymbol** - The root option symbol for option chains

    ### Cost and Fee Information
    - **estimatedCommission** - The estimated commission amount that will be charged if the order executes
    - **regulatoryFees** - The estimated gateway regulatory fees breakdown including SEC, TAF, ORF, OCC, CAT fees
    - **estimatedIndexOptionFee** - The estimated gateway fee when buying index options
    - **estimatedExecutionFee** - The estimated gateway fee when using specific venues for buying stocks
    - **estimatedCost** - The total estimated cost including all fees and commissions
    - **buyingPowerRequirement** - The buying power required for this order

    ### Order Details
    - **orderValue** - The estimated order value, excluding fees and commission
    - **estimatedQuantity** - For quantity orders this is exact, for amount-based orders this is an estimate
    - **estimatedProceeds** - The estimated proceeds from the order (for sell orders)

    ### Option-Specific Information
    - **optionDetails** - Consolidated option-specific details including strike price, expiration, rebates, and fees
    - **priceIncrement** - Price increment information for option orders

    ### Shorting-Specific Information
    - **shortSelling** - Information about short selling rules and fees

        Attributes:
            instrument (ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument):
            order_value (str):
            cusip (str | Unset):
            root_symbol (str | Unset):
            root_option_symbol (str | Unset):
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
            estimated_execution_fee (str | Unset):
            estimated_quantity (str | Unset):
            estimated_cost (str | Unset):
            buying_power_requirement (str | Unset):
            estimated_proceeds (str | Unset):
            option_details (ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails | Unset):
            estimated_order_rebate (ComHellopublicUserapigatewayApiRestPreflightGatewayOptionRebate | Unset):
            margin_requirement (ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement | Unset):
            margin_impact (ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact | Unset):
            short_selling (ComHellopublicUserapigatewayApiRestOrderGatewayShortSelling | Unset): Short-selling information
                for the given instrument.
            price_increment (ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement | Unset): Price increment
                information for option orders.
    """

    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument
    order_value: str
    cusip: str | Unset = UNSET
    root_symbol: str | Unset = UNSET
    root_option_symbol: str | Unset = UNSET
    estimated_commission: str | Unset = UNSET
    regulatory_fees: ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees | Unset = (
        UNSET
    )
    estimated_index_option_fee: str | Unset = UNSET
    estimated_execution_fee: str | Unset = UNSET
    estimated_quantity: str | Unset = UNSET
    estimated_cost: str | Unset = UNSET
    buying_power_requirement: str | Unset = UNSET
    estimated_proceeds: str | Unset = UNSET
    option_details: ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails | Unset = UNSET
    estimated_order_rebate: (
        ComHellopublicUserapigatewayApiRestPreflightGatewayOptionRebate | Unset
    ) = UNSET
    margin_requirement: (
        ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement | Unset
    ) = UNSET
    margin_impact: ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact | Unset = UNSET
    short_selling: ComHellopublicUserapigatewayApiRestOrderGatewayShortSelling | Unset = UNSET
    price_increment: ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument.to_dict()

        order_value = self.order_value

        cusip = self.cusip

        root_symbol = self.root_symbol

        root_option_symbol = self.root_option_symbol

        estimated_commission = self.estimated_commission

        regulatory_fees: dict[str, Any] | Unset = UNSET
        if not isinstance(self.regulatory_fees, Unset):
            regulatory_fees = self.regulatory_fees.to_dict()

        estimated_index_option_fee = self.estimated_index_option_fee

        estimated_execution_fee = self.estimated_execution_fee

        estimated_quantity = self.estimated_quantity

        estimated_cost = self.estimated_cost

        buying_power_requirement = self.buying_power_requirement

        estimated_proceeds = self.estimated_proceeds

        option_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.option_details, Unset):
            option_details = self.option_details.to_dict()

        estimated_order_rebate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_order_rebate, Unset):
            estimated_order_rebate = self.estimated_order_rebate.to_dict()

        margin_requirement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_requirement, Unset):
            margin_requirement = self.margin_requirement.to_dict()

        margin_impact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_impact, Unset):
            margin_impact = self.margin_impact.to_dict()

        short_selling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.short_selling, Unset):
            short_selling = self.short_selling.to_dict()

        price_increment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price_increment, Unset):
            price_increment = self.price_increment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "orderValue": order_value,
            }
        )
        if cusip is not UNSET:
            field_dict["cusip"] = cusip
        if root_symbol is not UNSET:
            field_dict["rootSymbol"] = root_symbol
        if root_option_symbol is not UNSET:
            field_dict["rootOptionSymbol"] = root_option_symbol
        if estimated_commission is not UNSET:
            field_dict["estimatedCommission"] = estimated_commission
        if regulatory_fees is not UNSET:
            field_dict["regulatoryFees"] = regulatory_fees
        if estimated_index_option_fee is not UNSET:
            field_dict["estimatedIndexOptionFee"] = estimated_index_option_fee
        if estimated_execution_fee is not UNSET:
            field_dict["estimatedExecutionFee"] = estimated_execution_fee
        if estimated_quantity is not UNSET:
            field_dict["estimatedQuantity"] = estimated_quantity
        if estimated_cost is not UNSET:
            field_dict["estimatedCost"] = estimated_cost
        if buying_power_requirement is not UNSET:
            field_dict["buyingPowerRequirement"] = buying_power_requirement
        if estimated_proceeds is not UNSET:
            field_dict["estimatedProceeds"] = estimated_proceeds
        if option_details is not UNSET:
            field_dict["optionDetails"] = option_details
        if estimated_order_rebate is not UNSET:
            field_dict["estimatedOrderRebate"] = estimated_order_rebate
        if margin_requirement is not UNSET:
            field_dict["marginRequirement"] = margin_requirement
        if margin_impact is not UNSET:
            field_dict["marginImpact"] = margin_impact
        if short_selling is not UNSET:
            field_dict["shortSelling"] = short_selling
        if price_increment is not UNSET:
            field_dict["priceIncrement"] = price_increment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_short_selling import (
            ComHellopublicUserapigatewayApiRestOrderGatewayShortSelling,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_impact import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayMarginImpact,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_margin_requirement import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayMarginRequirement,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_option_details import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_option_rebate import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayOptionRebate,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_price_increment import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayPriceIncrement,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_preflight_gateway_regulatory_fees import (
            ComHellopublicUserapigatewayApiRestPreflightGatewayRegulatoryFees,
        )

        d = dict(src_dict)
        instrument = ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
            d.pop("instrument")
        )

        order_value = d.pop("orderValue")

        cusip = d.pop("cusip", UNSET)

        root_symbol = d.pop("rootSymbol", UNSET)

        root_option_symbol = d.pop("rootOptionSymbol", UNSET)

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

        estimated_execution_fee = d.pop("estimatedExecutionFee", UNSET)

        estimated_quantity = d.pop("estimatedQuantity", UNSET)

        estimated_cost = d.pop("estimatedCost", UNSET)

        buying_power_requirement = d.pop("buyingPowerRequirement", UNSET)

        estimated_proceeds = d.pop("estimatedProceeds", UNSET)

        _option_details = d.pop("optionDetails", UNSET)
        option_details: ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails | Unset
        if isinstance(_option_details, Unset):
            option_details = UNSET
        else:
            option_details = (
                ComHellopublicUserapigatewayApiRestPreflightGatewayOptionDetails.from_dict(
                    _option_details
                )
            )

        _estimated_order_rebate = d.pop("estimatedOrderRebate", UNSET)
        estimated_order_rebate: (
            ComHellopublicUserapigatewayApiRestPreflightGatewayOptionRebate | Unset
        )
        if isinstance(_estimated_order_rebate, Unset):
            estimated_order_rebate = UNSET
        else:
            estimated_order_rebate = (
                ComHellopublicUserapigatewayApiRestPreflightGatewayOptionRebate.from_dict(
                    _estimated_order_rebate
                )
            )

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

        _short_selling = d.pop("shortSelling", UNSET)
        short_selling: ComHellopublicUserapigatewayApiRestOrderGatewayShortSelling | Unset
        if isinstance(_short_selling, Unset):
            short_selling = UNSET
        else:
            short_selling = ComHellopublicUserapigatewayApiRestOrderGatewayShortSelling.from_dict(
                _short_selling
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

        com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_response = cls(
            instrument=instrument,
            order_value=order_value,
            cusip=cusip,
            root_symbol=root_symbol,
            root_option_symbol=root_option_symbol,
            estimated_commission=estimated_commission,
            regulatory_fees=regulatory_fees,
            estimated_index_option_fee=estimated_index_option_fee,
            estimated_execution_fee=estimated_execution_fee,
            estimated_quantity=estimated_quantity,
            estimated_cost=estimated_cost,
            buying_power_requirement=buying_power_requirement,
            estimated_proceeds=estimated_proceeds,
            option_details=option_details,
            estimated_order_rebate=estimated_order_rebate,
            margin_requirement=margin_requirement,
            margin_impact=margin_impact,
            short_selling=short_selling,
            price_increment=price_increment,
        )

        com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_preflight_preflight_single_leg_response

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
