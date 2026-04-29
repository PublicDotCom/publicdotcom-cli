from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_account_account_settings import (
        ComHellopublicUserapigatewayApiRestAccountAccountSettings,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse")


@_attrs_define
class ComHellopublicUserapigatewayApiRestAccountAccountSettingsResponse:
    """
    Attributes:
        accounts (list[ComHellopublicUserapigatewayApiRestAccountAccountSettings] | Unset):
    """

    accounts: list[ComHellopublicUserapigatewayApiRestAccountAccountSettings] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_account_account_settings import (
            ComHellopublicUserapigatewayApiRestAccountAccountSettings,
        )

        d = dict(src_dict)
        _accounts = d.pop("accounts", UNSET)
        accounts: list[ComHellopublicUserapigatewayApiRestAccountAccountSettings] | Unset = UNSET
        if _accounts is not UNSET:
            accounts = []
            for accounts_item_data in _accounts:
                accounts_item = ComHellopublicUserapigatewayApiRestAccountAccountSettings.from_dict(
                    accounts_item_data
                )

                accounts.append(accounts_item)

        com_hellopublic_userapigateway_api_rest_account_account_settings_response = cls(
            accounts=accounts,
        )

        com_hellopublic_userapigateway_api_rest_account_account_settings_response.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_account_account_settings_response

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
