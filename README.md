# publicdotcom-cli

Command-line client for the Public.com Trading API.

Use `public` to authenticate, inspect accounts, retrieve portfolio and market data, run
preflight checks, and submit order-related requests from your terminal.

## Install

The recommended installation method for command-line Python tools is `pipx`:

```bash
pipx install publicdotcom-cli
```

You can also install with `uv`:

```bash
uv tool install publicdotcom-cli
```

Confirm the CLI is available:

```bash
public --help
```

## Quick Start

Generate a personal secret from your Public.com settings, then authenticate:

```bash
public auth login
public accounts list
public accounts set-default ACCOUNT_ID
public portfolio show
public market quotes AAPL MSFT
```

Most account-scoped commands use the configured default account. You can override it with
`--account-id ACCOUNT_ID` or `PUBLIC_ACCOUNT_ID=ACCOUNT_ID`.

## Important Disclosures

This CLI is a developer tool for interacting with the Public API. It is not investment,
financial, legal, tax, accounting, or trading advice, and it does not recommend any
security, strategy, account type, order type, or transaction.

Trading involves risk, including the possible loss of principal. You are responsible for
reviewing all request payloads, account IDs, symbols, quantities, prices, order sides,
time-in-force values, and other order instructions before submitting a trading command.

Order placement, replacement, and cancellation requests may be asynchronous. A successful
API response confirms submission to the API, not execution, cancellation, fill price,
availability, or final order state. Always verify order status after submitting,
replacing, or cancelling an order.

Market data, quotes, option chains, greeks, account data, and preflight calculations are
provided for informational and operational use through the API. They may be incomplete,
delayed, unavailable, or different from final execution values.

You are responsible for complying with all applicable laws, regulations, exchange rules,
API terms, account agreements, and internal policies that apply to your use of this CLI.
Do not use this tool unless you are authorized to access the relevant account and API
credentials.

Personal secrets and access tokens can authorize account access and trading activity.
Keep them private, do not commit them to source control, and rotate or revoke them if
you believe they were exposed.

## Authenticate

Generate a personal secret from Public, then run:

```bash
public auth login
```

The access token is stored with your OS keychain when available. If no keychain backend
is available, the CLI falls back to a user-only config file.

Access tokens are short-lived. To let the CLI refresh them automatically, opt in to
storing your personal secret:

```bash
public auth login --store-secret
```

Because the personal secret is long-lived, this is optional. The CLI stores it in your
OS keychain when available, otherwise it falls back to a user-only config file.

After that, secured commands automatically mint a fresh access token before the current
token expires or after a `401 Unauthorized` response. You can also refresh manually:

```bash
public auth refresh
```

You can also bypass stored credentials for automation:

```bash
PUBLIC_ACCESS_TOKEN=ey... public accounts list
PUBLIC_PERSONAL_SECRET=... public accounts list
```

Remove stored credentials with:

```bash
public auth logout
public auth logout --all
```

## Default Account

Most API operations require the `accountId` returned by `public accounts list`. You can
store a default account once:

```bash
public accounts set-default ACCOUNT_ID
public accounts get-default
```

Then omit `--account-id` from account-scoped commands:

```bash
public portfolio show
public market quotes AAPL MSFT
public order get ORDER_ID
```

You can override the default at any time:

```bash
public portfolio show --account-id ACCOUNT_ID
PUBLIC_ACCOUNT_ID=ACCOUNT_ID public portfolio show
public accounts clear-default
```

## Example Commands

```bash
public accounts list
public accounts set-default ACCOUNT_ID
public portfolio show
public history list --page-size 25
public instruments get AAPL EQUITY
public market quotes AAPL MSFT --type EQUITY
public market option-expirations AAPL
public market option-chain AAPL 2026-05-15
public options greeks "AAPL  260515C00200000"
public historicdata bars AAPL YEAR
public historicdata bars AAPL DAY --aggregation FIVE_MINUTES
public historicdata bars AAPL SINCE_PURCHASE --purchase-date 2024-01-15
```

## Historic Bar Data

Fetch OHLCV bar data for a symbol over a given time period:

```bash
public historicdata bars AAPL YEAR
public historicdata bars BTC-USD WEEK
```

Available periods: `DAY`, `WEEK`, `MONTH`, `QUARTER`, `HALF_YEAR`, `YEAR`, `FIVE_YEARS`, `YTD`, `SINCE_PURCHASE`.

Override the default bar aggregation with `--aggregation`:

```bash
public historicdata bars AAPL DAY --aggregation FIVE_MINUTES
public historicdata bars AAPL MONTH --aggregation ONE_HOUR
```

Available aggregations: `ONE_MINUTE`, `FIVE_MINUTES`, `TEN_MINUTES`, `FIFTEEN_MINUTES`, `THIRTY_MINUTES`, `ONE_HOUR`, `ONE_DAY`, `ONE_WEEK`, `ONE_MONTH`, `THREE_MONTHS`, `SIX_MONTHS`, `ONE_YEAR`.

When using the `SINCE_PURCHASE` period, supply the purchase date:

```bash
public historicdata bars AAPL SINCE_PURCHASE --purchase-date 2024-01-15
```

Trading requests use JSON files so the exact payload is visible before submission:

```bash
public order preflight-single --file examples/order.single-leg.market-buy.json
public order place --file examples/order.single-leg.market-buy.json
public order get ORDER_ID
public order cancel ORDER_ID
```

Trading commands prompt before submitting order placement, replacement, or cancellation
requests. Use `--yes` only when your automation has already performed equivalent
validation and approval.

## JSON Output

Use `--json` before the command group to print raw JSON:

```bash
public --json accounts list
public --json market quotes AAPL MSFT
```

## Configuration

The CLI supports these environment variables:

```bash
PUBLIC_ACCESS_TOKEN=...
PUBLIC_PERSONAL_SECRET=...
PUBLIC_ACCOUNT_ID=...
PUBLIC_API_BASE_URL=https://api.public.com
PUBLIC_AUTO_REFRESH=true
```

`PUBLIC_API_BASE_URL` is optional and defaults to `https://api.public.com`.

## Upgrade

```bash
pipx upgrade publicdotcom-cli
# or
uv tool upgrade publicdotcom-cli
```

## Development

For local development from a checkout:

```bash
uv sync --extra dev
uv run public --help
uv run pytest
```

## Regenerate The OpenAPI Client

The package ships with a generated API client. Contributors who need to regenerate it
must place the local OpenAPI spec at the repository root as `spec.yaml`, then run:

```bash
uv run python scripts/generate_client.py
```

The raw spec uses `*/*` for many JSON responses, which some Python generators do not
parse as JSON. The regeneration script normalizes those response content types before
running `openapi-python-client`. This requires network access the first time because it
uses `uvx openapi-python-client`.
