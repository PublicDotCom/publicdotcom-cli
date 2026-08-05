from enum import Enum


class SearchBondsSpOutlookItem(str, Enum):
    DEVELOPING = "DEVELOPING"
    NEGATIVE = "NEGATIVE"
    NOT_MEANINGFUL = "NOT_MEANINGFUL"
    NOT_RATED = "NOT_RATED"
    POSITIVE = "POSITIVE"
    STABLE = "STABLE"

    def __str__(self) -> str:
        return str(self.value)
