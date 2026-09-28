import re
from pathlib import Path

import pytest
from typer.testing import CliRunner

from publicdotcom_cli import __version__
from publicdotcom_cli import cli as cli_module
from publicdotcom_cli.cli import _apply_bracket_overrides, _order_search_body, app

_ANSI_ESCAPES = re.compile(r"\x1b\[[0-9;]*m")


def _plain(text: str) -> str:
    """Strip ANSI styling so help-text assertions hold when color is forced (CI)."""
    return _ANSI_ESCAPES.sub("", text)


def test_version_option_prints_package_version() -> None:
    result = CliRunner().invoke(app, ["--version"])

    assert result.exit_code == 0
    assert f"publicdotcom-cli {__version__}" in _plain(result.stdout)


def test_taxlots_help_lists_subcommands() -> None:
    result = CliRunner().invoke(app, ["taxlots", "--help"])

    assert result.exit_code == 0
    assert "list" in result.stdout
    assert "symbol" in result.stdout
    assert "csv" in result.stdout


def test_options_help_lists_strategy_quote() -> None:
    result = CliRunner().invoke(app, ["options", "--help"])

    assert result.exit_code == 0
    assert "strategy-quote" in result.stdout


def test_instruments_help_lists_bonds() -> None:
    result = CliRunner().invoke(app, ["instruments", "--help"])

    assert result.exit_code == 0
    assert "bonds" in result.stdout


def test_market_help_lists_bond_details() -> None:
    result = CliRunner().invoke(app, ["market", "--help"])

    assert result.exit_code == 0
    assert "bond-details" in result.stdout


def test_order_replace_help_lists_quantity_and_amount() -> None:
    result = CliRunner().invoke(app, ["order", "replace", "--help"])

    assert result.exit_code == 0
    assert "--quantity" in _plain(result.stdout)
    assert "--amount" in _plain(result.stdout)


def test_historicdata_bars_help_lists_ipo_date() -> None:
    result = CliRunner().invoke(app, ["historicdata", "bars", "--help"])

    assert result.exit_code == 0
    assert "--ipo-date" in _plain(result.stdout)


def test_order_replace_rejects_quantity_with_amount(tmp_path: Path) -> None:
    request = tmp_path / "replace.json"
    request.write_text("{}", encoding="utf-8")

    result = CliRunner().invoke(
        app,
        [
            "order",
            "replace",
            "--file",
            str(request),
            "--account-id",
            "acct-1",
            "--quantity",
            "5",
            "--amount",
            "100",
        ],
    )

    assert result.exit_code == 1
    assert "mutually exclusive" in result.stderr


def test_order_replace_rejects_file_with_quantity_and_amount(tmp_path: Path) -> None:
    request = tmp_path / "replace.json"
    request.write_text('{"quantity": "5", "amount": "100"}', encoding="utf-8")

    result = CliRunner().invoke(
        app,
        ["order", "replace", "--file", str(request), "--account-id", "acct-1", "--yes"],
    )

    assert result.exit_code == 1
    assert "cannot include both" in result.stderr


def test_order_place_help_lists_bracket_options() -> None:
    result = CliRunner().invoke(app, ["order", "place", "--help"])

    assert result.exit_code == 0
    plain = _plain(result.stdout)
    assert "--order-class" in plain
    assert "--take-profit-limit" in plain
    assert "--stop-loss-stop" in plain
    assert "--stop-loss-limit" in plain


def _bracket_request(tmp_path: Path) -> Path:
    request = tmp_path / "order.json"
    request.write_text(
        '{"instrument": {"symbol": "AAPL", "type": "EQUITY"}, "orderSide": "BUY", '
        '"orderType": "LIMIT", "expiration": {"timeInForce": "DAY"}, "quantity": "10"}',
        encoding="utf-8",
    )
    return request


def _place(request: Path, *args: str) -> object:
    return CliRunner().invoke(
        app,
        ["order", "place", "--file", str(request), "--account-id", "acct-1", *args],
    )


def test_order_place_rejects_invalid_order_class(tmp_path: Path) -> None:
    result = _place(_bracket_request(tmp_path), "--order-class", "TRAILING", "--yes")

    assert result.exit_code == 1
    assert "Invalid --order-class" in result.stderr


def test_order_place_rejects_stop_loss_limit_without_stop(tmp_path: Path) -> None:
    result = _place(
        _bracket_request(tmp_path),
        "--order-class",
        "BRACKET",
        "--stop-loss-limit",
        "209.50",
        "--yes",
    )

    assert result.exit_code == 1
    assert "requires --stop-loss-stop" in result.stderr


def test_order_place_rejects_bracket_class_without_exit_legs(tmp_path: Path) -> None:
    result = _place(_bracket_request(tmp_path), "--order-class", "BRACKET", "--yes")

    assert result.exit_code == 1
    assert "requires at least one of" in result.stderr


def test_order_place_rejects_exit_legs_without_bracket_class(tmp_path: Path) -> None:
    result = _place(_bracket_request(tmp_path), "--take-profit-limit", "245.00", "--yes")

    assert result.exit_code == 1
    assert "require --order-class" in result.stderr


def test_order_place_rejects_exit_legs_with_simple_class(tmp_path: Path) -> None:
    result = _place(
        _bracket_request(tmp_path),
        "--order-class",
        "SIMPLE",
        "--stop-loss-stop",
        "210.00",
        "--yes",
    )

    assert result.exit_code == 1
    assert "require --order-class" in result.stderr


def _overrides(**kwargs: str | None) -> dict:
    """Run the bracket overrides over a minimal body and return the bracket keys."""
    body: dict = {"instrument": {"symbol": "AAPL", "type": "EQUITY"}}
    defaults: dict[str, str | None] = {
        "order_class": None,
        "take_profit_limit": None,
        "stop_loss_stop": None,
        "stop_loss_limit": None,
    }
    defaults.update(kwargs)
    _apply_bracket_overrides(body, **defaults)  # type: ignore[arg-type]
    return {k: body[k] for k in ("orderClass", "takeProfit", "stopLoss") if k in body}


def test_bracket_overrides_noop_without_flags() -> None:
    assert _overrides() == {}


def test_bracket_overrides_build_both_exit_legs() -> None:
    assert _overrides(
        order_class="BRACKET", take_profit_limit="245.00", stop_loss_stop="210.00"
    ) == {
        "orderClass": "BRACKET",
        "takeProfit": {"limitPrice": "245.00"},
        "stopLoss": {"stopPrice": "210.00"},
    }


def test_bracket_overrides_normalize_order_class_case() -> None:
    result = _overrides(order_class="oco", take_profit_limit="245.00")

    assert result["orderClass"] == "OCO"


def test_bracket_overrides_stop_limit_makes_stop_limit_leg() -> None:
    result = _overrides(order_class="OTO", stop_loss_stop="210.00", stop_loss_limit="209.50")

    assert result["stopLoss"] == {"stopPrice": "210.00", "limitPrice": "209.50"}


def test_bracket_overrides_flags_win_over_request_file() -> None:
    body: dict = {"orderClass": "OTO", "takeProfit": {"limitPrice": "1.00"}}
    _apply_bracket_overrides(
        body,
        order_class="BRACKET",
        take_profit_limit="245.00",
        stop_loss_stop=None,
        stop_loss_limit=None,
    )

    assert body["orderClass"] == "BRACKET"
    assert body["takeProfit"] == {"limitPrice": "245.00"}


def test_bracket_overrides_accept_exit_legs_from_request_file() -> None:
    body: dict = {"stopLoss": {"stopPrice": "210.00"}}
    _apply_bracket_overrides(
        body,
        order_class="BRACKET",
        take_profit_limit=None,
        stop_loss_stop=None,
        stop_loss_limit=None,
    )

    assert body["orderClass"] == "BRACKET"
    assert body["stopLoss"] == {"stopPrice": "210.00"}


ORDER_V2 = {
    "orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc",
    "instrument": {"symbol": "AAPL", "type": "EQUITY"},
    "createdAt": "2026-09-21T14:30:00+00:00",
    "type": "LIMIT",
    "side": "BUY",
    "status": "FILLED",
    "quantity": "10",
    "expiration": {"timeInForce": "DAY"},
    "limitPrice": "245.00",
    "filledQuantity": "10",
    "averagePrice": "244.90",
    "equityMarketSession": "REGULAR",
    "filledAt": "2026-09-21T14:30:05+00:00",
    "lastModified": "2026-09-21T14:30:05+00:00",
    "trades": [
        {
            "instrument": {"symbol": "AAPL", "type": "EQUITY"},
            "quantity": "10",
            "price": "244.90",
            "side": "BUY",
            "tradeId": "trade-1",
            "timestamp": "2026-09-21T14:30:05+00:00",
        }
    ],
}


def _capture_calls(monkeypatch: pytest.MonkeyPatch, response: object) -> list:
    """Replace the HTTP helper so commands record their request instead of sending it."""
    calls: list = []

    def fake_call(ctx: object, method: str, path: str, **kwargs: object) -> object:
        calls.append((method, path, kwargs))
        return response

    monkeypatch.setattr(cli_module, "_call", fake_call)
    return calls


def test_order_help_lists_search_and_hides_deprecated_get_v2() -> None:
    result = CliRunner().invoke(app, ["order", "--help"])

    assert result.exit_code == 0
    assert "search" in result.stdout
    assert "get-v2" not in result.stdout


def test_order_search_help_lists_filters() -> None:
    result = CliRunner().invoke(app, ["order", "search", "--help"])

    assert result.exit_code == 0
    plain = _plain(result.stdout)
    for flag in (
        "--status",
        "--side",
        "--symbol",
        "--security-type",
        "--open-close",
        "--created-after",
        "--created-before",
    ):
        assert flag in plain


def test_order_search_posts_filters_to_search_endpoint(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, {"orders": []})

    result = CliRunner().invoke(
        app,
        [
            "order",
            "search",
            "--account-id",
            "acct-1",
            "--status",
            "filled",
            "--side",
            "buy",
            "--symbol",
            "aapl",
            "--symbol",
            "spy:option",
            "--security-type",
            "equity",
            "--open-close",
            "open",
            "--created-after",
            "2026-09-01T00:00:00Z",
            "--created-before",
            "2026-09-22T00:00:00Z",
        ],
    )

    assert result.exit_code == 0, result.stderr
    assert calls == [
        (
            "POST",
            "/userapigateway/trading/acct-1/order/search",
            {
                "json_body": {
                    "status": "FILLED",
                    "createdAfter": "2026-09-01T00:00:00Z",
                    "createdBefore": "2026-09-22T00:00:00Z",
                    "instruments": [
                        {"symbol": "AAPL", "type": "EQUITY"},
                        {"symbol": "SPY", "type": "OPTION"},
                    ],
                    "side": "BUY",
                    "openCloseIndicator": "OPEN",
                    "securityType": "EQUITY",
                }
            },
        )
    ]


def test_order_search_sends_empty_body_without_filters(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, {"orders": []})

    result = CliRunner().invoke(app, ["order", "search", "--account-id", "acct-1"])

    assert result.exit_code == 0, result.stderr
    assert calls[0][2] == {"json_body": {}}


def test_order_search_rejects_invalid_status(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, {"orders": []})

    result = CliRunner().invoke(
        app, ["order", "search", "--account-id", "acct-1", "--status", "OPEN"]
    )

    assert result.exit_code == 1
    assert "Invalid --status" in result.stderr
    assert calls == []


def test_order_search_rejects_malformed_symbol(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, {"orders": []})

    result = CliRunner().invoke(
        app, ["order", "search", "--account-id", "acct-1", "--symbol", ":OPTION"]
    )

    assert result.exit_code == 1
    assert "Invalid instrument" in result.stderr
    assert calls == []


def test_order_search_renders_orders_table(monkeypatch: pytest.MonkeyPatch) -> None:
    _capture_calls(monkeypatch, {"orders": [ORDER_V2]})

    result = CliRunner().invoke(app, ["order", "search", "--account-id", "acct-1"])

    assert result.exit_code == 0, result.stderr
    plain = _plain(result.stdout)
    assert "Orders" in plain
    assert "AAPL" in plain
    assert "FILLED" in plain
    assert "244.90" in plain


def test_order_search_json_flag_prints_raw_response(monkeypatch: pytest.MonkeyPatch) -> None:
    _capture_calls(monkeypatch, {"orders": [ORDER_V2]})

    result = CliRunner().invoke(app, ["--json", "order", "search", "--account-id", "acct-1"])

    assert result.exit_code == 0, result.stderr
    plain = _plain(result.stdout)
    assert "trades" in plain
    assert "trade-1" in plain
    assert "Orders" not in plain


def test_order_search_accepts_event_contract_security_type(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _capture_calls(monkeypatch, {"orders": []})

    result = CliRunner().invoke(
        app,
        ["order", "search", "--account-id", "acct-1", "--security-type", "eventcontract"],
    )

    assert result.exit_code == 0, result.stderr
    assert calls[0][2] == {"json_body": {"securityType": "EVENTCONTRACT"}}


def test_order_get_prints_v2_order_fields(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, ORDER_V2)

    result = CliRunner().invoke(app, ["order", "get", "ord-1", "--account-id", "acct-1"])

    assert result.exit_code == 0, result.stderr
    assert calls == [("GET", "/userapigateway/trading/acct-1/order/ord-1", {})]
    plain = _plain(result.stdout)
    for field in ("filledAt", "equityMarketSession", "lastModified", "trade-1"):
        assert field in plain


def test_order_get_v2_is_deprecated_alias_for_order_get(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, ORDER_V2)

    result = CliRunner().invoke(app, ["order", "get-v2", "ord-1", "--account-id", "acct-1"])

    assert result.exit_code == 0, result.stderr
    assert calls == [("GET", "/userapigateway/trading/acct-1/order/ord-1", {})]
    assert "deprecated" in _plain(result.stderr)
    assert "order get" in _plain(result.stderr)
    plain = _plain(result.stdout)
    assert "filledAt" in plain
    assert "trade-1" in plain


EVENT_ID = "KALSHI.KXBALANCESHEET-EO26-EVENT"
YES_SYMBOL = "KALSHI.KXBALANCESHEET-EO26-6.6.Y-EVENTCONTRACT"
NO_SYMBOL = "KALSHI.KXBALANCESHEET-EO26-6.6.N-EVENTCONTRACT"

EVENT_CONTRACT_CHARTS = {
    "period": "WEEK",
    "charts": [
        {
            "symbol": YES_SYMBOL,
            "previousClosePrice": "0.41",
            "currentPrice": "0.47",
            "totalGainLoss": "0.06",
            "totalGainLossPercentage": "14.63",
            "bars": [
                {
                    "timestamp": "2026-09-21T00:00:00Z",
                    "open": "0.40",
                    "close": "0.42",
                    "high": "0.43",
                    "low": "0.39",
                    "value": "0.42",
                    "volume": 1200,
                },
                {
                    "timestamp": "2026-09-28T00:00:00Z",
                    "open": "0.45",
                    "close": "0.47",
                    "high": "0.48",
                    "low": "0.44",
                    "value": "0.47",
                    "volume": 900,
                },
            ],
        }
    ],
}


def test_historicdata_help_lists_event_contract_bars() -> None:
    result = CliRunner().invoke(app, ["historicdata", "--help"])

    assert result.exit_code == 0
    assert "event-contract-bars" in result.stdout


def test_historicdata_bars_help_lists_event_contract_type() -> None:
    result = CliRunner().invoke(app, ["historicdata", "bars", "--help"])

    assert result.exit_code == 0
    assert "EVENTCONTRACT" in _plain(result.stdout)


def test_event_contract_bars_calls_endpoint(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, EVENT_CONTRACT_CHARTS)

    result = CliRunner().invoke(
        app,
        [
            "historicdata",
            "event-contract-bars",
            EVENT_ID,
            "week",
            "--symbol",
            YES_SYMBOL.lower(),
            "--symbol",
            NO_SYMBOL,
        ],
    )

    assert result.exit_code == 0, result.stderr
    assert calls == [
        (
            "GET",
            f"/userapigateway/historicdata/event-contracts/{EVENT_ID}/bars/WEEK",
            {"params": {"symbols": f"{YES_SYMBOL},{NO_SYMBOL}"}},
        )
    ]


def test_event_contract_bars_splits_comma_separated_symbols(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _capture_calls(monkeypatch, EVENT_CONTRACT_CHARTS)

    result = CliRunner().invoke(
        app,
        [
            "historicdata",
            "event-contract-bars",
            EVENT_ID,
            "ALL",
            "--symbol",
            f"{YES_SYMBOL}, {NO_SYMBOL}",
        ],
    )

    assert result.exit_code == 0, result.stderr
    assert calls[0][2] == {"params": {"symbols": f"{YES_SYMBOL},{NO_SYMBOL}"}}


def test_event_contract_bars_rejects_more_than_eight_symbols(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = _capture_calls(monkeypatch, EVENT_CONTRACT_CHARTS)
    args = ["historicdata", "event-contract-bars", EVENT_ID, "DAY"]
    for index in range(9):
        args += ["--symbol", f"KALSHI.X-{index}.Y-EVENTCONTRACT"]

    result = CliRunner().invoke(app, args)

    assert result.exit_code == 1
    assert "at most 8" in _plain(result.stderr)
    assert calls == []


def test_event_contract_bars_rejects_invalid_period(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, EVENT_CONTRACT_CHARTS)

    result = CliRunner().invoke(
        app,
        ["historicdata", "event-contract-bars", EVENT_ID, "YEAR", "--symbol", YES_SYMBOL],
    )

    assert result.exit_code == 1
    assert "Invalid period" in _plain(result.stderr)
    assert calls == []


def test_event_contract_bars_requires_a_symbol(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, EVENT_CONTRACT_CHARTS)

    result = CliRunner().invoke(app, ["historicdata", "event-contract-bars", EVENT_ID, "DAY"])

    assert result.exit_code != 0
    assert calls == []


def test_event_contract_bars_rejects_blank_symbols(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, EVENT_CONTRACT_CHARTS)

    result = CliRunner().invoke(
        app, ["historicdata", "event-contract-bars", EVENT_ID, "DAY", "--symbol", " , "]
    )

    assert result.exit_code == 1
    assert "at least one --symbol" in _plain(result.stderr)
    assert calls == []


def test_event_contract_bars_renders_charts_table(monkeypatch: pytest.MonkeyPatch) -> None:
    _capture_calls(monkeypatch, EVENT_CONTRACT_CHARTS)

    result = CliRunner().invoke(
        app,
        ["historicdata", "event-contract-bars", EVENT_ID, "WEEK", "--symbol", YES_SYMBOL],
    )

    assert result.exit_code == 0, result.stderr
    plain = _plain(result.stdout)
    assert "Event Contract Charts" in plain
    assert "0.47" in plain
    assert "14.63" in plain


def test_event_contract_bars_json_flag_prints_raw_response(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _capture_calls(monkeypatch, EVENT_CONTRACT_CHARTS)

    result = CliRunner().invoke(
        app,
        [
            "--json",
            "historicdata",
            "event-contract-bars",
            EVENT_ID,
            "WEEK",
            "--symbol",
            YES_SYMBOL,
        ],
    )

    assert result.exit_code == 0, result.stderr
    plain = _plain(result.stdout)
    assert '"bars"' in plain
    assert "Event Contract Charts" not in plain


def _search_body(**kwargs: object) -> dict:
    defaults: dict[str, object] = {
        "status": None,
        "side": None,
        "open_close": None,
        "security_type": None,
        "created_after": None,
        "created_before": None,
        "symbols": None,
    }
    defaults.update(kwargs)
    return _order_search_body(**defaults)  # type: ignore[arg-type]


def test_order_search_body_is_empty_without_filters() -> None:
    assert _search_body() == {}


def test_order_search_body_normalizes_enum_case() -> None:
    assert _search_body(status="partially_filled", side="sell", open_close="close") == {
        "status": "PARTIALLY_FILLED",
        "side": "SELL",
        "openCloseIndicator": "CLOSE",
    }


def test_order_search_body_defaults_symbol_type_to_equity() -> None:
    assert _search_body(symbols=["aapl", "spy:option"]) == {
        "instruments": [
            {"symbol": "AAPL", "type": "EQUITY"},
            {"symbol": "SPY", "type": "OPTION"},
        ]
    }
