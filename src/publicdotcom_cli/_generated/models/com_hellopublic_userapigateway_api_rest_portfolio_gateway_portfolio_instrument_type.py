from enum import Enum


class ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioInstrumentType(str, Enum):
    ALT = "ALT"
    BOND = "BOND"
    CRYPTO = "CRYPTO"
    EQUITY = "EQUITY"
    INDEX = "INDEX"
    OPTION = "OPTION"
    TREASURY = "TREASURY"

    def __str__(self) -> str:
        return str(self.value)
