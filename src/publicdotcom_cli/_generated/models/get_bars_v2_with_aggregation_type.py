from enum import Enum


class GetBarsV2WithAggregationType(str, Enum):
    CRYPTO = "CRYPTO"
    EQUITY = "EQUITY"
    EVENTCONTRACT = "EVENTCONTRACT"
    INDEX = "INDEX"
    OPTION = "OPTION"

    def __str__(self) -> str:
        return str(self.value)
