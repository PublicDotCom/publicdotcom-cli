from publicdotcom_cli.payloads import ensure_order_id, instrument, instruments


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
