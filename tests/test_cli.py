import re
from pathlib import Path

from typer.testing import CliRunner

from publicdotcom_cli import __version__
from publicdotcom_cli.cli import _apply_bracket_overrides, app

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
