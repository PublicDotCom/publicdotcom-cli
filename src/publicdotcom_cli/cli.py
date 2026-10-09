from __future__ import annotations

import base64
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
    print_event_categories,
    print_event_contract_charts,
    print_event_details,
    print_event_summaries,
    print_json,
    print_orders,
    print_quotes,
)
from publicdotcom_cli.payloads import (
    ensure_order_id,
    instrument,
    instrument_spec,
    instruments,
    load_json_file,
)

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
taxlots_app = typer.Typer(help="Unrealized tax lot commands.")
event_contracts_app = typer.Typer(help="Event contract (prediction market) discovery commands.")

app.add_typer(auth_app, name="auth")
app.add_typer(accounts_app, name="accounts")
app.add_typer(portfolio_app, name="portfolio")
app.add_typer(history_app, name="history")
app.add_typer(instruments_app, name="instruments")
app.add_typer(market_app, name="market")
app.add_typer(options_app, name="options")
app.add_typer(order_app, name="order")
app.add_typer(historicdata_app, name="historicdata")
app.add_typer(taxlots_app, name="taxlots")
app.add_typer(event_contracts_app, name="event-contracts")


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
    elif table == "orders":
        print_orders(data)
    elif table == "event_contract_charts":
        print_event_contract_charts(data)
    elif table == "event_categories":
        print_event_categories(data)
    elif table == "event_summaries":
        print_event_summaries(data)
    elif table == "event_details":
        print_event_details(data)
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


ORDER_CLASSES = ("SIMPLE", "BRACKET", "OCO", "OTO")
BRACKET_ORDER_CLASSES = ("BRACKET", "OCO", "OTO")


ORDER_SEARCH_STATUSES = (
    "NEW",
    "PARTIALLY_FILLED",
    "CANCELLED",
    "QUEUED_CANCELLED",
    "FILLED",
    "REJECTED",
    "PENDING_REPLACE",
    "PENDING_CANCEL",
    "EXPIRED",
    "REPLACED",
)
ORDER_SEARCH_SIDES = ("BUY", "SELL")
ORDER_SEARCH_OPEN_CLOSE = ("OPEN", "CLOSE")
ORDER_SEARCH_SECURITY_TYPES = (
    "EQUITY",
    "OPTION",
    "MULTI_LEG_INSTRUMENT",
    "CRYPTO",
    "ALT",
    "TREASURY",
    "BOND",
    "INDEX",
    "EVENTCONTRACT",
)

EVENT_CONTRACT_PERIODS = ("DAY", "WEEK", "MONTH", "ALL")
EVENT_CONTRACT_MAX_SYMBOLS = 8

EVENT_SORTING_MODES = ("VOLUME", "EXPIRATION", "RECENTLY_ADDED")
EVENT_FREQUENCIES = (
    "ALL",
    "ONCE",
    "FIFTEEN_MINUTES",
    "ONE_HOUR",
    "ONE_DAY",
    "ONE_WEEK",
    "ONE_MONTH",
    "ONE_YEAR",
)


def _normalized_choice(value: str | None, *, flag: str, choices: tuple[str, ...]) -> str | None:
    """Upper-case a flag value and reject anything outside the spec's enum."""
    if value is None:
        return None
    normalized = value.strip().upper()
    if normalized not in choices:
        exit_with_error(f"Invalid {flag} {value!r}. Expected one of: {', '.join(choices)}.")
    return normalized


def _order_search_body(
    *,
    status: str | None,
    side: str | None,
    open_close: str | None,
    security_type: str | None,
    created_after: str | None,
    created_before: str | None,
    symbols: list[str] | None,
) -> dict[str, Any]:
    """Build the order-search request body from the filter flags.

    Only filters that were given are included, so a bare `order search` sends `{}`
    and the API returns every order from the last 30 days (up to 500).
    """
    body: dict[str, Any] = {}

    normalized_status = _normalized_choice(status, flag="--status", choices=ORDER_SEARCH_STATUSES)
    if normalized_status is not None:
        body["status"] = normalized_status
    if created_after is not None:
        body["createdAfter"] = created_after
    if created_before is not None:
        body["createdBefore"] = created_before
    if symbols:
        body["instruments"] = [instrument_spec(value) for value in symbols]
    normalized_side = _normalized_choice(side, flag="--side", choices=ORDER_SEARCH_SIDES)
    if normalized_side is not None:
        body["side"] = normalized_side
    normalized_open_close = _normalized_choice(
        open_close, flag="--open-close", choices=ORDER_SEARCH_OPEN_CLOSE
    )
    if normalized_open_close is not None:
        body["openCloseIndicator"] = normalized_open_close
    normalized_security_type = _normalized_choice(
        security_type, flag="--security-type", choices=ORDER_SEARCH_SECURITY_TYPES
    )
    if normalized_security_type is not None:
        body["securityType"] = normalized_security_type

    return body


def _apply_bracket_overrides(
    body: dict[str, Any],
    *,
    order_class: str | None,
    take_profit_limit: str | None,
    stop_loss_stop: str | None,
    stop_loss_limit: str | None,
) -> None:
    """Fold the bracket-order flags into the request body, in place.

    Each flag overrides the corresponding key in the request file. Only the
    coherence of the flags themselves is checked here — the remaining bracket
    constraints (whole-share quantity, CORE session, entry order type) are
    enforced by the API.
    """
    if stop_loss_limit is not None and stop_loss_stop is None:
        exit_with_error("--stop-loss-limit requires --stop-loss-stop.")

    if order_class is not None:
        normalized = order_class.strip().upper()
        if normalized not in ORDER_CLASSES:
            exit_with_error(
                f"Invalid --order-class {order_class!r}. Expected one of: "
                f"{', '.join(ORDER_CLASSES)}."
            )
        body["orderClass"] = normalized

    if take_profit_limit is not None:
        body["takeProfit"] = {"limitPrice": take_profit_limit}

    if stop_loss_stop is not None:
        stop_loss: dict[str, str] = {"stopPrice": stop_loss_stop}
        if stop_loss_limit is not None:
            stop_loss["limitPrice"] = stop_loss_limit
        body["stopLoss"] = stop_loss

    effective_class = body.get("orderClass")
    has_exit_leg = "takeProfit" in body or "stopLoss" in body

    if effective_class in BRACKET_ORDER_CLASSES and not has_exit_leg:
        exit_with_error(
            f"Order class {effective_class} requires at least one of "
            "--take-profit-limit or --stop-loss-stop (or `takeProfit` / `stopLoss` "
            "in the request file)."
        )
    if has_exit_leg and effective_class not in BRACKET_ORDER_CLASSES:
        exit_with_error(
            "`takeProfit` and `stopLoss` require --order-class to be one of: "
            f"{', '.join(BRACKET_ORDER_CLASSES)}."
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


@instruments_app.command("bonds")
def instruments_bonds(
    ctx: typer.Context,
    page_number: Annotated[
        int | None,
        typer.Option("--page-number", min=0, help="Page number (zero-based). Defaults to 0."),
    ] = None,
    page_size: Annotated[
        int | None,
        typer.Option("--page-size", min=1, help="Number of items per page. Defaults to 20."),
    ] = None,
    sort_property: Annotated[
        str | None,
        typer.Option("--sort-property", help="Property to sort by."),
    ] = None,
    sort_direction: Annotated[
        str | None,
        typer.Option("--sort-direction", help="Sort direction: ASC or DESC. Defaults to DESC."),
    ] = None,
    issuer: Annotated[
        str | None,
        typer.Option("--issuer", help="Filter by issuer name."),
    ] = None,
    issuer_symbol: Annotated[
        list[str] | None,
        typer.Option("--issuer-symbol", help="Filter by issuer symbol. Repeat for multiple."),
    ] = None,
    bond_status: Annotated[
        list[str] | None,
        typer.Option(
            "--bond-status",
            help="Filter by bond status, e.g. OUTSTANDING, MATURED, CALLED. Repeat for multiple.",
        ),
    ] = None,
    bond_type: Annotated[
        list[str] | None,
        typer.Option(
            "--bond-type",
            help=(
                "Filter by bond type: AGENCY, CD, CORPORATE, GOVERNMENT, MUNICIPAL, or TREASURY. "
                "Repeat for multiple."
            ),
        ),
    ] = None,
    treasury_subtype: Annotated[
        list[str] | None,
        typer.Option(
            "--treasury-subtype",
            help=(
                "Filter by treasury subtype: BOND, BILL, NOTE, STRIPS, TIPS, or FLOATING. "
                "Repeat for multiple."
            ),
        ),
    ] = None,
    rating: Annotated[
        list[str] | None,
        typer.Option(
            "--rating",
            help="Filter by S&P credit rating, e.g. AAA, AA+, BBB-. Repeat for multiple.",
        ),
    ] = None,
    rating_category: Annotated[
        str | None,
        typer.Option(
            "--rating-category",
            help="Filter by rating category: INVESTMENT_GRADE or SPECULATIVE_GRADE.",
        ),
    ] = None,
    sp_outlook: Annotated[
        list[str] | None,
        typer.Option(
            "--sp-outlook",
            help=(
                "Filter by S&P outlook: POSITIVE, NEGATIVE, DEVELOPING, STABLE, NOT_RATED, or "
                "NOT_MEANINGFUL. Repeat for multiple."
            ),
        ),
    ] = None,
    sp_creditwatch: Annotated[
        list[str] | None,
        typer.Option(
            "--sp-creditwatch",
            help=(
                "Filter by S&P creditwatch status: POSITIVE, NEGATIVE, DEVELOPING, or "
                "NOT_MEANINGFUL. Repeat for multiple."
            ),
        ),
    ] = None,
    coupon_frequency: Annotated[
        list[str] | None,
        typer.Option(
            "--coupon-frequency",
            help=(
                "Filter by coupon payment frequency: AT_MATURITY, ZERO, MONTHLY, QUARTERLY, "
                "SEMI_ANNUAL, or ANNUAL. Repeat for multiple."
            ),
        ),
    ] = None,
    min_coupon: Annotated[
        float | None,
        typer.Option("--min-coupon", help="Minimum coupon rate."),
    ] = None,
    max_coupon: Annotated[
        float | None,
        typer.Option("--max-coupon", help="Maximum coupon rate."),
    ] = None,
    min_maturity_date: Annotated[
        str | None,
        typer.Option(
            "--min-maturity-date",
            help=(
                "Minimum maturity date (YYYY-MM-DD). The API defaults this to today + 14 days to "
                "exclude bonds nearing maturity with volatile yields."
            ),
        ),
    ] = None,
    max_maturity_date: Annotated[
        str | None,
        typer.Option("--max-maturity-date", help="Maximum maturity date (YYYY-MM-DD)."),
    ] = None,
    min_current_yield: Annotated[
        float | None,
        typer.Option("--min-current-yield", help="Minimum current yield."),
    ] = None,
    max_current_yield: Annotated[
        float | None,
        typer.Option("--max-current-yield", help="Maximum current yield."),
    ] = None,
    min_par_value: Annotated[
        float | None,
        typer.Option("--min-par-value", help="Minimum par value."),
    ] = None,
    max_par_value: Annotated[
        float | None,
        typer.Option("--max-par-value", help="Maximum par value."),
    ] = None,
    min_liquidity_rating: Annotated[
        float | None,
        typer.Option("--min-liquidity-rating", help="Minimum liquidity rating (1-5)."),
    ] = None,
    max_liquidity_rating: Annotated[
        float | None,
        typer.Option("--max-liquidity-rating", help="Maximum liquidity rating (1-5)."),
    ] = None,
    liquidity_rating: Annotated[
        list[float] | None,
        typer.Option(
            "--liquidity-rating",
            help=(
                "Filter by specific liquidity rating, from 1 (low) to 5 (high). "
                "Repeat for multiple."
            ),
        ),
    ] = None,
    callable_filter: Annotated[
        bool | None,
        typer.Option("--callable/--no-callable", help="Filter by callable status."),
    ] = None,
    perpetual: Annotated[
        bool | None,
        typer.Option("--perpetual/--no-perpetual", help="Filter by perpetual bond status."),
    ] = None,
    partial_par: Annotated[
        bool | None,
        typer.Option("--partial-par/--no-partial-par", help="Filter by partial par status."),
    ] = None,
) -> None:
    result = _call(
        ctx,
        "GET",
        "/userapigateway/trading/instruments/bonds",
        params={
            "pageNumber": page_number,
            "pageSize": page_size,
            "sortProperty": sort_property,
            "sortDirection": sort_direction,
            "issuer": issuer,
            "issuerSymbol": issuer_symbol,
            "bondStatus": bond_status,
            "bondType": bond_type,
            "treasurySubtype": treasury_subtype,
            "rating": rating,
            "ratingCategory": rating_category,
            "spOutlook": sp_outlook,
            "spCreditwatch": sp_creditwatch,
            "couponFrequency": coupon_frequency,
            "minCoupon": min_coupon,
            "maxCoupon": max_coupon,
            "minMaturityDate": min_maturity_date,
            "maxMaturityDate": max_maturity_date,
            "minCurrentYield": min_current_yield,
            "maxCurrentYield": max_current_yield,
            "minParValue": min_par_value,
            "maxParValue": max_par_value,
            "minLiquidityRating": min_liquidity_rating,
            "maxLiquidityRating": max_liquidity_rating,
            "liquidityRating": liquidity_rating,
            "callable": callable_filter,
            "perpetual": perpetual,
            "partialPar": partial_par,
        },
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


@market_app.command("bond-details")
def market_bond_details(
    ctx: typer.Context,
    symbol: Annotated[str, typer.Argument(help="Bond symbol, typically CUSIP-BOND format.")],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(
        ctx,
        "GET",
        f"/userapigateway/marketdata/{account_id}/bond-details/{symbol.upper()}",
    )
    _print(ctx, result)


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


@options_app.command("strategy-quote")
def option_strategy_quote(
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
        f"/userapigateway/option-details/{account_id}/strategy-details/quote",
        json_body=body,
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
    order_class: Annotated[
        str | None,
        typer.Option(
            "--order-class",
            help=(
                "Order class: SIMPLE, BRACKET, OCO or OTO. Overrides `orderClass` in the "
                "request file. The bracket classes need at least one of --take-profit-limit "
                "or --stop-loss-stop."
            ),
        ),
    ] = None,
    take_profit_limit: Annotated[
        str | None,
        typer.Option(
            "--take-profit-limit",
            help=(
                "Take-profit limit price for a bracket order. Overrides `takeProfit` in the "
                "request file."
            ),
        ),
    ] = None,
    stop_loss_stop: Annotated[
        str | None,
        typer.Option(
            "--stop-loss-stop",
            help=(
                "Stop-loss stop price for a bracket order. Overrides `stopLoss` in the "
                "request file. Placed as a STOP order unless --stop-loss-limit is given too."
            ),
        ),
    ] = None,
    stop_loss_limit: Annotated[
        str | None,
        typer.Option(
            "--stop-loss-limit",
            help=(
                "Stop-loss limit price, making the stop-loss a STOP_LIMIT order. "
                "Requires --stop-loss-stop."
            ),
        ),
    ] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    body = load_json_file(file)
    if not isinstance(body, dict):
        exit_with_error("Order request JSON must be an object.")
    _apply_bracket_overrides(
        body,
        order_class=order_class,
        take_profit_limit=take_profit_limit,
        stop_loss_stop=stop_loss_stop,
        stop_loss_limit=stop_loss_limit,
    )
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
    quantity: Annotated[
        str | None,
        typer.Option(
            "--quantity",
            help=(
                "Replacement order quantity. Overrides `quantity` in the request file. "
                "Mutually exclusive with --amount."
            ),
        ),
    ] = None,
    amount: Annotated[
        str | None,
        typer.Option(
            "--amount",
            help=(
                "Replacement notional order amount. Overrides `amount` in the request file. "
                "Mutually exclusive with --quantity."
            ),
        ),
    ] = None,
    yes: Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation.")] = False,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    if quantity is not None and amount is not None:
        exit_with_error("--quantity and --amount are mutually exclusive.")
    body = load_json_file(file)
    if quantity is not None or amount is not None:
        if not isinstance(body, dict):
            exit_with_error(
                "Replace request JSON must be an object to override quantity or amount."
            )
        if quantity is not None:
            body["quantity"] = quantity
            body.pop("amount", None)
        else:
            body["amount"] = amount
            body.pop("quantity", None)
    if isinstance(body, dict) and "quantity" in body and "amount" in body:
        exit_with_error(
            "Replace request cannot include both `quantity` and `amount`; "
            "they are mutually exclusive."
        )
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
    """Retrieve an order from the last 30 days, including its trades and fill timestamps."""
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(ctx, "GET", f"/userapigateway/trading/{account_id}/order/{order_id}")
    _print(ctx, result)


@order_app.command("search")
def order_search(
    ctx: typer.Context,
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    status: Annotated[
        str | None,
        typer.Option(
            "--status",
            help=(
                "Filter by order status: NEW, PARTIALLY_FILLED, CANCELLED, QUEUED_CANCELLED, "
                "FILLED, REJECTED, PENDING_REPLACE, PENDING_CANCEL, EXPIRED, or REPLACED."
            ),
        ),
    ] = None,
    side: Annotated[
        str | None,
        typer.Option("--side", help="Filter by order side: BUY or SELL."),
    ] = None,
    symbols: Annotated[
        list[str] | None,
        typer.Option(
            "--symbol",
            help=(
                "Filter by instrument, as SYMBOL or SYMBOL:TYPE (type defaults to EQUITY). "
                "Repeat for multiple."
            ),
        ),
    ] = None,
    security_type: Annotated[
        str | None,
        typer.Option(
            "--security-type",
            help=(
                "Filter by security type: EQUITY, OPTION, MULTI_LEG_INSTRUMENT, CRYPTO, ALT, "
                "TREASURY, BOND, INDEX, or EVENTCONTRACT."
            ),
        ),
    ] = None,
    open_close: Annotated[
        str | None,
        typer.Option("--open-close", help="Filter by open/close indicator: OPEN or CLOSE."),
    ] = None,
    created_after: Annotated[
        str | None,
        typer.Option(
            "--created-after",
            help="Only orders created at or after this ISO 8601 timestamp, e.g. 2026-09-01T00:00:00Z.",
        ),
    ] = None,
    created_before: Annotated[
        str | None,
        typer.Option(
            "--created-before",
            help="Only orders created before this ISO 8601 timestamp.",
        ),
    ] = None,
) -> None:
    """Search orders created within the last 30 days (up to 500 results)."""
    account_id = _resolve_account_id(ctx, account_id)
    try:
        body = _order_search_body(
            status=status,
            side=side,
            open_close=open_close,
            security_type=security_type,
            created_after=created_after,
            created_before=created_before,
            symbols=symbols,
        )
    except ValueError as exc:
        exit_with_error(str(exc))
    result = _call(
        ctx,
        "POST",
        f"/userapigateway/trading/{account_id}/order/search",
        json_body=body,
    )
    _print(ctx, result, table="orders")


@order_app.command("get-v2", hidden=True)
def order_get_v2(
    ctx: typer.Context,
    order_id: Annotated[str, typer.Argument()],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
) -> None:
    """Deprecated alias for `order get`, which now returns the same order shape."""
    print_error("`order get-v2` is deprecated and will be removed; use `order get` instead.")
    order_get(ctx, order_id=order_id, account_id=account_id)


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
    security_type: Annotated[
        str,
        typer.Argument(help="Instrument type: EQUITY, CRYPTO, OPTION, INDEX, EVENTCONTRACT."),
    ],
    symbol: Annotated[str, typer.Argument(help="Ticker symbol, e.g. AAPL.")],
    period: Annotated[
        str,
        typer.Argument(
            help="Time period: DAY, WEEK, MONTH, QUARTER, HALF_YEAR, YEAR, FIVE_YEARS, TEN_YEARS, ALL, YTD, SINCE_PURCHASE."
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
    ipo_date: Annotated[
        str | None,
        typer.Option(
            "--ipo-date",
            help=(
                "Optional IPO / first-trade date, YYYY-MM-DD. When the asset is younger "
                "than the requested period, the response uses a finer aggregation over "
                "post-IPO history and includes a leadingFill object describing the flat "
                "pre-IPO lead-in. Not applied to the DAY chart."
            ),
        ),
    ] = None,
) -> None:
    base = f"/userapigateway/historicdata/{security_type.upper()}/{symbol.upper()}/{period.upper()}"
    path = f"{base}/{aggregation.upper()}" if aggregation else base
    result = _call(ctx, "GET", path, params={"purchaseDate": purchase_date, "ipoDate": ipo_date})
    _print(ctx, result)


def _event_contract_symbols(values: list[str]) -> str:
    """Join repeated and/or comma-separated --symbol values into the API's `symbols` param."""
    symbols = [part.strip().upper() for value in values for part in value.split(",")]
    symbols = [symbol for symbol in symbols if symbol]
    if not symbols:
        exit_with_error("Pass at least one --symbol.")
    if len(symbols) > EVENT_CONTRACT_MAX_SYMBOLS:
        exit_with_error(
            f"Too many symbols ({len(symbols)}); the API accepts at most "
            f"{EVENT_CONTRACT_MAX_SYMBOLS} per request."
        )
    return ",".join(symbols)


@historicdata_app.command("event-contract-bars")
def historicdata_event_contract_bars(
    ctx: typer.Context,
    event_id: Annotated[
        str,
        typer.Argument(help="The -EVENT grouping id, e.g. KALSHI.KXBALANCESHEET-EO26-EVENT."),
    ],
    period: Annotated[
        str,
        typer.Argument(help="Time period: DAY, WEEK, MONTH, or ALL."),
    ],
    symbols: Annotated[
        list[str],
        typer.Option(
            "--symbol",
            help=(
                "An -EVENTCONTRACT symbol belonging to the event. Repeat (or comma-separate) "
                f"for up to {EVENT_CONTRACT_MAX_SYMBOLS}."
            ),
        ),
    ],
) -> None:
    """Fetch chart bars for up to 8 contracts of one event (prices are 0.00-1.00 probabilities)."""
    normalized_period = _normalized_choice(period, flag="period", choices=EVENT_CONTRACT_PERIODS)
    symbols_param = _event_contract_symbols(symbols)
    result = _call(
        ctx,
        "GET",
        f"/userapigateway/historicdata/event-contracts/{event_id.upper()}/bars/{normalized_period}",
        params={"symbols": symbols_param},
    )
    _print(ctx, result, table="event_contract_charts")


def _event_summary_body(
    *,
    sort: str,
    category: str | None,
    subcategory: str | None,
    next_token: str | None,
    include_resolved: bool | None,
    created_within_days: int | None,
    event_symbols: list[str] | None,
    frequencies: list[str] | None,
    resolution_start: str | None,
    resolution_end: str | None,
) -> dict[str, Any]:
    """Build the event-summary request body from the command flags.

    `sortingMode` is always sent (the spec requires it). The `filters` object is only
    sent when a filter flag is given; because the spec marks both of its lists as
    required, an omitted list defaults to `eventSymbols: []` / `frequencies: ["ALL"]`.
    """
    body: dict[str, Any] = {
        "sortingMode": _normalized_choice(sort, flag="--sort", choices=EVENT_SORTING_MODES)
    }
    if category is not None:
        body["category"] = category
    if subcategory is not None:
        body["subcategory"] = subcategory
    if next_token is not None:
        body["nextToken"] = next_token
    if include_resolved is not None:
        body["displayResolvedEvents"] = include_resolved
    if created_within_days is not None:
        body["createdWithinDays"] = created_within_days

    symbols = [part.strip().upper() for value in event_symbols or [] for part in value.split(",")]
    symbols = [symbol for symbol in symbols if symbol]
    normalized_frequencies = [
        _normalized_choice(value, flag="--frequency", choices=EVENT_FREQUENCIES)
        for value in frequencies or []
    ]
    if symbols or normalized_frequencies or resolution_start or resolution_end:
        filters: dict[str, Any] = {
            "eventSymbols": symbols,
            "frequencies": normalized_frequencies or ["ALL"],
        }
        if resolution_start is not None:
            filters["resolutionTimeStart"] = resolution_start
        if resolution_end is not None:
            filters["resolutionTimeEnd"] = resolution_end
        body["filters"] = filters

    return body


@event_contracts_app.command("categories")
def event_contracts_categories(ctx: typer.Context) -> None:
    """List event categories, their subcategories, and supported frequency filters."""
    result = _call(ctx, "GET", "/userapigateway/eventcontract/summary/categories")
    _print(ctx, result, table="event_categories")


@event_contracts_app.command("summary")
def event_contracts_summary(
    ctx: typer.Context,
    sort: Annotated[
        str,
        typer.Option("--sort", help="Sort order: VOLUME, EXPIRATION, or RECENTLY_ADDED."),
    ] = "VOLUME",
    category: Annotated[
        str | None,
        typer.Option("--category", help="Limit to a category from `event-contracts categories`."),
    ] = None,
    subcategory: Annotated[
        str | None,
        typer.Option("--subcategory", help="Limit to a subcategory."),
    ] = None,
    next_token: Annotated[
        str | None,
        typer.Option(
            "--next-token", help="nextToken from a previous response, to fetch the next page."
        ),
    ] = None,
    include_resolved: Annotated[
        bool | None,
        typer.Option(
            "--include-resolved/--no-include-resolved",
            help="Include or exclude resolved events (sends displayResolvedEvents).",
        ),
    ] = None,
    created_within_days: Annotated[
        int | None,
        typer.Option("--created-within-days", help="Only events created within the last N days."),
    ] = None,
    event_symbols: Annotated[
        list[str] | None,
        typer.Option(
            "--event-symbol",
            help="Only these events, e.g. KALSHI.KXBALANCESHEET-EO26. Repeat or comma-separate.",
        ),
    ] = None,
    frequencies: Annotated[
        list[str] | None,
        typer.Option(
            "--frequency",
            help=(
                "Event frequency filter: ALL, ONCE, FIFTEEN_MINUTES, ONE_HOUR, ONE_DAY, "
                "ONE_WEEK, ONE_MONTH, ONE_YEAR. Repeat for multiple."
            ),
        ),
    ] = None,
    resolution_start: Annotated[
        str | None,
        typer.Option(
            "--resolution-start", help="Only events resolving at or after this ISO 8601 time."
        ),
    ] = None,
    resolution_end: Annotated[
        str | None,
        typer.Option(
            "--resolution-end", help="Only events resolving at or before this ISO 8601 time."
        ),
    ] = None,
) -> None:
    """List event summaries (up to 100 per page; page with --next-token)."""
    body = _event_summary_body(
        sort=sort,
        category=category,
        subcategory=subcategory,
        next_token=next_token,
        include_resolved=include_resolved,
        created_within_days=created_within_days,
        event_symbols=event_symbols,
        frequencies=frequencies,
        resolution_start=resolution_start,
        resolution_end=resolution_end,
    )
    result = _call(ctx, "POST", "/userapigateway/eventcontract/summary", json_body=body)
    _print(ctx, result, table="event_summaries")


@event_contracts_app.command("details")
def event_contracts_details(
    ctx: typer.Context,
    event_symbol: Annotated[
        str,
        typer.Argument(
            help="The eventSymbol from `event-contracts summary`, e.g. KALSHI.KXBALANCESHEET-EO26."
        ),
    ],
    all_outcomes: Annotated[
        bool,
        typer.Option(
            "--all-outcomes/--no-all-outcomes",
            help="Return every outcome (default) or only a short list of up to 8.",
        ),
    ] = True,
) -> None:
    """Show an event's outcomes, YES/NO contract prices, timeline, and CFTC terms."""
    result = _call(
        ctx,
        "GET",
        f"/userapigateway/eventcontract/details/{event_symbol.strip().upper()}",
        params={"includeAllOutcomes": all_outcomes},
    )
    _print(ctx, result, table="event_details")


@taxlots_app.command("list")
def taxlots_list(
    ctx: typer.Context,
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(ctx, "GET", f"/userapigateway/trading/{account_id}/taxlots/unrealized")
    _print(ctx, result)


@taxlots_app.command("symbol")
def taxlots_symbol(
    ctx: typer.Context,
    symbol: Annotated[str, typer.Argument()],
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    price: Annotated[
        str | None,
        typer.Option("--price", help="Optional price used to value the lots."),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(
        ctx,
        "GET",
        f"/userapigateway/trading/{account_id}/taxlots/unrealized/{symbol.upper()}",
        params={"price": price},
    )
    _print(ctx, result)


@taxlots_app.command("csv")
def taxlots_csv(
    ctx: typer.Context,
    account_id: Annotated[
        str | None,
        typer.Option("--account-id", "-a", help="Account ID. Defaults to configured account."),
    ] = None,
    output: Annotated[
        Path | None,
        typer.Option(
            "--output",
            "-o",
            help="Write the decoded CSV file to this path instead of printing the response.",
        ),
    ] = None,
) -> None:
    account_id = _resolve_account_id(ctx, account_id)
    result = _call(ctx, "GET", f"/userapigateway/trading/{account_id}/taxlots/csv/unrealized")
    if output is not None:
        base64_data = result.get("base64Data") if isinstance(result, dict) else None
        if not isinstance(base64_data, str) or not base64_data:
            exit_with_error("Response did not contain base64Data to write.")
        output.write_bytes(base64.b64decode(base64_data))
        console.print(f"Tax lots CSV written to {output}.")
        return
    _print(ctx, result)


def main() -> None:
    app()
