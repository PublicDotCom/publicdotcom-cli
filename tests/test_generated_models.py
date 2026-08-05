from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest as CancelReplaceOrderRequest,
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
