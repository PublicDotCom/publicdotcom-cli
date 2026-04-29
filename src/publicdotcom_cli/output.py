from __future__ import annotations

import json
from typing import Any

import typer
from rich.console import Console
from rich.table import Table

console = Console()
err_console = Console(stderr=True)


def print_json(data: Any) -> None:
    console.print_json(json.dumps(data, default=str))


def print_error(message: str) -> None:
    err_console.print(f"[red]{message}[/red]")


def print_accounts(data: Any) -> None:
    accounts = data.get("accounts") if isinstance(data, dict) else None
    if not accounts:
        print_json(data)
        return

    table = Table(title="Accounts")
    table.add_column("Account ID")
    table.add_column("Type")
    table.add_column("Brokerage")
    table.add_column("Options")
    table.add_column("Permissions")

    for account in accounts:
        table.add_row(
            str(account.get("accountId", "")),
            str(account.get("accountType", "")),
            str(account.get("brokerageAccountType", "")),
            str(account.get("optionsLevel", "")),
            str(account.get("tradePermissions", "")),
        )
    console.print(table)


def print_quotes(data: Any) -> None:
    quotes = data.get("quotes") if isinstance(data, dict) else None
    if not quotes:
        print_json(data)
        return

    table = Table(title="Quotes")
    table.add_column("Symbol")
    table.add_column("Type")
    table.add_column("Outcome")
    table.add_column("Last", justify="right")
    table.add_column("Bid", justify="right")
    table.add_column("Ask", justify="right")
    table.add_column("Volume", justify="right")

    for quote in quotes:
        instrument = quote.get("instrument") or {}
        table.add_row(
            str(instrument.get("symbol", "")),
            str(instrument.get("type", "")),
            str(quote.get("outcome", "")),
            str(quote.get("last", "")),
            str(quote.get("bid", "")),
            str(quote.get("ask", "")),
            str(quote.get("volume", "")),
        )
    console.print(table)


def exit_with_error(message: str, code: int = 1) -> None:
    print_error(message)
    raise typer.Exit(code)
