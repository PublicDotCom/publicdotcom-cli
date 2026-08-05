from enum import Enum


class SearchBondsSpCreditwatchItem(str, Enum):
    DEVELOPING = "DEVELOPING"
    NEGATIVE = "NEGATIVE"
    NOT_MEANINGFUL = "NOT_MEANINGFUL"
    POSITIVE = "POSITIVE"

    def __str__(self) -> str:
        return str(self.value)
