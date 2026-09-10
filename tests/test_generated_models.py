from publicdotcom_cli._generated.models import (
    BarsResponse,
    ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest as CancelReplaceOrderRequest,
    ComHellopublicUserapigatewayApiRestOrderApiOrderRequest as OrderRequest,
    ComHellopublicUserapigatewayApiRestOrderApiOrderRequestOrderClass as OrderClass,
    ComHellopublicUserapigatewayApiRestOrderGatewayOrder as GatewayOrder,
    ComHellopublicUserapigatewayApiRestOrderGatewayStopLoss as StopLoss,
    ComHellopublicUserapigatewayApiRestOrderGatewayTakeProfit as TakeProfit,
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


BRACKET_ORDER_REQUEST = {
    "orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc",
    "instrument": {"symbol": "AAPL", "type": "EQUITY"},
    "orderSide": "BUY",
    "orderType": "LIMIT",
    "expiration": {"timeInForce": "DAY"},
    "quantity": 10,
}


def test_take_profit_round_trips() -> None:
    take_profit = TakeProfit.from_dict({"limitPrice": "245.00"})

    assert take_profit.limit_price == "245.00"
    assert take_profit.to_dict() == {"limitPrice": "245.00"}


def test_stop_loss_round_trips_stop_only() -> None:
    stop_loss = StopLoss.from_dict({"stopPrice": "210.00"})

    assert stop_loss.stop_price == "210.00"
    assert stop_loss.to_dict() == {"stopPrice": "210.00"}


def test_stop_loss_round_trips_stop_limit() -> None:
    stop_loss = StopLoss.from_dict({"stopPrice": "210.00", "limitPrice": "209.50"})

    assert stop_loss.limit_price == "209.50"
    assert stop_loss.to_dict() == {"stopPrice": "210.00", "limitPrice": "209.50"}


def test_order_request_round_trips_bracket_fields() -> None:
    request = OrderRequest.from_dict(
        {
            **BRACKET_ORDER_REQUEST,
            "orderClass": "BRACKET",
            "takeProfit": {"limitPrice": "245.00"},
            "stopLoss": {"stopPrice": "210.00"},
        }
    )

    assert request.order_class == OrderClass.BRACKET
    payload = request.to_dict()
    assert payload["orderClass"] == "BRACKET"
    assert payload["takeProfit"] == {"limitPrice": "245.00"}
    assert payload["stopLoss"] == {"stopPrice": "210.00"}


def test_order_request_omits_bracket_fields_when_absent() -> None:
    payload = OrderRequest.from_dict(BRACKET_ORDER_REQUEST).to_dict()

    assert "orderClass" not in payload
    assert "takeProfit" not in payload
    assert "stopLoss" not in payload


def test_gateway_order_round_trips_bracket_id() -> None:
    order = GatewayOrder.from_dict(
        {
            "orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc",
            "bracketId": "0d2abd8d-3625-4c83-a806-98abf35567cc",
        }
    )

    assert str(order.bracket_id) == "0d2abd8d-3625-4c83-a806-98abf35567cc"
    assert order.to_dict()["bracketId"] == "0d2abd8d-3625-4c83-a806-98abf35567cc"


def test_gateway_order_omits_bracket_id_for_standalone_orders() -> None:
    order = GatewayOrder.from_dict({"orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc"})

    assert "bracketId" not in order.to_dict()
