from __future__ import annotations

import json
import sys
import uuid
from pathlib import Path
from typing import Any, Iterable


def load_json_file(path: Path) -> Any:
    if str(path) == "-":
        raw = sys.stdin.read()
    else:
        raw = path.read_text(encoding="utf-8")

    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def instrument(symbol: str, security_type: str) -> dict[str, str]:
    return {"symbol": symbol.upper(), "type": security_type.upper()}


def instruments(symbols: Iterable[str], security_type: str) -> list[dict[str, str]]:
    return [instrument(symbol, security_type) for symbol in symbols]


def instrument_spec(value: str, default_type: str = "EQUITY") -> dict[str, str]:
    """Parse a `SYMBOL` or `SYMBOL:TYPE` flag value into an instrument payload."""
    symbol, separator, security_type = value.partition(":")
    symbol = symbol.strip()
    security_type = security_type.strip() if separator else default_type
    if not symbol or not security_type:
        raise ValueError(f"Invalid instrument {value!r}. Expected SYMBOL or SYMBOL:TYPE.")
    return instrument(symbol, security_type)


def ensure_order_id(body: dict[str, Any]) -> str:
    order_id = body.get("orderId")
    if isinstance(order_id, str) and order_id:
        return order_id
    order_id = str(uuid.uuid4())
    body["orderId"] = order_id
    return order_id
