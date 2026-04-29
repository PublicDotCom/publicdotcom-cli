# publicdotcom-cli

An installable Python CLI for the Public API.

The project keeps a vendored OpenAPI-generated client in `src/publicdotcom_cli/_generated`,
and the user-facing CLI wraps the API with safer terminal workflows, secure token storage,
JSON output, and confirmation prompts for trading actions.

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

## Install

From this checkout:

```bash
uv tool install .
```

During development:

```bash
uv sync --extra dev
uv run public --help
```

Once published to PyPI, users can install it with:

```bash
pipx install publicdotcom-cli
```

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

## Regenerate The OpenAPI Client

The OpenAPI spec is not committed to this repository. To regenerate the vendored client,
place the spec at the repository root as `spec.yaml`, then run:

```bash
uv run python scripts/generate_client.py
```

The raw spec uses `*/*` for many JSON responses, which some Python generators do not
parse as JSON. The regeneration script normalizes those response content types before
running `openapi-python-client`. This requires network access the first time because it
uses `uvx openapi-python-client`.
