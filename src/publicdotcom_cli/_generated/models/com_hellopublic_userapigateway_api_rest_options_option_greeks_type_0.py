from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOptionsOptionGreeksType0:
    """
    Attributes:
        delta (str | Unset): Delta is the theoretical estimate of how much an option's value may change given a $1 move
            UP or DOWN in the underlying security.
            The Delta values range from -1 to +1, with 0 representing an option where the premium barely moves relative to
            price changes in the underlying stock.
        gamma (str | Unset): Gamma represents the rate of change between an option's Delta and the underlying asset's
            price.
            Higher Gamma values indicate that the Delta could change dramatically with even very small price changes in the
            underlying stock or fund.
        theta (str | Unset): Theta represents the rate of change between the option price and time, or time
            sensitivity—sometimes known as an option's time decay.
            Theta indicates the amount an option's price would decrease as the time to expiration decreases, all else equal.
        vega (str | Unset): Vega measures the amount of increase or decrease in an option premium based on a 1% change
            in implied volatility.
        rho (str | Unset): Rho represents the rate of change between an option's value and a 1% change in the interest
            rate. This measures sensitivity to the interest rate.
        implied_volatility (str | Unset): Implied volatility (IV) is a theoretical forecast of how volatile an
            underlying stock is expected to be in the future.
    """

    delta: str | Unset = UNSET
    gamma: str | Unset = UNSET
    theta: str | Unset = UNSET
    vega: str | Unset = UNSET
    rho: str | Unset = UNSET
    implied_volatility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delta = self.delta

        gamma = self.gamma

        theta = self.theta

        vega = self.vega

        rho = self.rho

        implied_volatility = self.implied_volatility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delta is not UNSET:
            field_dict["delta"] = delta
        if gamma is not UNSET:
            field_dict["gamma"] = gamma
        if theta is not UNSET:
            field_dict["theta"] = theta
        if vega is not UNSET:
            field_dict["vega"] = vega
        if rho is not UNSET:
            field_dict["rho"] = rho
        if implied_volatility is not UNSET:
            field_dict["impliedVolatility"] = implied_volatility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delta = d.pop("delta", UNSET)

        gamma = d.pop("gamma", UNSET)

        theta = d.pop("theta", UNSET)

        vega = d.pop("vega", UNSET)

        rho = d.pop("rho", UNSET)

        implied_volatility = d.pop("impliedVolatility", UNSET)

        com_hellopublic_userapigateway_api_rest_options_option_greeks_type_0 = cls(
            delta=delta,
            gamma=gamma,
            theta=theta,
            vega=vega,
            rho=rho,
            implied_volatility=implied_volatility,
        )

        com_hellopublic_userapigateway_api_rest_options_option_greeks_type_0.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_options_option_greeks_type_0

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
