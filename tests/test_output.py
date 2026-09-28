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


def _capture_event_contract_charts(monkeypatch: pytest.MonkeyPatch, data: object) -> str:
    buffer = io.StringIO()
    monkeypatch.setattr(output, "console", Console(file=buffer, width=250, no_color=True))
    output.print_event_contract_charts(data)
    return buffer.getvalue()


def test_print_event_contract_charts_renders_one_row_per_symbol(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered = _capture_event_contract_charts(
        monkeypatch,
        {
            "period": "DAY",
            "charts": [
                {
                    "symbol": "KX-1.Y-EVENTCONTRACT",
                    "previousClosePrice": "0.30",
                    "currentPrice": "0.35",
                    "totalGainLoss": "0.05",
                    "totalGainLossPercentage": "16.67",
                    "bars": [
                        {"timestamp": "2026-09-28T13:00:00Z", "close": "0.31"},
                        {"timestamp": "2026-09-28T14:00:00Z", "close": "0.35"},
                    ],
                },
                {
                    "symbol": "KX-2.N-EVENTCONTRACT",
                    "previousClosePrice": None,
                    "currentPrice": None,
                    "totalGainLoss": None,
                    "totalGainLossPercentage": None,
                    "bars": [],
                },
            ],
        },
    )

    assert "Event Contract Charts (DAY)" in rendered
    for cell in (
        "KX-1.Y-EVENTCONTRACT",
        "0.35",
        "0.30",
        "16.67",
        "2026-09-28T13:00:00Z",
        "2026-09-28T14:00:00Z",
    ):
        assert cell in rendered
    assert "KX-2.N-EVENTCONTRACT" in rendered
    assert "None" not in rendered  # nullable prices render blank


def test_print_event_contract_charts_falls_back_to_json_without_charts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered = _capture_event_contract_charts(monkeypatch, {"period": "DAY", "charts": []})

    assert "Event Contract Charts" not in rendered
    assert '"charts"' in rendered
