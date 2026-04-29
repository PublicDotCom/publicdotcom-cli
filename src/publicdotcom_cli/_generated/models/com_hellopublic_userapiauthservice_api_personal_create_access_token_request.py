from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest")


@_attrs_define
class ComHellopublicUserapiauthserviceApiPersonalCreateAccessTokenRequest:
    """
    Attributes:
        secret (str): A valid personal secret
        validity_in_minutes (int | None | Unset): Validity of the access token to be issued in minutes. Defaults to 15
            minutes.
    """

    secret: str
    validity_in_minutes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        validity_in_minutes: int | None | Unset
        if isinstance(self.validity_in_minutes, Unset):
            validity_in_minutes = UNSET
        else:
            validity_in_minutes = self.validity_in_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
            }
        )
        if validity_in_minutes is not UNSET:
            field_dict["validityInMinutes"] = validity_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret = d.pop("secret")

        def _parse_validity_in_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        validity_in_minutes = _parse_validity_in_minutes(d.pop("validityInMinutes", UNSET))

        com_hellopublic_userapiauthservice_api_personal_create_access_token_request = cls(
            secret=secret,
            validity_in_minutes=validity_in_minutes,
        )

        com_hellopublic_userapiauthservice_api_personal_create_access_token_request.additional_properties = d
        return com_hellopublic_userapiauthservice_api_personal_create_access_token_request

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
