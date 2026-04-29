from enum import Enum


class ComHellopublicUserapigatewayApiRestAccountAccountSettingsAccountType(str, Enum):
    BOND_ACCOUNT = "BOND_ACCOUNT"
    BROKERAGE = "BROKERAGE"
    HIGH_YIELD = "HIGH_YIELD"
    RIA_ASSET = "RIA_ASSET"
    ROTH_IRA = "ROTH_IRA"
    TRADITIONAL_IRA = "TRADITIONAL_IRA"
    TREASURY = "TREASURY"

    def __str__(self) -> str:
        return str(self.value)
