from publicdotcom_cli._generated.models import (
    BarsResponse,
    ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest as CancelReplaceOrderRequest,
    LeadingFill,
)

REPLACE_REQUEST = {
    "orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc",
    "requestId": "9b2f8a64-6f19-4c8e-9a5d-0e8b1c2d3e4f",
    "orderType": "MARKET",
    "expiration": {"timeInForce": "DAY"},
}


def test_cancel_replace_request_round_trips_amount() -> None:
    request = CancelReplaceOrderRequest.from_dict({**REPLACE_REQUEST, "amount": "100.00"})

    assert request.amount == "100.00"
    assert request.to_dict()["amount"] == "100.00"
    assert "quantity" not in request.to_dict()


def test_cancel_replace_request_round_trips_quantity() -> None:
    request = CancelReplaceOrderRequest.from_dict({**REPLACE_REQUEST, "quantity": "5"})

    assert request.quantity == "5"
    assert request.to_dict()["quantity"] == "5"
    assert "amount" not in request.to_dict()


BARS_RESPONSE = {
    "symbol": "RDDT",
    "period": "FIVE_YEARS",
    "totalExpectedBars": 260,
    "preMarket": {"expectedBars": 0, "bars": []},
    "regularMarket": {"expectedBars": 260, "bars": []},
    "afterMarket": {"expectedBars": 0, "bars": []},
}

LEADING_FILL = {
    "startTimestamp": "2021-08-11T13:30:00Z",
    "endTimestamp": "2024-03-21T13:30:00Z",
    "value": "50.44",
    "count": 135,
    "includedInTotalExpectedBars": False,
}


def test_bars_response_round_trips_leading_fill() -> None:
    response = BarsResponse.from_dict({**BARS_RESPONSE, "leadingFill": LEADING_FILL})

    assert isinstance(response.leading_fill, LeadingFill)
    assert response.leading_fill.start_timestamp == "2021-08-11T13:30:00Z"
    assert response.leading_fill.end_timestamp == "2024-03-21T13:30:00Z"
    assert response.leading_fill.value == "50.44"
    assert response.leading_fill.count == 135
    assert response.leading_fill.included_in_total_expected_bars is False
    assert response.to_dict()["leadingFill"] == LEADING_FILL


def test_bars_response_omits_leading_fill_when_absent() -> None:
    response = BarsResponse.from_dict(BARS_RESPONSE)

    assert "leadingFill" not in response.to_dict()
