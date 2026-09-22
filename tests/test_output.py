import io

import pytest
from rich.console import Console

from publicdotcom_cli import output


def _capture_accounts(monkeypatch: pytest.MonkeyPatch, data: object) -> str:
    buffer = io.StringIO()
    monkeypatch.setattr(output, "console", Console(file=buffer, width=200, no_color=True))
    output.print_accounts(data)
    return buffer.getvalue()


def test_print_accounts_renders_entity_account_type(monkeypatch: pytest.MonkeyPatch) -> None:
    rendered = _capture_accounts(
        monkeypatch,
        {
            "accounts": [
                {
                    "accountId": "acct-1",
                    "accountType": "ENTITY",
                    "brokerageAccountType": "MARGIN",
                    "optionsLevel": "LEVEL_2",
                    "tradePermissions": "FULL",
                }
            ]
        },
    )

    assert "ENTITY" in rendered
    assert "acct-1" in rendered


def _capture_orders(monkeypatch: pytest.MonkeyPatch, data: object) -> str:
    buffer = io.StringIO()
    monkeypatch.setattr(output, "console", Console(file=buffer, width=200, no_color=True))
    output.print_orders(data)
    return buffer.getvalue()


def test_print_orders_renders_table_columns(monkeypatch: pytest.MonkeyPatch) -> None:
    rendered = _capture_orders(
        monkeypatch,
        {
            "orders": [
                {
                    "orderId": "ord-1",
                    "instrument": {"symbol": "AAPL", "type": "EQUITY"},
                    "type": "LIMIT",
                    "side": "BUY",
                    "status": "FILLED",
                    "quantity": "10",
                    "filledQuantity": "10",
                    "averagePrice": "244.90",
                    "createdAt": "2026-09-21T14:30:00Z",
                },
                {
                    "orderId": "ord-2",
                    "instrument": {"symbol": "MSFT", "type": "EQUITY"},
                    "type": "MARKET",
                    "side": "SELL",
                    "status": "NEW",
                    "notionalValue": "500.00",
                },
            ]
        },
    )

    assert "Orders" in rendered
    for cell in ("ord-1", "AAPL", "LIMIT", "BUY", "FILLED", "244.90", "2026-09-21T14:30:00Z"):
        assert cell in rendered
    assert "ord-2" in rendered
    assert "500.00" in rendered  # notional shown when quantity is absent


def test_print_orders_falls_back_to_json_without_orders(monkeypatch: pytest.MonkeyPatch) -> None:
    rendered = _capture_orders(monkeypatch, {"orders": []})

    assert "Orders" not in rendered
    assert '"orders"' in rendered
