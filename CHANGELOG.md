# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.2] - 2026-08-05

### Added
- `public instruments bonds` command covering the new
  `GET /userapigateway/trading/instruments/bonds` endpoint: paged, filtered
  fixed-income search with options for issuer, bond status/type, treasury
  subtype, S&P rating/outlook/creditwatch, coupon, maturity dates, current
  yield, par value, liquidity rating, and callable/perpetual/partial-par flags.
- `public market bond-details SYMBOL` command covering the new
  `GET /userapigateway/marketdata/{accountId}/bond-details/{symbol}` endpoint,
  returning comprehensive bond pricing, rating, coupon, and maturity/call data.
- `--quantity` and `--amount` overrides on `public order replace`, mirroring the
  cancel-replace request schema's new notional `amount` field. The two are
  mutually exclusive (enforced before submission, including when both fields
  appear in the request file). Replacement is now supported for equity, option,
  and crypto quantity orders.
- `examples/order.replace.notional.json` demonstrating a notional (`amount`)
  cancel-replace payload.
- README sections for bond search, bond details, and order replacement.

### Changed
- Regenerated `_generated/` from the updated `spec.yaml`:
  - New `search-bonds` and `get-bond-details` endpoint modules and models
    (`InstrumentDto`, `BondDetailsResponse`, Spring page/pageable/sort, and the
    bond search filter enums).
  - `amount` added to `ApiCancelReplaceOrderRequest` (mutually exclusive with
    `quantity`).
  - `AGGREGATE` added to the tax-lot `OutOfDateStatus` `type` enum.
  - Refreshed endpoint docstrings (instruments list/get, quotes, greeks,
    history, replace-order) to match the updated spec text; `get-instrument`
    now documents 400/404 responses.
- `scripts/generate_client.py` now injects `x-enum-varnames` for enum values
  that collide after sanitization (e.g. S&P ratings `AA+`/`AA`/`AA-`), which
  the bonds `rating` filter requires for generation to succeed.

## [1.3.1] - 2026-07-24

### Changed
- Regenerated `_generated/` API client from the updated `spec.yaml`:
  - `ENTITY` added to the `accountType` enums on `GatewayPortfolioAccountV2` and
    `AccountSettings`. Additive and non-breaking — the CLI treats `accountType`
    as an opaque string (`public accounts` renders it in a table, `public
    portfolio` emits raw JSON), so entity accounts already display correctly.
  - The three `taxlots` endpoints now document `trading.read` (was `portfolio`)
    as their required scope, matching the corrected spec. Behaviour is
    unchanged; only the stated scope was wrong.

### Added
- `tests/test_generated_enums.py` asserting both regenerated `accountType`
  enums parse `ENTITY` and match the spec's full member set.
- `tests/test_output.py` covering `print_accounts` rendering of an `ENTITY`
  account, guarding against a future regression to strict enum parsing.

## [1.3.0] - 2026-07-20

### Added
- `public taxlots` command group covering the new unrealized tax-lot endpoints:
  `taxlots list` (`GET /userapigateway/trading/{accountId}/taxlots/unrealized`),
  `taxlots symbol SYMBOL [--price]`
  (`GET /userapigateway/trading/{accountId}/taxlots/unrealized/{symbol}`), and
  `taxlots csv [--output PATH]`
  (`GET /userapigateway/trading/{accountId}/taxlots/csv/unrealized`), which can
  decode the returned base64 CSV to a file.
- `public options strategy-quote --file FILE` command covering
  `POST /userapigateway/option-details/{accountId}/strategy-details/quote`.
- `examples/order.single-leg.tax-lot-matching.json` demonstrating the optional
  `taxLotMatchingInstructions` field now accepted on order-placement and
  single-leg preflight request payloads.
- `examples/strategy-quote.request.json` sample `StrategyQuoteRequest` body.
- README sections documenting the tax-lot and strategy-quote commands.

### Changed
- Regenerated `_generated/` API client from the updated `spec.yaml`.

## [1.2.1] - 2026-06-17

### Added
- `examples/order.single-leg.cash-only.json` demonstrating the optional `useMargin`
  field, which controls whether margin or cash-only buying power is used when placing
  single-leg and multi-leg orders. Documented in README.

### Changed
- `public historicdata bars` help text now lists the `TEN_YEARS` and `ALL` period
  values added in the updated API spec.

## [1.2.0] - 2026-05-14

### Changed
- **Breaking:** `public historicdata bars` now requires a leading `SECURITY_TYPE`
  positional argument (`EQUITY`, `CRYPTO`, `OPTION`, or `INDEX`) to match the
  updated `/userapigateway/historicdata/{type}/{symbol}/{period}` spec. Existing
  invocations like `public historicdata bars AAPL YEAR` must become
  `public historicdata bars EQUITY AAPL YEAR`.
- Regenerated `_generated/` API client from `spec.yaml`; the bar endpoints now
  land under `_generated/api/market_data/` as `get_bars_v2` and
  `get_bars_v2_with_aggregation`.
- README quick-reference and Historic Bar Data section updated for the new
  argument order.

### Added
- `LICENSE` file containing the Apache License, Version 2.0 text (the project
  was already declared as Apache-2.0 in `pyproject.toml`).

## [1.1.0] - 2026-05-06

### Added
- `public historicdata bars` command covering
  `GET /userapigateway/historicdata/{symbol}/{period}` and
  `GET /userapigateway/historicdata/{symbol}/{period}/{aggregation}`, with
  `--aggregation` and `--purchase-date` options.
- README section documenting historic bar data usage.

## [1.0.0] - 2026-04-29

### Added
- First tagged release of the CLI.

## [0.1.0] - 2026-04-29

### Added
- Initial commit: CLI scaffolding, generated API client from `spec.yaml`,
  authentication, accounts, portfolio, history, instruments, market data,
  option details, and order placement commands.
