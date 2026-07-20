from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar(
    "T", bound="ComHellopublicUserapigatewayApiRestPortfolioGatewayAvailableToWithdrawType0"
)


@_attrs_define
class ComHellopublicUserapigatewayApiRestPortfolioGatewayAvailableToWithdrawType0:
    """Available to withdraw summary

    Attributes:
        cash_only_available_to_withdraw (str): Available to withdraw on cash only. If the account does not have margin
            investing enabled, then this is the same as availableToWithdraw.
        available_to_withdraw (str): Total amount available to withdraw.
    """

    cash_only_available_to_withdraw: str
    available_to_withdraw: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cash_only_available_to_withdraw = self.cash_only_available_to_withdraw

        available_to_withdraw = self.available_to_withdraw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cashOnlyAvailableToWithdraw": cash_only_available_to_withdraw,
                "availableToWithdraw": available_to_withdraw,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cash_only_available_to_withdraw = d.pop("cashOnlyAvailableToWithdraw")

        available_to_withdraw = d.pop("availableToWithdraw")

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_available_to_withdraw_type_0 = (
            cls(
                cash_only_available_to_withdraw=cash_only_available_to_withdraw,
                available_to_withdraw=available_to_withdraw,
            )
        )

        com_hellopublic_userapigateway_api_rest_portfolio_gateway_available_to_withdraw_type_0.additional_properties = d
        return (
            com_hellopublic_userapigateway_api_rest_portfolio_gateway_available_to_withdraw_type_0
        )

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
