from enum import Enum


class ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSecurityType(str, Enum):
    ALT = "ALT"
    BOND = "BOND"
    CRYPTO = "CRYPTO"
    EQUITY = "EQUITY"
    OPTION = "OPTION"
    TREASURY = "TREASURY"

    def __str__(self) -> str:
        return str(self.value)
