from enum import Enum


class ComHellopublicHstier2ServiceTaxlotsApiOptionSpecificTaxLotDetailsOptionType(str, Enum):
    CALL = "CALL"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
