import pytest

from publicdotcom_cli.payloads import ensure_order_id, instrument, instrument_spec, instruments


def test_instrument_payload_uppercases_values() -> None:
    assert instrument("aapl", "equity") == {"symbol": "AAPL", "type": "EQUITY"}


def test_instruments_payload_reuses_type_for_each_symbol() -> None:
    assert instruments(["aapl", "msft"], "equity") == [
        {"symbol": "AAPL", "type": "EQUITY"},
        {"symbol": "MSFT", "type": "EQUITY"},
    ]


def test_ensure_order_id_preserves_existing_id() -> None:
    body = {"orderId": "existing"}
    assert ensure_order_id(body) == "existing"
    assert body == {"orderId": "existing"}


def test_ensure_order_id_adds_missing_id() -> None:
    body = {}
    order_id = ensure_order_id(body)
    assert body["orderId"] == order_id
    assert len(order_id) == 36


def test_instrument_spec_defaults_type_to_equity() -> None:
    assert instrument_spec("aapl") == {"symbol": "AAPL", "type": "EQUITY"}


def test_instrument_spec_parses_symbol_and_type() -> None:
    assert instrument_spec("spy:option") == {"symbol": "SPY", "type": "OPTION"}


def test_instrument_spec_rejects_missing_symbol_or_type() -> None:
    for value in (":OPTION", "AAPL:", ""):
        with pytest.raises(ValueError):
            instrument_spec(value)
