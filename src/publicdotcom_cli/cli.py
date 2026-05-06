from __future__ import annotations

from dataclasses import dataclass
from getpass import getpass
from pathlib import Path
from typing import Annotated, Any

import typer

from publicdotcom_cli import __version__
from publicdotcom_cli.client import ApiClient, ApiError, MissingTokenError
from publicdotcom_cli.config import (
    ACCOUNT_ID_ENV_VAR,
    AUTO_REFRESH_ENV_VAR,
    BASE_URL_ENV_VAR,
    DEFAULT_BASE_URL,
    SECRET_ENV_VAR,
    TOKEN_ENV_VAR,
    clear_default_account_id,
    clear_personal_secret,
    clear_token,
    get_default_account_id,
    get_personal_secret,
    get_token,
    mask_token,
    set_default_account_id,
    set_personal_secret,
    set_token,
    token_expires_soon,
)
from publicdotcom_cli.output import (
    console,
    exit_with_error,
    print_accounts,
    print_error,
    print_json,
    print_quotes,
)
from publicdotcom_cli.payloads import ensure_order_id, instrument, instruments, load_json_file

app = typer.Typer(help="CLI for the Public API.")
auth_app = typer.Typer(help="Authentication commands.")
accounts_app = typer.Typer(help="Account commands.")
portfolio_app = typer.Typer(help="Portfolio commands.")
history_app = typer.Typer(help="Account history commands.")
instruments_app = typer.Typer(help="Instrument lookup commands.")
market_app = typer.Typer(help="Market data commands.")
options_app = typer.Typer(help="Option details commands.")
order_app = typer.Typer(help="Order and preflight commands.")
historicdata_app = typer.Typer(help="Historic bar data commands.")

app.add_typer(auth_app, name="auth")
app.add_typer(accounts_app, name="accounts")
app.add_typer(portfolio_app, name="portfolio")
app.add_typer(history_app, name="history")
app.add_typer(instruments_app, name="instruments")
app.add_typer(market_app, name="market")
app.add_typer(options_app, name="options")
app.add_typer(order_app, name="order")
app.add_typer(historicdata_app, name="historicdata")


@dataclass
class RuntimeConfig:
    base_url: str
    token: str | None
    personal_secret: str | None
    default_account_id: str | None
    timeout: float
    json_output: bool
    auto_refresh: bool
    refresh_validity_minutes: int
    refresh_skew_seconds: int


def _runtime(ctx: typer.Context) -> RuntimeConfig:
    runtime = ctx.find_root().obj
    if not isinstance(runtime, RuntimeConfig):
        raise RuntimeError("CLI runtime was not initialized")
    return runtime


def _api(ctx: typer.Context) -> ApiClient:
    runtime = _runtime(ctx)
    return ApiClient(base_url=runtime.base_url, token=runtime.token, timeout=runtime.timeout)


def _resolve_account_id(ctx: typer.Context, account_id: str | None) -> str:
    resolved = account_id or _runtime(ctx).default_account_id
    if not resolved:
        exit_with_error(
            "No account ID provided. Pass --account-id, set PUBLIC_ACCOUNT_ID, "
            "or run `public accounts set-default ACCOUNT_ID`."
        )
    return resolved


def _request_access_token(runtime: RuntimeConfig, secret: str) -> str:
    client = ApiClient(base_url=runtime.base_url, token=None, timeout=runtime.timeout)
    result = client.request(
        "POST",
        "/userapiauthservice/personal/access-tokens",
        json_body={
            "secret": secret,
            "validityInMinutes": runtime.refresh_validity_minutes,
        },
        authenticated=False,
    )
    if not isinstance(result, dict) or not isinstance(result.get("accessToken"), str):
        raise RuntimeError("Login response did not contain an accessToken.")
    return result["accessToken"]


def _request_access_token_or_exit(runtime: RuntimeConfig, secret: str) -> str:
    try:
        return _request_access_token(runtime, secret)
    except ApiError as exc:
        print_error(str(exc))
        if exc.body is not None:
            print_json(exc.body)
        raise typer.Exit(1) from exc
    except RuntimeError as exc:
        exit_with_error(str(exc))


def _refresh_token(ctx: typer.Context, *, force: bool = False) -> bool:
    runtime = _runtime(ctx)
    if not runtime.auto_refresh or not runtime.personal_secret:
        return False
    if not force and not token_expires_soon(
        runtime.token, skew_seconds=runtime.refresh_skew_seconds
    ):
        return False

    try:
        token = _request_access_token(runtime, runtime.personal_secret)
    except ApiError as exc:
        print_error("Automatic token refresh failed.")
        print_error(str(exc))
        if exc.body is not None:
            print_json(exc.body)
        raise typer.Exit(1) from exc
    except RuntimeError as exc:
        exit_with_error(str(exc))

    runtime.token = token
    set_token(token)
    return True


def _print(ctx: typer.Context, data: Any, *, table: str | None = None) -> None:
    runtime = _runtime(ctx)
    if runtime.json_output:
        print_json(data)
    elif table == "accounts":
        print_accounts(data)
    elif table == "quotes":
        print_quotes(data)
    else:
        print_json(data)


def _call(ctx: typer.Context, method: str, path: str, **kwargs: Any) -> Any:
    authenticated = bool(kwargs.get("authenticated", True))
    if authenticated:
        _refresh_token(ctx)

    try:
        return _api(ctx).request(method, path, **kwargs)
    except MissingTokenError as exc:
        if authenticated and _refresh_token(ctx, force=True):
            return _api(ctx).request(method, path, **kwargs)
        exit_with_error(str(exc))
    except ApiError as exc:
        if authenticated and exc.status_code == 401 and _refresh_token(ctx, force=True):
            return _api(ctx).request(method, path, **kwargs)
        print_error(str(exc))
        if exc.body is not None:
            print_json(exc.body)
        raise typer.Exit(1) from exc


ORDER_ACTION_WARNING = (
    "Trading action: review the account, symbols, side, quantity, prices, "
    "expiration, time-in-force, and full request payload before continuing."
)


def _confirm(action: str, yes: bool, *, warning: str | None = None) -> None:
    if yes:
        return
    if warning:
        console.print(f"[yellow]{warning}[/yellow]")
    if not typer.confirm(action):
        raise typer.Abort()


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"publicdotcom-cli {__version__}")
        raise typer.Exit()


@app.callback()
def root(
    ctx: typer.Context,
    version: Annotated[
        bool | None,
        typer.Option(
            "--version",
            callback=_version_callback,
            is_eager=True,
            help="Show the CLI version and exit.",
        ),
    ] = None,
    base_url: Annotated[
        str,
        typer.Option(
            "--base-url",
            envvar=BASE_URL_ENV_VAR,
            help="API base URL.",
        ),
    ] = DEFAULT_BASE_URL,
    token: Annotated[
        str | None,
        typer.Option(
            "--token",
            envvar=TOKEN_ENV_VAR,
            help="Access token. Prefer PUBLIC_ACCESS_TOKEN for automation.",
        ),
    ] = None,
    timeout: Annotated[
        float,
        typer.Option("--timeout", min=1.0, help="HTTP timeout in seconds."),
    ] = 30.0,
    auto_refresh: Annotated[
        bool,
        typer.Option(
            "--auto-refresh/--no-auto-refresh",
            envvar=AUTO_REFRESH_ENV_VAR,
            help="Refresh access tokens from a stored or environment personal secret.",
        ),
    ] = True,
    refresh_validity_minutes: Annotated[
        int,
        typer.Option(
            "--refresh-validity-minutes",
            min=5,
            max=1440,
            help="Lifetime for automatically refreshed access tokens.",
        ),
    ] = 60,
    refresh_skew_seconds: Annotated[
        int,
        typer.Option(
            "--refresh-skew-seconds",
            min=0,
            help="Refresh JWTs this many seconds before their exp timestamp.",
        ),
    ] = 60,
    json_output: Annotated[
        bool,
        typer.Option("--json", help="Always print raw JSON output."),
    ] = False,
) -> None:
    ctx.obj = RuntimeConfig(
        base_url=base_url,
        token=token or get_token(),
        personal_secret=get_personal_secret(),
        default_account_id=get_default_account_id(),
        timeout=timeout,
        json_output=json_output,
        auto_refresh=auto_refresh,
        refresh_validity_minutes=refresh_validity_minutes,
        refresh_skew_seconds=refresh_skew_seconds,
    )


@auth_app.command("login")
def auth_login(
    ctx: typer.Context,
    secret: Annotated[
        str | None,
        typer.Option("--secret", help="Personal secret. If omitted, you will be prompted."),
    ] = None,
    validity_minutes: Annotated[
        int,
        typer.Option(
            "--validity-minutes",
            min=5,
            max=1440,
            help="Access token lifetime in minutes.",
        ),
    ] = 60,
    print_token: Annotated[
        bool,
        typer.Option("--print-token", help="Print the access token after login."),
    ] = False,
    store_secret: Annotated[
        bool,
        typer.Option(
            "--store-secret",
            help="Store the personal secret so future commands can refresh tokens automatically.",
        ),
    ] = False,
) -> None:
    secret = secret or getpass("Personal secret: ")
    runtime = _runtime(ctx)
    runtime.refresh_validity_minutes = validity_minutes
    token = _request_access_token_or_exit(runtime, secret)
    runtime.token = token
    location = set_token(token)
    console.print(f"Access token stored in {location}.")
    if store_secret:
        secret_location = set_personal_secret(secret)
        runtime.personal_secret = secret
        console.print(f"Personal secret stored in {secret_location} for automatic refresh.")
    if print_token:
        console.print(token)


@auth_app.command("refresh")
def auth_refresh(
    ctx: typer.Context,
    secret: Annotated[
        str | None,
        typer.Option("--secret", help="Personal secret. Uses stored secret if omitted."),
    ] = None,
    validity_minutes: Annotated[
        int,
        typer.Option(
            "--validity-minutes",
            min=5,
            max=1440,
            help="Access token lifetime in minutes.",
        ),
    ] = 60,
    store_secret: Annotated[
        bool,
        typer.Option(
            "--store-secret", help="Store the provided personal secret for future refresh."
        ),
    ] = False,
    print_token: Annotated[
        bool,
        typer.Option("--print-token", help="Print the refreshed access token."),
    ] = False,
) -> None:
    runtime = _runtime(ctx)
    secret = secret or runtime.personal_secret or getpass("Personal secret: ")
    runtime.refresh_validity_minutes = validity_minutes
    token = _request_access_token_or_exit(runtime, secret)
    runtime.token = token
    location = set_token(token)
    console.print(f"Access token refreshed and stored in {location}.")
    if store_secret:
        secret_location = set_personal_secret(secret)
        runtime.personal_secret = secret
        console.print(f"Personal secret stored in {secret_location} for automatic refresh.")
    if print_token:
        console.print(token)


@auth_app.command("status")
def auth_status(ctx: typer.Context) -> None:
    runtime = _runtime(ctx)
    console.print(f"Base URL: {runtime.base_url}")
    console.print(f"Access token: {mask_token(runtime.token)}")
    console.print(f"Personal secret: {mask_token(runtime.personal_secret)}")
    console.print(f"Default account ID: {runtime.default_account_id or 'not set'}")
    console.print(f"Auto refresh: {'enabled' if runtime.auto_refresh else 'disabled'}")
    console.print(f"Secret env var: {SECRET_ENV_VAR}")
    console.print(f"Account env var: {ACCOUNT_ID_ENV_VAR}")


@auth_app.command("logout")
def auth_logout(
    clear_secret: Annotated[
        bool,
        typer.Option("--all", help="Also remove the stored personal secret."),
    ] = False,
) -> None:
    clear_token()
    console.print("Access token removed.")
    if clear_secret:
        clear_personal_secret()
        console.print("Personal secret removed.")


@accounts_app.command("list")
def accounts_list(ctx: typer.Context) -> None:
    result = _call(ctx, "GET", "/userapigateway/trading/account")
    _print(ctx, result, table="accounts")


@accounts_app.command("set-default")
def accounts_set_default(
    ctx: typer.Context,
    account_id: Annotated[
        str, typer.Argument(help="Account ID returned by `public accounts list`.")
    ],
) -> None:
    runtime = _runtime(ctx)
    runtime.default_account_id = account_id
    location = set_default_account_id(account_id)
    console.print(f"Default account ID set to {account_id} in {location}.")


@accounts_app.command("get-default")
def accounts_get_default(ctx: typer.Context) -> None:
    runtime = _runtime(ctx)
    if not runtime.default_account_id:
        exit_with_error("No default account ID set. Run `public accounts set-default ACCOUNT_ID`.")
    console.print(runtime.default_account_id)


@accounts_app.command("clear-default")
def accounts_clear_default(ctx: typer.Context) -> None:
    runtime = _runtime(ctx)
    runtime.default_account_id = None
    clear_default_account_id()
    console.print("Default account ID removed.")


@portfolio_app.command("show")
def portfolio_show(
    ctx: typer.Context,
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(ctx, "GET", f"/userapigateway/trading/{account_id}/portfolio/v2")
    _print(ctx, result)


@history_app.command("list")
def history_list(
    ctx: typer.Context,
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    start: Annotated[str | None, typer.Option("--start", help="ISO 8601 start timestamp.")] = None,
    end: Annotated[str | None, typer.Option("--end", help="ISO 8601 end timestamp.")] = None,
    page_size: Annotated[int | None, typer.Option("--page-size", min=1)] = None,
    next_token: Annotated[str | None, typer.Option("--next-token")] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(
        ctx,
        "GET",
        f"/userapigateway/trading/{account_id}/history",
        params={
            "start": start,
            "end": end,
            "pageSize": page_size,
            "nextToken": next_token,
        },
    )
    _print(ctx, result)


@instruments_app.command("list")
def instruments_list(
    ctx: typer.Context,
    type_filter: Annotated[
        list[str] | None,
        typer.Option("--type-filter", help="Security type filter. Repeat for multiple."),
    ] = None,
    trading_filter: Annotated[
        list[str] | None,
        typer.Option("--trading-filter", help="Trading status filter. Repeat for multiple."),
    ] = None,
    fractional_trading_filter: Annotated[
        list[str] | None,
        typer.Option(
            "--fractional-trading-filter",
            help="Fractional trading status filter. Repeat for multiple.",
        ),
    ] = None,
    option_trading_filter: Annotated[
        list[str] | None,
        typer.Option("--option-trading-filter", help="Option trading filter. Repeat for multiple."),
    ] = None,
    option_spread_trading_filter: Annotated[
        list[str] | None,
        typer.Option(
            "--option-spread-trading-filter",
            help="Option spread trading filter. Repeat for multiple.",
        ),
    ] = None,
) -> None:
    result = _call(
        ctx,
        "GET",
        "/userapigateway/trading/instruments",
        params={
            "typeFilter": type_filter,
            "tradingFilter": trading_filter,
            "fractionalTradingFilter": fractional_trading_filter,
            "optionTradingFilter": option_trading_filter,
            "optionSpreadTradingFilter": option_spread_trading_filter,
        },
    )
    _print(ctx, result)


@instruments_app.command("get")
def instrument_get(
    ctx: typer.Context,
    symbol: Annotated[str, typer.Argument()],
    security_type: Annotated[str, typer.Argument(help="EQUITY, OPTION, CRYPTO, etc.")],
) -> None:
    result = _call(
        ctx,
        "GET",
        f"/userapigateway/trading/instruments/{symbol.upper()}/{security_type.upper()}",
    )
    _print(ctx, result)


@market_app.command("quotes")
def market_quotes(
    ctx: typer.Context,
    symbols: Annotated[list[str], typer.Argument(help="One or more symbols.")],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    security_type: Annotated[
        str,
        typer.Option("--type", help="Instrument type for all symbols."),
    ] = "EQUITY",
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(
        ctx,
        "POST",
        f"/userapigateway/marketdata/{account_id}/quotes",
        json_body={"instruments": instruments(symbols, security_type)},
    )
    _print(ctx, result, table="quotes")


@market_app.command("option-expirations")
def option_expirations(
    ctx: typer.Context,
    symbol: Annotated[str, typer.Argument()],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    security_type: Annotated[
        str,
        typer.Option("--type", help="Underlying instrument type."),
    ] = "EQUITY",
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(
        ctx,
        "POST",
        f"/userapigateway/marketdata/{account_id}/option-expirations",
        json_body={"instrument": instrument(symbol, security_type)},
    )
    _print(ctx, result)


@market_app.command("option-chain")
def option_chain(
    ctx: typer.Context,
    symbol: Annotated[str, typer.Argument()],
    expiration_date: Annotated[str, typer.Argument(help="Expiration date as YYYY-MM-DD.")],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    security_type: Annotated[
        str,
        typer.Option("--type", help="Underlying instrument type."),
    ] = "EQUITY",
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(
        ctx,
        "POST",
        f"/userapigateway/marketdata/{account_id}/option-chain",
        json_body={
            "instrument": instrument(symbol, security_type),
            "expirationDate": expiration_date,
        },
    )
    _print(ctx, result)


@options_app.command("greeks")
def option_greeks(
    ctx: typer.Context,
    osi_symbols: Annotated[list[str], typer.Argument(help="One or more OSI-normalized symbols.")],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(
        ctx,
        "GET",
        f"/userapigateway/option-details/{account_id}/greeks",
        params={"osiSymbols": osi_symbols},
    )
    _print(ctx, result)


@order_app.command("preflight-single")
def preflight_single(
    ctx: typer.Context,
    file: Annotated[Path, typer.Option("--file", "-f", exists=True, readable=True)],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    body = load_json_file(file)
    result = _call(
        ctx,
        "POST",
        f"/userapigateway/trading/{account_id}/preflight/single-leg",
        json_body=body,
    )
    _print(ctx, result)


@order_app.command("preflight-multi")
def preflight_multi(
    ctx: typer.Context,
    file: Annotated[Path, typer.Option("--file", "-f", exists=True, readable=True)],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    body = load_json_file(file)
    result = _call(
        ctx,
        "POST",
        f"/userapigateway/trading/{account_id}/preflight/multi-leg",
        json_body=body,
    )
    _print(ctx, result)


@order_app.command("place")
def order_place(
    ctx: typer.Context,
    file: Annotated[Path, typer.Option("--file", "-f", exists=True, readable=True)],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    body = load_json_file(file)
    if not isinstance(body, dict):
        exit_with_error("Order request JSON must be an object.")
    order_id = ensure_order_id(body)
    _confirm(f"Submit order {order_id}?", yes, warning=ORDER_ACTION_WARNING)
    result = _call(
        ctx,
        "POST",
        f"/userapigateway/trading/{account_id}/order",
        json_body=body,
    )
    _print(ctx, result)


@order_app.command("replace")
def order_replace(
    ctx: typer.Context,
    file: Annotated[Path, typer.Option("--file", "-f", exists=True, readable=True)],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    body = load_json_file(file)
    _confirm("Submit cancel-replace request?", yes, warning=ORDER_ACTION_WARNING)
    result = _call(
        ctx,
        "PUT",
        f"/userapigateway/trading/{account_id}/order",
        json_body=body,
    )
    _print(ctx, result)


@order_app.command("place-multileg")
def order_place_multileg(
    ctx: typer.Context,
    file: Annotated[Path, typer.Option("--file", "-f", exists=True, readable=True)],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    body = load_json_file(file)
    if not isinstance(body, dict):
        exit_with_error("Multileg order request JSON must be an object.")
    order_id = ensure_order_id(body)
    _confirm(f"Submit multileg order {order_id}?", yes, warning=ORDER_ACTION_WARNING)
    result = _call(
        ctx,
        "POST",
        f"/userapigateway/trading/{account_id}/order/multileg",
        json_body=body,
    )
    _print(ctx, result)


@order_app.command("get")
def order_get(
    ctx: typer.Context,
    order_id: Annotated[str, typer.Argument()],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(ctx, "GET", f"/userapigateway/trading/{account_id}/order/{order_id}")
    _print(ctx, result)


@order_app.command("cancel")
def order_cancel(
    ctx: typer.Context,
    order_id: Annotated[str, typer.Argument()],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    _confirm(
        f"Cancel order {order_id}?",
        yes,
        warning="Trading action: cancellation requests may be asynchronous. Verify order status after submitting.",
    )
    result = _call(ctx, "DELETE", f"/userapigateway/trading/{account_id}/order/{order_id}")
    _print(ctx, result if result is not None else {"cancelRequested": True})


@historicdata_app.command("bars")
def historicdata_bars(
    ctx: typer.Context,
    symbol: Annotated[str, typer.Argument(help="Ticker symbol, e.g. AAPL.")],
    period: Annotated[
        str,
        typer.Argument(
            help="Time period: DAY, WEEK, MONTH, QUARTER, HALF_YEAR, YEAR, FIVE_YEARS, YTD, SINCE_PURCHASE."
        ),
    ],
    aggregation: Annotated[
        str | None,
        typer.Option(
            "--aggregation",
            help=(
                "Bar aggregation override: ONE_MINUTE, FIVE_MINUTES, TEN_MINUTES, "
                "FIFTEEN_MINUTES, THIRTY_MINUTES, ONE_HOUR, ONE_DAY, ONE_WEEK, "
                "ONE_MONTH, THREE_MONTHS, SIX_MONTHS, ONE_YEAR."
            ),
        ),
    ] = None,
    purchase_date: Annotated[
        str | None,
        typer.Option("--purchase-date", help="Required when period is SINCE_PURCHASE. YYYY-MM-DD."),
    ] = None,
) -> None:
    if aggregation:
        path = f"/userapigateway/historicdata/{symbol.upper()}/{period.upper()}/{aggregation.upper()}"
    else:
        path = f"/userapigateway/historicdata/{symbol.upper()}/{period.upper()}"
    result = _call(ctx, "GET", path, params={"purchaseDate": purchase_date})
    _print(ctx, result)


def main() -> None:
    app()
