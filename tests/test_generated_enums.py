from publicdotcom_cli._generated.models import (
    ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusType as OutOfDateStatusType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType as AccountSettingsAccountType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2AccountType as PortfolioAccountType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiOrderRequestOrderClass as OrderClass,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestOpenCloseIndicator as QueryOrdersOpenCloseIndicator,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSecurityType as QueryOrdersSecurityType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestSide as QueryOrdersSide,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderApiQueryOrdersRequestStatus as QueryOrdersStatus,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2Status as OrderV2Status,
)
from publicdotcom_cli._generated.models import SearchBondsRatingItem

EXPECTED_ACCOUNT_TYPES = {
    "BOND_ACCOUNT",
    "BROKERAGE",
    "ENTITY",
    "HIGH_YIELD",
    "JOINT",
    "RIA_ASSET",
    "ROTH_IRA",
    "TRADITIONAL_IRA",
    "TREASURY",
}


def test_portfolio_account_type_parses_entity() -> None:
    assert PortfolioAccountType("ENTITY") is PortfolioAccountType.ENTITY


def test_account_settings_account_type_parses_entity() -> None:
    assert AccountSettingsAccountType("ENTITY") is AccountSettingsAccountType.ENTITY


def test_account_type_enums_match_spec() -> None:
    assert {member.value for member in PortfolioAccountType} == EXPECTED_ACCOUNT_TYPES
    assert {member.value for member in AccountSettingsAccountType} == EXPECTED_ACCOUNT_TYPES


EXPECTED_OUT_OF_DATE_STATUS_TYPES = {
    "AGGREGATE",
    "CORPORATE_ACTION_UNDERWAY",
    "LOT_ASSIGNED",
    "NOT_REPORTED_YET",
    "ORDER_OR_TRADE_ON_SYMBOL_TODAY",
    "PRE_EXISTING_OPEN_ORDER_ON_SYMBOL",
}


def test_out_of_date_status_type_parses_aggregate() -> None:
    assert OutOfDateStatusType("AGGREGATE") is OutOfDateStatusType.AGGREGATE


def test_out_of_date_status_type_matches_spec() -> None:
    assert {member.value for member in OutOfDateStatusType} == EXPECTED_OUT_OF_DATE_STATUS_TYPES


def test_search_bonds_rating_item_parses_symbol_ratings() -> None:
    assert SearchBondsRatingItem("AAA") is SearchBondsRatingItem.AAA
    assert SearchBondsRatingItem("AA+") is SearchBondsRatingItem.AA_PLUS
    assert SearchBondsRatingItem("AA") is SearchBondsRatingItem.AA
    assert SearchBondsRatingItem("AA-") is SearchBondsRatingItem.AA_MINUS
    assert SearchBondsRatingItem("SP-1+") is SearchBondsRatingItem.SP_1_PLUS
    assert SearchBondsRatingItem("SP-1") is SearchBondsRatingItem.SP_1


def test_search_bonds_rating_item_covers_all_spec_values() -> None:
    assert len(SearchBondsRatingItem) == 29


EXPECTED_ORDER_CLASSES = {"SIMPLE", "BRACKET", "OCO", "OTO"}


def test_order_class_parses_bracket_values() -> None:
    assert OrderClass("SIMPLE") is OrderClass.SIMPLE
    assert OrderClass("BRACKET") is OrderClass.BRACKET
    assert OrderClass("OCO") is OrderClass.OCO
    assert OrderClass("OTO") is OrderClass.OTO


def test_order_class_matches_spec() -> None:
    assert {member.value for member in OrderClass} == EXPECTED_ORDER_CLASSES


def test_account_type_enums_parse_joint() -> None:
    assert PortfolioAccountType("JOINT") is PortfolioAccountType.JOINT
    assert AccountSettingsAccountType("JOINT") is AccountSettingsAccountType.JOINT


EXPECTED_ORDER_STATUSES = {
    "NEW",
    "PARTIALLY_FILLED",
    "CANCELLED",
    "QUEUED_CANCELLED",
    "FILLED",
    "REJECTED",
    "PENDING_REPLACE",
    "PENDING_CANCEL",
    "EXPIRED",
    "REPLACED",
}

EXPECTED_QUERY_SECURITY_TYPES = {
    "EQUITY",
    "OPTION",
    "MULTI_LEG_INSTRUMENT",
    "CRYPTO",
    "ALT",
    "TREASURY",
    "BOND",
    "INDEX",
}


def test_order_v2_status_matches_spec() -> None:
    assert {member.value for member in OrderV2Status} == EXPECTED_ORDER_STATUSES


def test_query_orders_enums_match_spec() -> None:
    assert {member.value for member in QueryOrdersStatus} == EXPECTED_ORDER_STATUSES
    assert {member.value for member in QueryOrdersSecurityType} == EXPECTED_QUERY_SECURITY_TYPES
    assert {member.value for member in QueryOrdersSide} == {"BUY", "SELL"}
    assert {member.value for member in QueryOrdersOpenCloseIndicator} == {"OPEN", "CLOSE"}
