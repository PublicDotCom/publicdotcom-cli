import io
import re

import pytest
from rich.console import Console
from typer.testing import CliRunner

from publicdotcom_cli import cli as cli_module
from publicdotcom_cli import output
from publicdotcom_cli._generated.api.event_contracts import (
    get_event_categories,
    get_event_details,
    get_event_summary,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFilters as EventSummaryFilters,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiFiltersFrequenciesItem as FilterFrequency,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDto as EventSummaryRequest,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDtoSortingMode as SortingMode,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDtoPredictedOutcome as PredictedOutcome,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoSettledOutcome as SettledOutcome,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoState as OutcomeState,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoTrading as OutcomeTrading,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventCategoryListDto as EventCategoryList,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDtoFrequenciesItem as CategoryFrequency,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventSummaryUserApiListDto as EventSummaryList,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDto as EventDetails,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDtoExchange as Exchange,
)
from publicdotcom_cli.cli import _event_summary_body, app

ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

EVENT_SYMBOL = "KALSHI.KXBALANCESHEET-EO26"
YES_SYMBOL = "KALSHI.KXBALANCESHEET-EO26-6.6.Y"
NO_SYMBOL = "KALSHI.KXBALANCESHEET-EO26-6.6.N"
FREQUENCIES = {
    "ALL",
    "ONCE",
    "FIFTEEN_MINUTES",
    "ONE_HOUR",
    "ONE_DAY",
    "ONE_WEEK",
    "ONE_MONTH",
    "ONE_YEAR",
}

CATEGORIES = {
    "categories": [
        {
            "category": "Economics",
            "subcategories": ["Fed", "Inflation"],
            "eventFrequency": {"show": True, "frequencies": ["ALL", "ONE_MONTH"]},
        }
    ]
}

SUMMARIES = {
    "content": [
        {
            "title": "Size of Fed balance sheet at end of 2026",
            "eventSymbol": EVENT_SYMBOL,
            "volume": "125000",
            "resolutionTime": "2026-12-31T23:59:00+00:00",
            "resolved": False,
            "halted": False,
            "category": "Economics",
            "subcategories": ["Fed"],
            "symbols": [YES_SYMBOL, NO_SYMBOL],
        }
    ],
    "nextToken": "page-2",
}

DETAILS = {
    "eventSymbol": EVENT_SYMBOL,
    "exchange": "KALSHI",
    "resolved": False,
    "halted": False,
    "title": "Size of Fed balance sheet at end of 2026",
    "category": "Economics",
    "volume": "125000",
    "subcategories": ["Fed"],
    "cftcContract": {
        "contractTermsUrl": "https://example.com/terms.pdf",
        "prohibitions": ["Fed employees"],
        "resolutionSources": [{"name": "Federal Reserve", "url": "https://example.com/h41"}],
    },
    "outcomeCount": 1,
    "outcomes": [
        {
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
            "contracts": [
                {
                    "symbol": YES_SYMBOL,
                    "predictedOutcome": "YES",
                    "bid": "0.61",
                    "ask": "0.63",
                    "last": "0.62",
                    "probability": "0.62",
                },
                {
                    "symbol": NO_SYMBOL,
                    "predictedOutcome": "NO",
                    "bid": "0.37",
                    "ask": "0.39",
                    "last": "0.38",
                    "probability": "0.38",
                },
            ],
        }
    ],
}


def _plain(text: str) -> str:
    return ANSI_RE.sub("", text)


def _capture_calls(monkeypatch: pytest.MonkeyPatch, response: object) -> list:
    """Replace the HTTP helper so commands record their request instead of sending it."""
    calls: list = []

    def fake_call(ctx: object, method: str, path: str, **kwargs: object) -> object:
        calls.append((method, path, kwargs))
        return response

    monkeypatch.setattr(cli_module, "_call", fake_call)
    return calls


def _capture_output(monkeypatch: pytest.MonkeyPatch, printer: str, data: object) -> str:
    buffer = io.StringIO()
    monkeypatch.setattr(output, "console", Console(file=buffer, width=250, no_color=True))
    getattr(output, printer)(data)
    return buffer.getvalue()


def _summary_body(**kwargs: object) -> dict:
    defaults: dict[str, object] = {
        "sort": "VOLUME",
        "category": None,
        "subcategory": None,
        "next_token": None,
        "include_resolved": None,
        "created_within_days": None,
        "event_symbols": None,
        "frequencies": None,
        "resolution_start": None,
        "resolution_end": None,
    }
    defaults.update(kwargs)
    return _event_summary_body(**defaults)


# --- commands ---------------------------------------------------------------


def test_root_help_lists_event_contracts() -> None:
    result = CliRunner().invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "event-contracts" in result.stdout


def test_event_contracts_help_lists_subcommands() -> None:
    result = CliRunner().invoke(app, ["event-contracts", "--help"])

    assert result.exit_code == 0
    for command in ("categories", "summary", "details"):
        assert command in result.stdout


def test_categories_calls_endpoint(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, CATEGORIES)

    result = CliRunner().invoke(app, ["event-contracts", "categories"])

    assert result.exit_code == 0, result.stderr
    assert calls == [("GET", "/userapigateway/eventcontract/summary/categories", {})]
    plain = _plain(result.stdout)
    assert "Event Categories" in plain
    assert "Inflation" in plain


def test_summary_defaults_to_volume_sort_without_filters(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, SUMMARIES)

    result = CliRunner().invoke(app, ["event-contracts", "summary"])

    assert result.exit_code == 0, result.stderr
    assert calls == [
        (
            "POST",
            "/userapigateway/eventcontract/summary",
            {"json_body": {"sortingMode": "VOLUME"}},
        )
    ]


def test_summary_posts_all_flags(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, SUMMARIES)

    result = CliRunner().invoke(
        app,
        [
            "event-contracts",
            "summary",
            "--sort",
            "expiration",
            "--category",
            "Economics",
            "--subcategory",
            "Fed",
            "--next-token",
            "page-2",
            "--include-resolved",
            "--created-within-days",
            "7",
            "--event-symbol",
            EVENT_SYMBOL.lower(),
            "--event-symbol",
            "KALSHI.OTHER, KALSHI.THIRD",
            "--frequency",
            "one_day",
            "--frequency",
            "ONE_WEEK",
            "--resolution-start",
            "2026-10-01T00:00:00Z",
            "--resolution-end",
            "2026-12-31T23:59:59Z",
        ],
    )

    assert result.exit_code == 0, result.stderr
    assert calls == [
        (
            "POST",
            "/userapigateway/eventcontract/summary",
            {
                "json_body": {
                    "sortingMode": "EXPIRATION",
                    "category": "Economics",
                    "subcategory": "Fed",
                    "nextToken": "page-2",
                    "displayResolvedEvents": True,
                    "createdWithinDays": 7,
                    "filters": {
                        "eventSymbols": [EVENT_SYMBOL, "KALSHI.OTHER", "KALSHI.THIRD"],
                        "frequencies": ["ONE_DAY", "ONE_WEEK"],
                        "resolutionTimeStart": "2026-10-01T00:00:00Z",
                        "resolutionTimeEnd": "2026-12-31T23:59:59Z",
                    },
                }
            },
        )
    ]


def test_summary_no_include_resolved_sends_false(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, SUMMARIES)

    result = CliRunner().invoke(app, ["event-contracts", "summary", "--no-include-resolved"])

    assert result.exit_code == 0, result.stderr
    assert calls[0][2]["json_body"]["displayResolvedEvents"] is False


def test_summary_rejects_invalid_sort(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, SUMMARIES)

    result = CliRunner().invoke(app, ["event-contracts", "summary", "--sort", "POPULAR"])

    assert result.exit_code == 1
    assert "Invalid --sort" in _plain(result.stderr)
    assert calls == []


def test_summary_rejects_invalid_frequency(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, SUMMARIES)

    result = CliRunner().invoke(app, ["event-contracts", "summary", "--frequency", "HOURLY"])

    assert result.exit_code == 1
    assert "Invalid --frequency" in _plain(result.stderr)
    assert calls == []


def test_summary_renders_events_table_and_next_token(monkeypatch: pytest.MonkeyPatch) -> None:
    _capture_calls(monkeypatch, SUMMARIES)

    result = CliRunner().invoke(app, ["event-contracts", "summary"])

    assert result.exit_code == 0, result.stderr
    plain = _plain(result.stdout)
    assert "Events" in plain
    assert "125000" in plain
    assert "--next-token page-2" in plain


def test_summary_json_flag_prints_raw_response(monkeypatch: pytest.MonkeyPatch) -> None:
    _capture_calls(monkeypatch, SUMMARIES)

    result = CliRunner().invoke(app, ["--json", "event-contracts", "summary"])

    assert result.exit_code == 0, result.stderr
    plain = _plain(result.stdout)
    assert '"nextToken"' in plain
    assert "More results" not in plain


def test_details_calls_endpoint_with_all_outcomes(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, DETAILS)

    result = CliRunner().invoke(app, ["event-contracts", "details", EVENT_SYMBOL.lower()])

    assert result.exit_code == 0, result.stderr
    assert calls == [
        (
            "GET",
            f"/userapigateway/eventcontract/details/{EVENT_SYMBOL}",
            {"params": {"includeAllOutcomes": True}},
        )
    ]


def test_details_no_all_outcomes_sends_false(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _capture_calls(monkeypatch, DETAILS)

    result = CliRunner().invoke(
        app, ["event-contracts", "details", EVENT_SYMBOL, "--no-all-outcomes"]
    )

    assert result.exit_code == 0, result.stderr
    assert calls[0][2] == {"params": {"includeAllOutcomes": False}}


def test_details_renders_outcomes_table(monkeypatch: pytest.MonkeyPatch) -> None:
    _capture_calls(monkeypatch, DETAILS)

    result = CliRunner().invoke(app, ["event-contracts", "details", EVENT_SYMBOL])

    assert result.exit_code == 0, result.stderr
    plain = _plain(result.stdout)
    assert "Outcomes" in plain
    assert "0.61" in plain
    assert "0.39" in plain


# --- request body -------------------------------------------------------------


def test_summary_body_only_requires_sorting_mode() -> None:
    assert _summary_body() == {"sortingMode": "VOLUME"}


def test_summary_body_symbol_filter_defaults_frequencies_to_all() -> None:
    body = _summary_body(event_symbols=[EVENT_SYMBOL])

    assert body["filters"] == {"eventSymbols": [EVENT_SYMBOL], "frequencies": ["ALL"]}


def test_summary_body_frequency_filter_defaults_symbols_to_empty() -> None:
    body = _summary_body(frequencies=["once"])

    assert body["filters"] == {"eventSymbols": [], "frequencies": ["ONCE"]}


def test_summary_body_resolution_window_alone_builds_filters() -> None:
    body = _summary_body(resolution_end="2026-12-31T00:00:00Z")

    assert body["filters"] == {
        "eventSymbols": [],
        "frequencies": ["ALL"],
        "resolutionTimeEnd": "2026-12-31T00:00:00Z",
    }


def test_summary_body_ignores_blank_symbols() -> None:
    assert _summary_body(event_symbols=[" , "]) == {"sortingMode": "VOLUME"}


# --- output -------------------------------------------------------------------


def test_print_event_categories_renders_rows(monkeypatch: pytest.MonkeyPatch) -> None:
    rendered = _capture_output(monkeypatch, "print_event_categories", CATEGORIES)

    for cell in ("Event Categories", "Economics", "Fed, Inflation", "ALL, ONE_MONTH"):
        assert cell in rendered


def test_print_event_summaries_shows_status(monkeypatch: pytest.MonkeyPatch) -> None:
    data = {
        "content": [
            dict(SUMMARIES["content"][0], resolved=True),
            dict(SUMMARIES["content"][0], eventSymbol="KALSHI.HALTED", halted=True),
        ]
    }

    rendered = _capture_output(monkeypatch, "print_event_summaries", data)

    assert "RESOLVED" in rendered
    assert "HALTED" in rendered
    assert "More results" not in rendered


def test_print_event_details_renders_header_and_outcomes(monkeypatch: pytest.MonkeyPatch) -> None:
    rendered = _capture_output(monkeypatch, "print_event_details", DETAILS)

    for cell in (
        EVENT_SYMBOL,
        "KALSHI",
        "Outcomes: 1 of 1",
        "https://example.com/terms.pdf",
        "ABOVE $6.6 TRILLION",
        "STATE_OPEN",
        "BUY_AND_SELL",
        "0.62",
        "2026-12-31T23:59:00+00:00",
    ):
        assert cell in rendered


@pytest.mark.parametrize(
    ("printer", "data"),
    [
        ("print_event_categories", {"categories": []}),
        ("print_event_summaries", {"content": []}),
        ("print_event_details", {"message": "unexpected"}),
    ],
)
def test_event_printers_fall_back_to_json(
    monkeypatch: pytest.MonkeyPatch, printer: str, data: dict
) -> None:
    rendered = _capture_output(monkeypatch, printer, data)

    assert rendered.lstrip().startswith("{")


# --- generated client ---------------------------------------------------------


def test_generated_summary_request_round_trips_filters() -> None:
    payload = {
        "sortingMode": "RECENTLY_ADDED",
        "category": "Economics",
        "displayResolvedEvents": False,
        "createdWithinDays": 3,
        "filters": {
            "eventSymbols": [EVENT_SYMBOL],
            "frequencies": ["ONE_DAY"],
            "resolutionTimeStart": "2026-10-01T00:00:00+00:00",
        },
    }

    request = EventSummaryRequest.from_dict(payload)

    assert request.sorting_mode is SortingMode.RECENTLY_ADDED
    assert isinstance(request.filters, EventSummaryFilters)
    assert request.filters.event_symbols == [EVENT_SYMBOL]
    assert request.to_dict() == payload


def test_generated_summary_list_uses_event_symbol() -> None:
    response = EventSummaryList.from_dict(SUMMARIES)

    assert response.content[0].event_symbol == EVENT_SYMBOL
    assert response.next_token == "page-2"
    assert response.to_dict()["content"][0]["eventSymbol"] == EVENT_SYMBOL


def test_generated_event_details_parse_outcomes_and_contracts() -> None:
    details = EventDetails.from_dict(DETAILS)

    assert details.event_symbol == EVENT_SYMBOL
    assert details.exchange is Exchange.KALSHI
    outcome = details.outcomes[0]
    assert outcome.state is OutcomeState.STATE_OPEN
    assert outcome.trading is OutcomeTrading.BUY_AND_SELL
    assert outcome.settled_outcome is SettledOutcome.SETTLED_OUTCOME_UNSPECIFIED
    assert outcome.contracts[0].predicted_outcome is PredictedOutcome.YES
    assert details.cftc_contract.resolution_sources[0].name == "Federal Reserve"


def test_generated_categories_parse() -> None:
    categories = EventCategoryList.from_dict(CATEGORIES)

    frequency = categories.categories[0].event_frequency
    assert frequency.show is True
    assert frequency.frequencies == [CategoryFrequency.ALL, CategoryFrequency.ONE_MONTH]


def test_generated_enums_match_spec() -> None:
    assert {member.value for member in SortingMode} == {"VOLUME", "EXPIRATION", "RECENTLY_ADDED"}
    assert {member.value for member in FilterFrequency} == FREQUENCIES
    assert {member.value for member in CategoryFrequency} == FREQUENCIES
    assert {member.value for member in Exchange} == {
        "EXCHANGE_UNSPECIFIED",
        "EMULATOR",
        "KALSHI",
        "PMUS",
        "CDNA",
    }
    assert {member.value for member in PredictedOutcome} == {"YES", "NO"}
    assert {member.value for member in OutcomeTrading} == {
        "BUY_AND_SELL",
        "LIQUIDATION_ONLY",
        "DISABLED",
    }
    assert {member.value for member in OutcomeState} == {
        "STATE_UNSPECIFIED",
        "STATE_NEW",
        "STATE_OPEN",
        "STATE_HALTED",
        "STATE_CLOSED",
        "STATE_SETTLED",
    }


def test_generated_enums_are_str_enums() -> None:
    # The CLI supports Python 3.10, so generated enums must not use enum.StrEnum (3.11+).
    assert issubclass(SortingMode, str)
    assert SortingMode.VOLUME == "VOLUME"
    assert str(Exchange.KALSHI) == "KALSHI"


def test_generated_endpoint_modules_target_spec_paths() -> None:
    assert get_event_summary._get_kwargs(
        body=EventSummaryRequest(sorting_mode=SortingMode.VOLUME)
    ) == {
        "method": "post",
        "url": "/userapigateway/eventcontract/summary",
        "json": {"sortingMode": "VOLUME"},
        "headers": {"Content-Type": "application/json"},
    }
    assert get_event_categories._get_kwargs()["url"] == (
        "/userapigateway/eventcontract/summary/categories"
    )
    kwargs = get_event_details._get_kwargs(EVENT_SYMBOL, include_all_outcomes=False)
    assert kwargs["url"] == f"/userapigateway/eventcontract/details/{EVENT_SYMBOL}"
    assert kwargs["params"] == {"includeAllOutcomes": False}
