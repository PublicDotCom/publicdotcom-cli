from enum import Enum


class GetBarsV2Type(str, Enum):
    CRYPTO = "CRYPTO"
    EQUITY = "EQUITY"
    EVENTCONTRACT = "EVENTCONTRACT"
    INDEX = "INDEX"
    OPTION = "OPTION"

    def __str__(self) -> str:
        return str(self.value)
