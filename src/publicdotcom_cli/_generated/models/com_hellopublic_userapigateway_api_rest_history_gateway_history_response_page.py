from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction import (
        ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransaction,
    )


T = TypeVar("T", bound="ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage")


@_attrs_define
class ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryResponsePage:
    """Gateway history response page

    Attributes:
        transactions (list[ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransaction] | Unset): List of
            transactions
        next_token (None | str | Unset): Token to retrieve the next page of results
        start (datetime.datetime | None | Unset): Start timestamp of the history query
        end (datetime.datetime | None | Unset): End timestamp of the history query
        page_size (int | None | Unset): Number of items to return
    """

    transactions: (
        list[ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransaction] | Unset
    ) = UNSET
    next_token: None | str | Unset = UNSET
    start: datetime.datetime | None | Unset = UNSET
    end: datetime.datetime | None | Unset = UNSET
    page_size: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()
                transactions.append(transactions_item)

        next_token: None | str | Unset
        if isinstance(self.next_token, Unset):
            next_token = UNSET
        else:
            next_token = self.next_token

        start: None | str | Unset
        if isinstance(self.start, Unset):
            start = UNSET
        elif isinstance(self.start, datetime.datetime):
            start = self.start.isoformat()
        else:
            start = self.start

        end: None | str | Unset
        if isinstance(self.end, Unset):
            end = UNSET
        elif isinstance(self.end, datetime.datetime):
            end = self.end.isoformat()
        else:
            end = self.end

        page_size: int | None | Unset
        if isinstance(self.page_size, Unset):
            page_size = UNSET
        else:
            page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if next_token is not UNSET:
            field_dict["nextToken"] = next_token
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.com_hellopublic_userapigateway_api_rest_history_gateway_history_transaction import (
            ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransaction,
        )

        d = dict(src_dict)
        _transactions = d.pop("transactions", UNSET)
        transactions: (
            list[ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransaction] | Unset
        ) = UNSET
        if _transactions is not UNSET:
            transactions = []
            for transactions_item_data in _transactions:
                transactions_item = (
                    ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransaction.from_dict(
                        transactions_item_data
                    )
                )

                transactions.append(transactions_item)

        def _parse_next_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_token = _parse_next_token(d.pop("nextToken", UNSET))

        def _parse_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_type_0 = isoparse(data)

                return start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start = _parse_start(d.pop("start", UNSET))

        def _parse_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_0 = isoparse(data)

                return end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end = _parse_end(d.pop("end", UNSET))

        def _parse_page_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_size = _parse_page_size(d.pop("pageSize", UNSET))

        com_hellopublic_userapigateway_api_rest_history_gateway_history_response_page = cls(
            transactions=transactions,
            next_token=next_token,
            start=start,
            end=end,
            page_size=page_size,
        )

        com_hellopublic_userapigateway_api_rest_history_gateway_history_response_page.additional_properties = d
        return com_hellopublic_userapigateway_api_rest_history_gateway_history_response_page

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
