from enum import Enum


class GetAllInstrumentsTypeFilterItem(str, Enum):
    ALT = "ALT"
    BOND = "BOND"
    CRYPTO = "CRYPTO"
    EQUITY = "EQUITY"
    INDEX = "INDEX"
    MULTI_LEG_INSTRUMENT = "MULTI_LEG_INSTRUMENT"
    OPTION = "OPTION"
    TREASURY = "TREASURY"

    def __str__(self) -> str:
        return str(self.value)
