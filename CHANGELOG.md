# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
