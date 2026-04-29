from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoShortingAvailability(str, Enum):
    EASY_TO_BORROW = "EASY_TO_BORROW"
    HARD_TO_BORROW = "HARD_TO_BORROW"
    NOT_SHORTABLE = "NOT_SHORTABLE"

    def __str__(self) -> str:
        return str(self.value)
