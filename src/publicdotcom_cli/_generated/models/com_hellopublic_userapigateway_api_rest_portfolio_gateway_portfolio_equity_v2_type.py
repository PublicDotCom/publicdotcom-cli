from enum import Enum


class ComHellopublicUserapigatewayApiRestPortfolioGatewayPortfolioEquityV2Type(str, Enum):
    BONDS = "BONDS"
    CASH = "CASH"
    CRYPTO = "CRYPTO"
    JIKO_ACCOUNT = "JIKO_ACCOUNT"
    OPTIONS_LONG = "OPTIONS_LONG"
    OPTIONS_SHORT = "OPTIONS_SHORT"
    STOCK = "STOCK"

    def __str__(self) -> str:
        return str(self.value)
