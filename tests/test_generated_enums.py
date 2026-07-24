from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType as AccountSettingsAccountType,
)
from publicdotcom_cli._generated.models import (
    ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioAccountV2AccountType as PortfolioAccountType,
)

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
