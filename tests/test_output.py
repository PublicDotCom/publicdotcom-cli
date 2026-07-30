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
