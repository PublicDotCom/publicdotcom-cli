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
public instruments bonds --bond-type TREASURY --rating AAA
public market quotes AAPL MSFT --type EQUITY
public market bond-details 912828XG0-BOND
public market option-expirations AAPL
public market option-chain AAPL 2026-05-15
public options greeks "AAPL  260515C00200000"
public options strategy-quote --file examples/strategy-quote.request.json
public historicdata bars EQUITY AAPL YEAR
public historicdata bars EQUITY AAPL DAY --aggregation FIVE_MINUTES
public historicdata bars EQUITY AAPL SINCE_PURCHASE --purchase-date 2024-01-15
public historicdata bars EQUITY RDDT FIVE_YEARS --ipo-date 2024-03-21
public historicdata event-contract-bars KALSHI.KXBALANCESHEET-EO26-EVENT WEEK --symbol KALSHI.KXBALANCESHEET-EO26-6.6.Y-EVENTCONTRACT
public taxlots list
public taxlots symbol AAPL
public taxlots csv --output taxlots.csv
```

## Historic Bar Data

Fetch OHLCV bar data for a symbol over a given time period. The first argument is the instrument type (`EQUITY`, `CRYPTO`, `OPTION`, `INDEX`, or `EVENTCONTRACT`):

```bash
public historicdata bars EQUITY AAPL YEAR
public historicdata bars CRYPTO BTC-USD WEEK
```

Available periods: `DAY`, `WEEK`, `MONTH`, `QUARTER`, `HALF_YEAR`, `YEAR`, `FIVE_YEARS`, `YTD`, `SINCE_PURCHASE`.

Override the default bar aggregation with `--aggregation`:

```bash
public historicdata bars EQUITY AAPL DAY --aggregation FIVE_MINUTES
public historicdata bars EQUITY AAPL MONTH --aggregation ONE_HOUR
```

Available aggregations: `ONE_MINUTE`, `FIVE_MINUTES`, `TEN_MINUTES`, `FIFTEEN_MINUTES`, `THIRTY_MINUTES`, `ONE_HOUR`, `ONE_DAY`, `ONE_WEEK`, `ONE_MONTH`, `THREE_MONTHS`, `SIX_MONTHS`, `ONE_YEAR`.

When using the `SINCE_PURCHASE` period, supply the purchase date:

```bash
public historicdata bars EQUITY AAPL SINCE_PURCHASE --purchase-date 2024-01-15
```

For recently listed assets, pass the IPO / first-trade date with `--ipo-date`. When the asset is younger than the requested period, the backend switches to a finer aggregation over the available post-IPO history and the response includes a `leadingFill` object describing the flat lead-in to draw for the pre-IPO portion. Omitting the option leaves behavior unchanged, and it is not applied to the `DAY` chart:

```bash
public historicdata bars EQUITY RDDT FIVE_YEARS --ipo-date 2024-03-21
```

### Event Contract Charts

`historicdata event-contract-bars EVENT_ID PERIOD` fetches chart bars for up to 8
prediction-market contracts belonging to one event. `EVENT_ID` is the `-EVENT` grouping
id; pass each `-EVENTCONTRACT` symbol with `--symbol` (repeat it, or comma-separate).
`PERIOD` is `DAY`, `WEEK`, `MONTH`, or `ALL`:

```bash
public historicdata event-contract-bars KALSHI.KXBALANCESHEET-EO26-EVENT WEEK \
  --symbol KALSHI.KXBALANCESHEET-EO26-6.6.Y-EVENTCONTRACT \
  --symbol KALSHI.KXBALANCESHEET-EO26-6.6.N-EVENTCONTRACT
```

The table shows each symbol's current and previous-close price, total gain/loss, bar
count and first/last bar timestamps; use `--json` for the bars themselves. Prices are
dollars from `0.00` to `1.00` for the side the symbol names (a `.N` symbol carries the NO
prices), i.e. the implied probability — multiply by 100 for cents or percent. Periods
are measured back from now, or from the event's close time once it has stopped trading.
Bars start at the first period with a price, so align charts by timestamp rather than
index; symbols with no data in the period are omitted from the response.

Trading requests use JSON files so the exact payload is visible before submission:

```bash
public order preflight-single --file examples/order.single-leg.market-buy.json
public order place --file examples/order.single-leg.market-buy.json
public order replace --file examples/order.replace.notional.json
public order get ORDER_ID
public order cancel ORDER_ID
public order search --status FILLED --created-after 2026-09-01T00:00:00Z
```

Trading commands prompt before submitting order placement, replacement, or cancellation
requests. Use `--yes` only when your automation has already performed equivalent
validation and approval.

Order payloads accept optional fields beyond the basics shown above. For example,
`useMargin` controls buying power on `order place` and `order place-multileg`: set it to
`false` to evaluate the order against cash-only buying power instead of margin. When
omitted it defaults to `true` (margin applied where the account allows). See
`examples/order.single-leg.cash-only.json` for a sample.

Order-placement and single-leg preflight payloads also accept an optional
`taxLotMatchingInstructions` array (up to 8 entries of `{taxLotId, quantity}`) to specify
which tax lots to close when selling equity. See
`examples/order.single-leg.tax-lot-matching.json` for a sample.

### Bracket Orders

`order place` accepts bracket orders — an entry order with take-profit and/or stop-loss
exit legs that are placed automatically when the entry fills. Set `orderClass` to
`BRACKET`, `OCO` or `OTO` in the request file, or pass the flags:

```bash
public order place --file examples/order.single-leg.bracket.json

public order place --file examples/order.single-leg.market-buy.json \
  --order-class BRACKET --take-profit-limit 245.00 --stop-loss-stop 210.00

# STOP_LIMIT stop-loss instead of a plain STOP
public order place --file examples/order.single-leg.market-buy.json \
  --order-class OTO --stop-loss-stop 210.00 --stop-loss-limit 209.50
```

`--order-class`, `--take-profit-limit`, `--stop-loss-stop` and `--stop-loss-limit`
override `orderClass`, `takeProfit` and `stopLoss` in the request file. A bracket class
needs at least one exit leg, and exit legs need a bracket class — the CLI checks both
before submitting.

| Class | Meaning |
|---|---|
| `SIMPLE` (or omitted) | Standalone order — no exit legs. |
| `BRACKET` | Entry with take-profit and/or stop-loss exits. |
| `OCO` | One-cancels-other exits; the entry must be a `LIMIT` order. |
| `OTO` | One-triggers-other — the entry triggers the attached exit. |

The API enforces the remaining constraints: equities and options only, a whole-share
`quantity` (no `amount`), the `CORE` market session, and a `LIMIT` or `MARKET` entry
order type (`LIMIT` only for `OCO`). Responses from `order get` carry a `bracketId` —
the entry order's id, shared by every leg of the bracket, and absent on standalone
orders. See `examples/order.single-leg.bracket.json` for a full sample payload.

Bracket legs have their own replacement rules: the entry order cannot be replaced, and
the closing legs accept `limitPrice` / `stopPrice` replacements only — resubmit
`quantity`, `orderType` and `expiration` unchanged.

`order replace` submits a cancel-replace request for an open order. The replacement can
specify either a `quantity` or a notional `amount` — the two fields are mutually
exclusive. `--quantity` and `--amount` override the corresponding field in the request
file. Replacement is supported for equity, option, and crypto quantity orders, and is
asynchronous: verify order status after submitting. See
`examples/order.replace.notional.json` for a sample notional replacement payload.

```bash
public order replace --file examples/order.replace.notional.json
public order replace --file examples/order.replace.notional.json --amount 250.00
```

### Order Search

`order search` queries the last 30 days of orders (up to 500) and renders them as a
table. Combine any of the filters, or pass none to list everything:

```bash
public order search
public order search --status FILLED --side BUY --created-after 2026-09-01T00:00:00Z
public order search --symbol AAPL --symbol SPY:OPTION --open-close OPEN
public --json order search --security-type MULTI_LEG_INSTRUMENT
```

`--symbol` takes `SYMBOL` or `SYMBOL:TYPE` (the type defaults to `EQUITY`) and can be
repeated. `--status`, `--side`, `--security-type` (including `EVENTCONTRACT`) and
`--open-close` accept the values from the API spec, case-insensitively;
`--created-after` and `--created-before` are ISO 8601 timestamps. Each order includes
`trades` (each with `tradeId`, `price`, `quantity`, `side`, `timestamp`), `filledAt`,
`replacedAt`, `lastModified` and `equityMarketSession`.

`order get ORDER_ID` returns a single order in that same shape. Both commands only cover
orders created within the last 30 days. The 1.3.5 `order get-v2` command is now a
deprecated, hidden alias for `order get` (the separate v2 endpoints were removed from the
API) and will be dropped in a future release.

## Tax Lots

Inspect unrealized tax lots for the configured (or `--account-id`) account:

```bash
public taxlots list
public taxlots symbol AAPL
public taxlots symbol AAPL --price 150.00
```

`taxlots symbol` accepts an optional `--price` used to value the lots. Export the full set
as CSV — by default the base64-encoded response is printed, or pass `--output` to decode
and write the CSV file directly:

```bash
public taxlots csv
public taxlots csv --output taxlots.csv
```

## Strategy Quote

Request a quote for a multi-leg options strategy from a JSON request file:

```bash
public options strategy-quote --file examples/strategy-quote.request.json
```

The request body is a `StrategyQuoteRequest` with a `baseSymbol` and an `optionLegs` array
(each leg is `{symbol, side, openCloseIndicator, ratioQuantity}`), plus an optional
`equityLeg`. See `examples/strategy-quote.request.json` for a sample.

## Bonds

Search fixed income instruments with optional filtering, sorting, and pagination:

```bash
public instruments bonds
public instruments bonds --bond-type TREASURY --treasury-subtype NOTE --min-coupon 4
public instruments bonds --rating AAA --rating AA+ --max-maturity-date 2030-12-31
public instruments bonds --page-size 50 --sort-property maturityDate --sort-direction ASC
```

Filters cover issuer, bond status/type, treasury subtype, S&P ratings and outlook,
coupon, maturity dates, current yield, par value, liquidity rating, and
callable/perpetual/partial-par flags. Repeatable options (for example `--rating`) can be
passed multiple times. Results are returned as a page with `content` plus paging
metadata. The API defaults the minimum maturity date to today + 14 days to exclude bonds
nearing maturity with volatile yields; pass `--min-maturity-date` to override.

Retrieve comprehensive details for a single bond — pricing, ratings, coupon, and
maturity/call information — using the configured (or `--account-id`) account. The bond
symbol is typically in `CUSIP-BOND` format:

```bash
public market bond-details 912828XG0-BOND
```

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
