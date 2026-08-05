from pathlib import Path

from typer.testing import CliRunner

from publicdotcom_cli import __version__
from publicdotcom_cli.cli import app


def test_version_option_prints_package_version() -> None:
    result = CliRunner().invoke(app, ["--version"])

    assert result.exit_code == 0
    assert f"publicdotcom-cli {__version__}" in result.stdout


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
    assert "--quantity" in result.stdout
    assert "--amount" in result.stdout


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
