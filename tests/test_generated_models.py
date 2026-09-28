from publicdotcom_cli._generated.api.order_placement import get_order, search_orders
from publicdotcom_cli._generated.models import (
    BarsResponse,
    ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequest as CancelReplaceOrderRequest,
    ComHellopublicUserapigatewayApiRestOrderApiOrderRequest as OrderRequest,
    ComHellopublicUserapigatewayApiRestOrderApiOrderRequestOrderClass as OrderClass,
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequest as QueryOrdersRequest,
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSecurityType as QueryOrdersSecurityType,
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestStatus as QueryOrdersStatus,
    ComHellopublicUserapigatewayApiRestOrderGatewayOrder as GatewayOrder,
    ComHellopublicUserapigatewayApiRestOrderGatewayStopLoss as StopLoss,
    ComHellopublicUserapigatewayApiRestOrderGatewayTakeProfit as TakeProfit,
    ComHellopublicUserapigatewayApiRestOrderV2GatewayOrders as GatewayOrders,
    ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2 as GatewayOrderV2,
    ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2EquityMarketSession as OrderV2EquityMarketSession,
    ComHellopublicUserapigatewayApiRestOrderV2GatewayTrade as GatewayTrade,
    EventContractChart,
    EventContractChartsResponse,
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


ORDER_V2 = {
    "orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc",
    "instrument": {"symbol": "AAPL", "type": "EQUITY"},
    "createdAt": "2026-09-21T14:30:00+00:00",
    "type": "LIMIT",
    "side": "BUY",
    "status": "FILLED",
    "quantity": "10",
    "expiration": {"timeInForce": "DAY"},
    "limitPrice": "245.00",
    "filledQuantity": "10",
    "averagePrice": "244.90",
    "equityMarketSession": "REGULAR",
    "filledAt": "2026-09-21T14:30:05+00:00",
    "replacedAt": "2026-09-21T14:29:00+00:00",
    "lastModified": "2026-09-21T14:30:05+00:00",
    "trades": [
        {
            "instrument": {"symbol": "AAPL", "type": "EQUITY"},
            "quantity": "10",
            "price": "244.90",
            "side": "BUY",
            "tradeId": "trade-1",
            "timestamp": "2026-09-21T14:30:05+00:00",
        }
    ],
}


def test_gateway_order_v2_round_trips_v2_fields() -> None:
    order = GatewayOrderV2.from_dict(ORDER_V2)

    assert order.equity_market_session == OrderV2EquityMarketSession.REGULAR
    assert order.filled_at.isoformat() == "2026-09-21T14:30:05+00:00"
    assert order.replaced_at.isoformat() == "2026-09-21T14:29:00+00:00"
    assert order.last_modified.isoformat() == "2026-09-21T14:30:05+00:00"
    assert len(order.trades) == 1
    assert isinstance(order.trades[0], GatewayTrade)
    assert order.trades[0].trade_id == "trade-1"
    assert order.trades[0].price == "244.90"
    assert order.to_dict() == ORDER_V2


def test_gateway_order_v2_omits_v2_fields_when_absent() -> None:
    payload = GatewayOrderV2.from_dict(
        {"orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc", "status": "NEW"}
    ).to_dict()

    for key in ("trades", "filledAt", "replacedAt", "lastModified", "equityMarketSession"):
        assert key not in payload


def test_gateway_orders_round_trips_list() -> None:
    orders = GatewayOrders.from_dict({"orders": [ORDER_V2]})

    assert len(orders.orders) == 1
    assert orders.orders[0].order_id == ORDER_V2["orderId"]
    assert orders.to_dict() == {"orders": [ORDER_V2]}


QUERY_ORDERS_REQUEST = {
    "status": "FILLED",
    "createdAfter": "2026-09-01T00:00:00+00:00",
    "createdBefore": "2026-09-22T00:00:00+00:00",
    "instruments": [{"symbol": "AAPL", "type": "EQUITY"}],
    "side": "BUY",
    "openCloseIndicator": "OPEN",
    "securityType": "EQUITY",
}


def test_query_orders_request_round_trips_all_filters() -> None:
    request = QueryOrdersRequest.from_dict(QUERY_ORDERS_REQUEST)

    assert request.status == QueryOrdersStatus.FILLED
    assert request.security_type == QueryOrdersSecurityType.EQUITY
    assert request.to_dict() == QUERY_ORDERS_REQUEST


def test_query_orders_request_is_empty_without_filters() -> None:
    assert QueryOrdersRequest.from_dict({}).to_dict() == {}


def test_search_orders_module_targets_search_path() -> None:
    kwargs = search_orders._get_kwargs("acct-1", body=QueryOrdersRequest.from_dict({}))

    assert kwargs["method"] == "post"
    assert kwargs["url"] == "/userapigateway/trading/acct-1/order/search"


def test_get_order_module_parses_v2_order_shape() -> None:
    import httpx

    payload = {
        "orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc",
        "status": "FILLED",
        "equityMarketSession": "REGULAR",
        "filledAt": "2026-09-21T14:30:05+00:00",
        "trades": [{"tradeId": "trade-1", "side": "BUY", "quantity": "10", "price": "244.90"}],
    }
    response = httpx.Response(200, json=payload)

    parsed = get_order._parse_response(client=None, response=response)  # type: ignore[arg-type]

    assert isinstance(parsed, GatewayOrderV2)
    assert parsed.equity_market_session is OrderV2EquityMarketSession.REGULAR
    assert isinstance(parsed.trades[0], GatewayTrade)
    assert parsed.trades[0].trade_id == "trade-1"


def test_get_order_v2_module_was_removed() -> None:
    import importlib.util

    assert (
        importlib.util.find_spec("publicdotcom_cli._generated.api.order_placement.get_order_v2")
        is None
    )


EVENT_CONTRACT_CHARTS = {
    "period": "WEEK",
    "charts": [
        {
            "symbol": "KALSHI.KXBALANCESHEET-EO26-6.6.Y-EVENTCONTRACT",
            "previousClosePrice": "0.41",
            "currentPrice": "0.47",
            "totalGainLoss": "0.06",
            "totalGainLossPercentage": "14.63",
            "bars": [
                {
                    "timestamp": "2026-09-28T00:00:00Z",
                    "open": "0.45",
                    "close": "0.47",
                    "high": "0.48",
                    "low": "0.44",
                    "value": "0.47",
                    "volume": 900,
                }
            ],
        }
    ],
}


def test_event_contract_charts_response_round_trips() -> None:
    response = EventContractChartsResponse.from_dict(EVENT_CONTRACT_CHARTS)

    assert response.period == "WEEK"
    assert isinstance(response.charts[0], EventContractChart)
    assert response.charts[0].current_price == "0.47"
    assert response.charts[0].bars[0].close == "0.47"
    assert response.to_dict() == EVENT_CONTRACT_CHARTS


def test_event_contract_chart_keeps_null_prices() -> None:
    chart = EventContractChart.from_dict(
        {
            "symbol": "KALSHI.X-1.N-EVENTCONTRACT",
            "previousClosePrice": None,
            "currentPrice": None,
            "totalGainLoss": None,
            "totalGainLossPercentage": None,
            "bars": [],
        }
    )

    assert chart.current_price is None
    assert chart.to_dict()["currentPrice"] is None
