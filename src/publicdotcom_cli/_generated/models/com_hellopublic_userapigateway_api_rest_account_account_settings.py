from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_account_account_settings_account_type import (
    ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType,
)
from ..models.com_hellopublic_userapigateway_api_rest_account_account_settings_brokerage_account_type import (
    ComHellopublicUserapigatewayApiRestAccountAccountSettingsBrokerageAccountType,
)
from ..models.com_hellopublic_userapigateway_api_rest_account_account_settings_options_level import (
    ComHellopublicUserapigatewayApiRestAccountAccountSettingsOptionsLevel,
)
from ..models.com_hellopublic_userapigateway_api_rest_account_account_settings_trade_permissions import (
    ComHellopublicUserapigatewayApiRestAccountAccountSettingsTradePermissions,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestAccountAccountSettings")


@_attrs_define
class ComHellopublicUserapigatewayApiRestAccountAccountSettings:
    """
    Attributes:
        account_id (str | Unset):
        account_type (ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType | Unset):
        options_level (ComHellopublicUserapigatewayApiRestAccountAccountSettingsOptionsLevel | Unset):
        brokerage_account_type (ComHellopublicUserapigatewayApiRestAccountAccountSettingsBrokerageAccountType | Unset):
        trade_permissions (ComHellopublicUserapigatewayApiRestAccountAccountSettingsTradePermissions | Unset):
    """

    account_id: str | Unset = UNSET
    account_type: ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType | Unset = (
        UNSET
    )
    options_level: ComHellopublicUserapigatewayApiRestAccountAccountSettingsOptionsLevel | Unset = (
        UNSET
    )
    brokerage_account_type: (
        ComHellopublicUserapigatewayApiRestAccountAccountSettingsBrokerageAccountType | Unset
    ) = UNSET
    trade_permissions: (
        ComHellopublicUserapigatewayApiRestAccountAccountSettingsTradePermissions | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        options_level: str | Unset = UNSET
        if not isinstance(self.options_level, Unset):
            options_level = self.options_level.value

        brokerage_account_type: str | Unset = UNSET
        if not isinstance(self.brokerage_account_type, Unset):
            brokerage_account_type = self.brokerage_account_type.value

        trade_permissions: str | Unset = UNSET
        if not isinstance(self.trade_permissions, Unset):
            trade_permissions = self.trade_permissions.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if options_level is not UNSET:
            field_dict["optionsLevel"] = options_level
        if brokerage_account_type is not UNSET:
            field_dict["brokerageAccountType"] = brokerage_account_type
        if trade_permissions is not UNSET:
            field_dict["tradePermissions"] = trade_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType(
                _account_type
            )

        _options_level = d.pop("optionsLevel", UNSET)
        options_level: ComHellopublicUserapigatewayApiRestAccountAccountSettingsOptionsLevel | Unset
        if isinstance(_options_level, Unset):
            options_level = UNSET
        else:
            options_level = ComHellopublicUserapigatewayApiRestAccountAccountSettingsOptionsLevel(
                _options_level
            )

        _brokerage_account_type = d.pop("brokerageAccountType", UNSET)
        brokerage_account_type: (
            ComHellopublicUserapigatewayApiRestAccountAccountSettingsBrokerageAccountType | Unset
        )
        if isinstance(_brokerage_account_type, Unset):
            brokerage_account_type = UNSET
        else:
            brokerage_account_type = (
                ComHellopublicUserapigatewayApiRestAccountAccountSettingsBrokerageAccountType(
                    _brokerage_account_type
                )
            )

        _trade_permissions = d.pop("tradePermissions", UNSET)
        trade_permissions: (
            ComHellopublicUserapigatewayApiRestAccountAccountSettingsTradePermissions | Unset
        )
        if isinstance(_trade_permissions, Unset):
            trade_permissions = UNSET
        else:
            trade_permissions = (
                ComHellopublicUserapigatewayApiRestAccountAccountSettingsTradePermissions(
                    _trade_permissions
                )
            )

        com_hellopublic_userapigateway_api_rest_account_account_settings = cls(
            account_id=account_id,
            account_type=account_type,
            options_level=options_level,
            brokerage_account_type=brokerage_account_type,
            trade_permissions=trade_permissions,
        )

        com_hellopublic_userapigateway_api_rest_account_account_settings.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_account_account_settings

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
