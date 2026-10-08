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


def print_orders(data: Any) -> None:
    orders = data.get("orders") if isinstance(data, dict) else None
    if not orders:
        print_json(data)
        return

    table = Table(title="Orders")
    table.add_column("Order ID")
    table.add_column("Symbol")
    table.add_column("Type")
    table.add_column("Side")
    table.add_column("Status")
    table.add_column("Qty / Notional", justify="right")
    table.add_column("Filled", justify="right")
    table.add_column("Avg Price", justify="right")
    table.add_column("Created")

    for order in orders:
        instrument = order.get("instrument") or {}
        table.add_row(
            str(order.get("orderId", "")),
            str(instrument.get("symbol", "")),
            str(order.get("type", "")),
            str(order.get("side", "")),
            str(order.get("status", "")),
            str(order.get("quantity") or order.get("notionalValue") or ""),
            str(order.get("filledQuantity", "")),
            str(order.get("averagePrice", "")),
            str(order.get("createdAt", "")),
        )
    console.print(table)


def print_event_contract_charts(data: Any) -> None:
    charts = data.get("charts") if isinstance(data, dict) else None
    if not charts:
        print_json(data)
        return

    period = data.get("period")
    table = Table(title=f"Event Contract Charts ({period})" if period else "Event Contract Charts")
    table.add_column("Symbol")
    table.add_column("Current", justify="right")
    table.add_column("Prev Close", justify="right")
    table.add_column("Gain/Loss", justify="right")
    table.add_column("Gain/Loss %", justify="right")
    table.add_column("Bars", justify="right")
    table.add_column("First Bar")
    table.add_column("Last Bar")

    for chart in charts:
        bars = chart.get("bars") or []
        table.add_row(
            str(chart.get("symbol", "")),
            str(chart.get("currentPrice") or ""),
            str(chart.get("previousClosePrice") or ""),
            str(chart.get("totalGainLoss") or ""),
            str(chart.get("totalGainLossPercentage") or ""),
            str(len(bars)),
            str(bars[0].get("timestamp", "")) if bars else "",
            str(bars[-1].get("timestamp", "")) if bars else "",
        )
    console.print(table)


def print_event_categories(data: Any) -> None:
    categories = data.get("categories") if isinstance(data, dict) else None
    if not categories:
        print_json(data)
        return

    table = Table(title="Event Categories")
    table.add_column("Category")
    table.add_column("Subcategories")
    table.add_column("Frequencies")

    for category in categories:
        frequency = category.get("eventFrequency") or {}
        table.add_row(
            str(category.get("category", "")),
            ", ".join(str(item) for item in category.get("subcategories") or []),
            ", ".join(str(item) for item in frequency.get("frequencies") or []),
        )
    console.print(table)


def _event_status(event: dict[str, Any]) -> str:
    if event.get("resolved"):
        return "RESOLVED"
    if event.get("halted"):
        return "HALTED"
    return "OPEN"


def print_event_summaries(data: Any) -> None:
    events = data.get("content") if isinstance(data, dict) else None
    if not events:
        print_json(data)
        return

    table = Table(title="Events")
    table.add_column("Event Symbol")
    table.add_column("Title")
    table.add_column("Category")
    table.add_column("Volume", justify="right")
    table.add_column("Resolution Time")
    table.add_column("Status")
    table.add_column("Contracts", justify="right")

    for event in events:
        table.add_row(
            str(event.get("eventSymbol", "")),
            str(event.get("title", "")),
            str(event.get("category", "")),
            str(event.get("volume", "")),
            str(event.get("resolutionTime") or ""),
            _event_status(event),
            str(len(event.get("symbols") or [])),
        )
    console.print(table)

    next_token = data.get("nextToken")
    if next_token:
        console.print(f"More results: pass --next-token {next_token}")


def _contract_by_side(outcome: dict[str, Any], side: str) -> dict[str, Any]:
    for contract in outcome.get("contracts") or []:
        if contract.get("predictedOutcome") == side:
            return contract
    return {}


def print_event_details(data: Any) -> None:
    outcomes = data.get("outcomes") if isinstance(data, dict) else None
    if not isinstance(data, dict) or "eventSymbol" not in data:
        print_json(data)
        return

    console.print(
        f"[bold]{data.get('title', '')}[/bold] ({data.get('eventSymbol', '')})\n"
        f"Exchange: {data.get('exchange', '')}  Category: {data.get('category', '')}  "
        f"Volume: {data.get('volume', '')}  Status: {_event_status(data)}  "
        f"Outcomes: {len(outcomes or [])} of {data.get('outcomeCount', '')}"
    )
    cftc = data.get("cftcContract") or {}
    if cftc.get("contractTermsUrl"):
        console.print(f"Contract terms: {cftc['contractTermsUrl']}")

    if not outcomes:
        return

    table = Table(title="Outcomes")
    table.add_column("Outcome")
    table.add_column("State")
    table.add_column("Trading")
    table.add_column("Probability", justify="right")
    table.add_column("YES Bid", justify="right")
    table.add_column("YES Ask", justify="right")
    table.add_column("NO Bid", justify="right")
    table.add_column("NO Ask", justify="right")
    table.add_column("Volume", justify="right")
    table.add_column("Close Time")

    for outcome in outcomes:
        yes = _contract_by_side(outcome, "YES")
        no = _contract_by_side(outcome, "NO")
        timeline = outcome.get("timeline") or {}
        table.add_row(
            str(outcome.get("title", "")),
            str(outcome.get("state", "")),
            str(outcome.get("trading", "")),
            str(yes.get("probability") or ""),
            str(yes.get("bid") or ""),
            str(yes.get("ask") or ""),
            str(no.get("bid") or ""),
            str(no.get("ask") or ""),
            str(outcome.get("volume", "")),
            str(timeline.get("closeTime", "")),
        )
    console.print(table)


def exit_with_error(message: str, code: int = 1) -> None:
    print_error(message)
    raise typer.Exit(code)
