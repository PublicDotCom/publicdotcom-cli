from publicdotcom_cli._generated.models import (
    ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusType as OutOfDateStatusType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType as AccountSettingsAccountType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2AccountType as PortfolioAccountType,
)
from publicdotcom_cli._generated.models import SearchBondsRatingItem

EXPECTED_ACCOUNT_TYPES = {
    "BOND_ACCOUNT",
    "BROKERAGE",
    "ENTITY",
    "HIGH_YIELD",
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
