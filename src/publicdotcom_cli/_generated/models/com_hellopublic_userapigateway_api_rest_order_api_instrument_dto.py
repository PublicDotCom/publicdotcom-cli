from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_order_api_instrument_dto_fractional_trading import (
    ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoFractionalTrading,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_api_instrument_dto_option_spread_trading import (
    ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionSpreadTrading,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_api_instrument_dto_option_trading import (
    ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionTrading,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_api_instrument_dto_shorting_availability import (
    ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoShortingAvailability,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_api_instrument_dto_trading import (
    ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoTrading,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_holdingsystem_core_types_option_price_increment import (
        ComHellopublicHoldingsystemCoreTypesOptionPriceIncrement,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_bond import (
        ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond,
    )
    from ..models.com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_crypto import (
        ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsCrypto,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderApiInstrumentDto:
    """
    Attributes:
        instrument (ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument):
        trading (ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoTrading):
        fractional_trading (ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoFractionalTrading):
        option_trading (ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionTrading):
        option_spread_trading (ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionSpreadTrading):
        instrument_details (ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond |
            ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsCrypto | Unset):
        shorting_availability (ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoShortingAvailability | Unset):
            The short-selling availability.
        hard_to_borrow_percentage_rate (str | Unset): The hard to borrow rate as a percentage value.
        option_contract_price_increments (ComHellopublicHoldingsystemCoreTypesOptionPriceIncrement | Unset): Record
            representing price increments below and above $3.
    """

    instrument: ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument
    trading: ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoTrading
    fractional_trading: ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoFractionalTrading
    option_trading: ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionTrading
    option_spread_trading: (
        ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionSpreadTrading
    )
    instrument_details: (
        ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond
        | ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsCrypto
        | Unset
    ) = UNSET
    shorting_availability: (
        ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoShortingAvailability | Unset
    ) = UNSET
    hard_to_borrow_percentage_rate: str | Unset = UNSET
    option_contract_price_increments: (
        ComHellopublicHoldingsystemCoreTypesOptionPriceIncrement | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_bond import (
            ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond,
        )

        instrument = self.instrument.to_dict()

        trading = self.trading.value

        fractional_trading = self.fractional_trading.value

        option_trading = self.option_trading.value

        option_spread_trading = self.option_spread_trading.value

        instrument_details: dict[str, Any] | Unset
        if isinstance(self.instrument_details, Unset):
            instrument_details = UNSET
        elif isinstance(
            self.instrument_details,
            ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond,
        ):
            instrument_details = self.instrument_details.to_dict()
        else:
            instrument_details = self.instrument_details.to_dict()

        shorting_availability: str | Unset = UNSET
        if not isinstance(self.shorting_availability, Unset):
            shorting_availability = self.shorting_availability.value

        hard_to_borrow_percentage_rate = self.hard_to_borrow_percentage_rate

        option_contract_price_increments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.option_contract_price_increments, Unset):
            option_contract_price_increments = self.option_contract_price_increments.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "trading": trading,
                "fractionalTrading": fractional_trading,
                "optionTrading": option_trading,
                "optionSpreadTrading": option_spread_trading,
            }
        )
        if instrument_details is not UNSET:
            field_dict["instrumentDetails"] = instrument_details
        if shorting_availability is not UNSET:
            field_dict["shortingAvailability"] = shorting_availability
        if hard_to_borrow_percentage_rate is not UNSET:
            field_dict["hardToBorrowPercentageRate"] = hard_to_borrow_percentage_rate
        if option_contract_price_increments is not UNSET:
            field_dict["optionContractPriceIncrements"] = option_contract_price_increments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_holdingsystem_core_types_option_price_increment import (
            ComHellopublicHoldingsystemCoreTypesOptionPriceIncrement,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_bond import (
            ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond,
        )
        from ..models.com_hellopublic_userapigateway_api_rest_order_instrumentdetails_api_instrument_details_crypto import (
            ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsCrypto,
        )

        d = dict(src_dict)
        instrument = ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
            d.pop("instrument")
        )

        trading = ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoTrading(d.pop("trading"))

        fractional_trading = (
            ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoFractionalTrading(
                d.pop("fractionalTrading")
            )
        )

        option_trading = ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionTrading(
            d.pop("optionTrading")
        )

        option_spread_trading = (
            ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionSpreadTrading(
                d.pop("optionSpreadTrading")
            )
        )

        def _parse_instrument_details(
            data: object,
        ) -> (
            ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond
            | ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsCrypto
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instrument_details_type_0 = ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsBond.from_dict(
                    data
                )

                return instrument_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            instrument_details_type_1 = ComHellopublicUserapigatewayApiRestOrderInstrumentdetailsApiInstrumentDetailsCrypto.from_dict(
                data
            )

            return instrument_details_type_1

        instrument_details = _parse_instrument_details(d.pop("instrumentDetails", UNSET))

        _shorting_availability = d.pop("shortingAvailability", UNSET)
        shorting_availability: (
            ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoShortingAvailability | Unset
        )
        if isinstance(_shorting_availability, Unset):
            shorting_availability = UNSET
        else:
            shorting_availability = (
                ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoShortingAvailability(
                    _shorting_availability
                )
            )

        hard_to_borrow_percentage_rate = d.pop("hardToBorrowPercentageRate", UNSET)

        _option_contract_price_increments = d.pop("optionContractPriceIncrements", UNSET)
        option_contract_price_increments: (
            ComHellopublicHoldingsystemCoreTypesOptionPriceIncrement | Unset
        )
        if isinstance(_option_contract_price_increments, Unset):
            option_contract_price_increments = UNSET
        else:
            option_contract_price_increments = (
                ComHellopublicHoldingsystemCoreTypesOptionPriceIncrement.from_dict(
                    _option_contract_price_increments
                )
            )

        com_hellopublic_userapigateway_api_rest_order_api_instrument_dto = cls(
            instrument=instrument,
            trading=trading,
            fractional_trading=fractional_trading,
            option_trading=option_trading,
            option_spread_trading=option_spread_trading,
            instrument_details=instrument_details,
            shorting_availability=shorting_availability,
            hard_to_borrow_percentage_rate=hard_to_borrow_percentage_rate,
            option_contract_price_increments=option_contract_price_increments,
        )

        com_hellopublic_userapigateway_api_rest_order_api_instrument_dto.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_api_instrument_dto

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
