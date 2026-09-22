from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.com_hellopublic_userapigateway_api_rest_order_api_query_orders_request_open_close_indicator import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestOpenCloseIndicator,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_api_query_orders_request_security_type import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSecurityType,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_api_query_orders_request_side import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSide,
)
from ..models.com_hellopublic_userapigateway_api_rest_order_api_query_orders_request_status import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
        ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest")


@_attrs_define
class ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest:
    """
    Attributes:
        status (ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestStatus | Unset):
        created_after (datetime.datetime | Unset):
        created_before (datetime.datetime | Unset):
        instruments (list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument] | Unset):
        side (ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSide | Unset):
        open_close_indicator (ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestOpenCloseIndicator | Unset):
        security_type (ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSecurityType | Unset):
    """

    status: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestStatus | Unset = UNSET
    created_after: datetime.datetime | Unset = UNSET
    created_before: datetime.datetime | Unset = UNSET
    instruments: list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument] | Unset = (
        UNSET
    )
    side: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSide | Unset = UNSET
    open_close_indicator: (
        ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestOpenCloseIndicator | Unset
    ) = UNSET
    security_type: (
        ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSecurityType | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        created_after: str | Unset = UNSET
        if not isinstance(self.created_after, Unset):
            created_after = self.created_after.isoformat()

        created_before: str | Unset = UNSET
        if not isinstance(self.created_before, Unset):
            created_before = self.created_before.isoformat()

        instruments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instruments, Unset):
            instruments = []
            for instruments_item_data in self.instruments:
                instruments_item = instruments_item_data.to_dict()
                instruments.append(instruments_item)

        side: str | Unset = UNSET
        if not isinstance(self.side, Unset):
            side = self.side.value

        open_close_indicator: str | Unset = UNSET
        if not isinstance(self.open_close_indicator, Unset):
            open_close_indicator = self.open_close_indicator.value

        security_type: str | Unset = UNSET
        if not isinstance(self.security_type, Unset):
            security_type = self.security_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if created_after is not UNSET:
            field_dict["createdAfter"] = created_after
        if created_before is not UNSET:
            field_dict["createdBefore"] = created_before
        if instruments is not UNSET:
            field_dict["instruments"] = instruments
        if side is not UNSET:
            field_dict["side"] = side
        if open_close_indicator is not UNSET:
            field_dict["openCloseIndicator"] = open_close_indicator
        if security_type is not UNSET:
            field_dict["securityType"] = security_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_order_gateway_order_instrument import (
            ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument,
        )

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestStatus(_status)

        _created_after = d.pop("createdAfter", UNSET)
        created_after: datetime.datetime | Unset
        if isinstance(_created_after, Unset):
            created_after = UNSET
        else:
            created_after = datetime.datetime.fromisoformat(_created_after)

        _created_before = d.pop("createdBefore", UNSET)
        created_before: datetime.datetime | Unset
        if isinstance(_created_before, Unset):
            created_before = UNSET
        else:
            created_before = datetime.datetime.fromisoformat(_created_before)

        _instruments = d.pop("instruments", UNSET)
        instruments: (
            list[ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument] | Unset
        ) = UNSET
        if _instruments is not UNSET:
            instruments = []
            for instruments_item_data in _instruments:
                instruments_item = (
                    ComHellopublicUserapigatewayApiRestOrderGatewayOrderInstrument.from_dict(
                        instruments_item_data
                    )
                )

                instruments.append(instruments_item)

        _side = d.pop("side", UNSET)
        side: ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSide | Unset
        if isinstance(_side, Unset):
            side = UNSET
        else:
            side = ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSide(_side)

        _open_close_indicator = d.pop("openCloseIndicator", UNSET)
        open_close_indicator: (
            ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestOpenCloseIndicator | Unset
        )
        if isinstance(_open_close_indicator, Unset):
            open_close_indicator = UNSET
        else:
            open_close_indicator = (
                ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestOpenCloseIndicator(
                    _open_close_indicator
                )
            )

        _security_type = d.pop("securityType", UNSET)
        security_type: (
            ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSecurityType | Unset
        )
        if isinstance(_security_type, Unset):
            security_type = UNSET
        else:
            security_type = (
                ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSecurityType(
                    _security_type
                )
            )

        com_hellopublic_userapigateway_api_rest_order_api_query_orders_request = cls(
            status=status,
            created_after=created_after,
            created_before=created_before,
            instruments=instruments,
            side=side,
            open_close_indicator=open_close_indicator,
            security_type=security_type,
        )

        com_hellopublic_userapigateway_api_rest_order_api_query_orders_request.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_order_api_query_orders_request

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
