"""Spec sync: on-close order types, day-trade buying power and related response fields."""

import enum
import inspect
import io
import json
from pathlib import Path

import httpx
import pytest
import typer
from rich.console import Console
from typer.testing import CliRunner

from publicdotcom_cli import cli as cli_module
from publicdotcom_cli import output
from publicdotcom_cli._generated.api.order_placement import get_order, search_orders
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDto as EventOutcome,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiCancelReplaceOrderRequestOrderType as CancelReplaceOrderType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiMultilegOrderRequestType as MultilegOrderType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiOrderRequest as OrderRequest,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiOrderRequestOrderType as OrderRequestOrderType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderGatewayOrderType as GatewayOrderType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderGatewayStopLoss as StopLoss,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2 as GatewayOrderV2,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2Type as GatewayOrderV2Type,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderV2GatewayTrade as GatewayTrade,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayBuyingPower as BuyingPower,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2 as PortfolioAccountV2,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightMultiLegRequestOrderType as PreflightMultiLegOrderType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOrderType as PreflightSingleLegOrderType,
)
from publicdotcom_cli.cli import _apply_bracket_overrides, app
from publicdotcom_cli._generated.types import UNSET

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"

EXPECTED_ORDER_TYPES = {
    "MARKET",
    "LIMIT",
    "STOP",
    "STOP_LIMIT",
    "MARKET_ON_CLOSE",
    "LIMIT_ON_CLOSE",
}

ORDER_TYPE_ENUMS = (
    OrderRequestOrderType,
    CancelReplaceOrderType,
    PreflightSingleLegOrderType,
    PreflightMultiLegOrderType,
    MultilegOrderType,
    GatewayOrderType,
    GatewayOrderV2Type,
)


# --- order-type enums -----------------------------------------------------------


@pytest.mark.parametrize("enum_cls", ORDER_TYPE_ENUMS, ids=lambda cls: cls.__name__)
def test_order_type_enums_match_spec(enum_cls: type[enum.Enum]) -> None:
    assert {member.value for member in enum_cls} == EXPECTED_ORDER_TYPES


@pytest.mark.parametrize("enum_cls", ORDER_TYPE_ENUMS, ids=lambda cls: cls.__name__)
def test_order_type_enums_parse_on_close_values(enum_cls: type[enum.Enum]) -> None:
    assert enum_cls("MARKET_ON_CLOSE").value == "MARKET_ON_CLOSE"
    assert enum_cls("LIMIT_ON_CLOSE").value == "LIMIT_ON_CLOSE"
    assert str(enum_cls("LIMIT_ON_CLOSE")) == "LIMIT_ON_CLOSE"


@pytest.mark.parametrize("enum_cls", ORDER_TYPE_ENUMS, ids=lambda cls: cls.__name__)
def test_order_type_enums_stay_python_310_compatible(enum_cls: type[enum.Enum]) -> None:
    # enum.StrEnum is Python 3.11+; the vendored client must keep the (str, Enum) style.
    assert enum_cls.__bases__ == (str, enum.Enum)
    assert "StrEnum" not in inspect.getsource(inspect.getmodule(enum_cls))


def test_order_request_round_trips_limit_on_close() -> None:
    payload = {
        "orderId": "0d2abd8d-3625-4c83-a806-98abf35567cc",
        "instrument": {"symbol": "AAPL", "type": "EQUITY"},
        "orderSide": "BUY",
        "orderType": "LIMIT_ON_CLOSE",
        "expiration": {"timeInForce": "DAY"},
        "quantity": "1",
        "limitPrice": "227.50",
    }

    request = OrderRequest.from_dict(payload)

    assert request.order_type is OrderRequestOrderType.LIMIT_ON_CLOSE
    assert request.to_dict() == payload


def test_gateway_order_v2_parses_market_on_close_type() -> None:
    order = GatewayOrderV2.from_dict({"orderId": "order-1", "type": "MARKET_ON_CLOSE"})

    assert order.type_ is GatewayOrderV2Type.MARKET_ON_CLOSE


# --- stop-loss --------------------------------------------------------------------


def test_generated_stop_loss_allows_missing_stop_price() -> None:
    # The spec makes stopPrice optional (trailing stop-losses); the model mirrors that.
    stop_loss = StopLoss.from_dict({})

    assert stop_loss.stop_price is UNSET
    assert stop_loss.to_dict() == {}


def test_bracket_flags_still_require_stop_price_for_stop_loss_limit() -> None:
    # The CLI exposes no trailing fields yet, so a flag-built stop-loss always needs a stop.
    body: dict = {"instrument": {"symbol": "AAPL", "type": "EQUITY"}}

    with pytest.raises(typer.Exit):
        _apply_bracket_overrides(
            body,
            order_class="BRACKET",
            take_profit_limit=None,
            stop_loss_stop=None,
            stop_loss_limit="209.50",
        )


# --- day-trade buying power ---------------------------------------------------------

BUYING_POWER = {
    "cashOnlyBuyingPower": "1000.00",
    "buyingPower": "2000.00",
    "optionsBuyingPower": "1500.00",
}


def test_buying_power_round_trips_day_trade_buying_power() -> None:
    payload = {**BUYING_POWER, "dayTradeBuyingPower": "8000.00"}

    buying_power = BuyingPower.from_dict(payload)

    assert buying_power.day_trade_buying_power == "8000.00"
    assert buying_power.to_dict() == payload


def test_buying_power_tolerates_missing_day_trade_buying_power() -> None:
    # The spec marks dayTradeBuyingPower required, but the CLI treats it as optional so
    # responses from servers that have not rolled it out yet still parse.
    buying_power = BuyingPower.from_dict(BUYING_POWER)

    assert buying_power.day_trade_buying_power is UNSET
    assert buying_power.to_dict() == BUYING_POWER


def test_portfolio_parses_without_day_trade_buying_power() -> None:
    portfolio = PortfolioAccountV2.from_dict(
        {
            "accountId": "acct-1",
            "accountType": "BROKERAGE",
            "buyingPower": BUYING_POWER,
            "equity": [],
            "positions": [],
            "orders": [],
        }
    )

    assert portfolio.buying_power.buying_power == "2000.00"
    assert portfolio.buying_power.day_trade_buying_power is UNSET


def test_portfolio_show_prints_day_trade_buying_power(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    response = {
        "accountId": "acct-1",
        "buyingPower": {**BUYING_POWER, "dayTradeBuyingPower": "8000.00"},
    }
    calls = _capture_calls(monkeypatch, response)

    result = CliRunner().invoke(app, ["portfolio", "show", "--account-id", "acct-1"])

    assert result.exit_code == 0, result.stderr
    assert calls[0][:2] == ("GET", "/userapigateway/trading/acct-1/portfolio/v2")
    assert json.loads(result.stdout)["buyingPower"]["dayTradeBuyingPower"] == "8000.00"


# --- trade market identification code ------------------------------------------------


def test_gateway_trade_round_trips_market_identification_code() -> None:
    payload = {"tradeId": "trade-1", "price": "244.90", "marketIdentificationCode": "XNAS"}

    trade = GatewayTrade.from_dict(payload)

    assert trade.market_identification_code == "XNAS"
    assert trade.to_dict() == payload


def test_gateway_trade_omits_market_identification_code_when_absent() -> None:
    trade = GatewayTrade.from_dict({"tradeId": "trade-1"})

    assert trade.market_identification_code is UNSET
    assert "marketIdentificationCode" not in trade.to_dict()


# --- event outcome floor strike ----------------------------------------------------

OUTCOME = {
    "outcomeId": "KALSHI.KXBALANCESHEET-EO26-6.6",
    "title": "ABOVE $6.6 TRILLION",
    "rules": "Resolves YES if the balance sheet is above $6.6T.",
    "volume": "80000",
    "state": "STATE_OPEN",
    "timeline": {
        "openTime": "2026-01-01T00:00:00+00:00",
        "closeTime": "2026-12-31T23:59:00+00:00",
    },
    "settledOutcome": "SETTLED_OUTCOME_UNSPECIFIED",
    "trading": "BUY_AND_SELL",
    "contracts": [],
}


def test_event_outcome_round_trips_floor_strike() -> None:
    outcome = EventOutcome.from_dict({**OUTCOME, "floorStrike": "6.6"})

    assert outcome.floor_strike == "6.6"
    assert outcome.to_dict()["floorStrike"] == "6.6"


def test_event_outcome_omits_floor_strike_when_absent() -> None:
    outcome = EventOutcome.from_dict(OUTCOME)

    assert outcome.floor_strike is UNSET
    assert "floorStrike" not in outcome.to_dict()


def _event_details(*outcomes: dict) -> dict:
    return {
        "eventSymbol": "KALSHI.KXBALANCESHEET-EO26",
        "title": "Size of Fed balance sheet at end of 2026",
        "outcomeCount": len(outcomes),
        "outcomes": list(outcomes),
    }


def _render_event_details(monkeypatch: pytest.MonkeyPatch, data: dict) -> str:
    buffer = io.StringIO()
    monkeypatch.setattr(output, "console", Console(file=buffer, width=250, no_color=True))
    output.print_event_details(data)
    return buffer.getvalue()


def test_event_details_shows_floor_strike_column_when_present(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered = _render_event_details(
        monkeypatch,
        _event_details({**OUTCOME, "floorStrike": "6.6"}, {**OUTCOME, "title": "NO STRIKE"}),
    )

    assert "Floor Strike" in rendered
    assert "6.6" in rendered.split("ABOVE $6.6 TRILLION", 1)[1]
    assert "NO STRIKE" in rendered


def test_event_details_hides_floor_strike_column_when_absent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rendered = _render_event_details(monkeypatch, _event_details(OUTCOME))

    assert "Floor Strike" not in rendered
    assert "ABOVE $6.6 TRILLION" in rendered


# --- 400 Invalid account ID --------------------------------------------------------


@pytest.mark.parametrize("module", [get_order, search_orders], ids=["get_order", "search_orders"])
def test_order_endpoints_handle_documented_400(module: object) -> None:
    response = httpx.Response(400, json={"message": "Invalid account ID."})

    assert module._parse_response(client=None, response=response) is None  # type: ignore[attr-defined]


# --- CLI pass-through ---------------------------------------------------------------


def _capture_calls(monkeypatch: pytest.MonkeyPatch, response: object) -> list:
    calls: list = []

    def fake_call(ctx: object, method: str, path: str, **kwargs: object) -> object:
        calls.append((method, path, kwargs))
        return response

    monkeypatch.setattr(cli_module, "_call", fake_call)
    return calls


def test_limit_on_close_example_is_a_valid_order_request() -> None:
    payload = json.loads((EXAMPLES / "order.single-leg.limit-on-close.json").read_text())
    payload["orderId"] = "0d2abd8d-3625-4c83-a806-98abf35567cc"

    request = OrderRequest.from_dict(payload)

    assert request.order_type is OrderRequestOrderType.LIMIT_ON_CLOSE
    assert request.limit_price == "227.50"


@pytest.mark.parametrize("order_type", ["MARKET_ON_CLOSE", "LIMIT_ON_CLOSE"])
def test_order_place_sends_on_close_order_type(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, order_type: str
) -> None:
    request = tmp_path / "order.json"
    body = {
        "instrument": {"symbol": "AAPL", "type": "EQUITY"},
        "orderSide": "BUY",
        "orderType": order_type,
        "expiration": {"timeInForce": "DAY"},
        "quantity": "1",
    }
    request.write_text(json.dumps(body), encoding="utf-8")
    calls = _capture_calls(monkeypatch, {"orderId": "order-1"})

    result = CliRunner().invoke(
        app, ["order", "place", "--file", str(request), "--account-id", "acct-1", "--yes"]
    )

    assert result.exit_code == 0, result.stderr
    method, path, kwargs = calls[0]
    assert (method, path) == ("POST", "/userapigateway/trading/acct-1/order")
    assert kwargs["json_body"]["orderType"] == order_type


@pytest.mark.parametrize(
    ("command", "path"),
    [
        (["order", "preflight-single"], "/userapigateway/trading/acct-1/preflight/single-leg"),
        (["order", "preflight-multi"], "/userapigateway/trading/acct-1/preflight/multi-leg"),
    ],
)
def test_preflight_sends_on_close_order_type(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, command: list[str], path: str
) -> None:
    request = tmp_path / "preflight.json"
    request.write_text(json.dumps({"orderType": "LIMIT_ON_CLOSE"}), encoding="utf-8")
    calls = _capture_calls(monkeypatch, {})

    result = CliRunner().invoke(app, [*command, "--file", str(request), "--account-id", "acct-1"])

    assert result.exit_code == 0, result.stderr
    assert calls[0][1] == path
    assert calls[0][2]["json_body"]["orderType"] == "LIMIT_ON_CLOSE"
