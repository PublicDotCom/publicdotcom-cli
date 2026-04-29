from typer.testing import CliRunner

from publicdotcom_cli import __version__
from publicdotcom_cli.cli import app


def test_version_option_prints_package_version() -> None:
    result = CliRunner().invoke(app, ["--version"])

    assert result.exit_code == 0
    assert f"publicdotcom-cli {__version__}" in result.stdout
