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
