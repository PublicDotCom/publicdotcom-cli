from enum import Enum


class SearchBondsRatingCategory(str, Enum):
    INVESTMENT_GRADE = "INVESTMENT_GRADE"
    SPECULATIVE_GRADE = "SPECULATIVE_GRADE"

    def __str__(self) -> str:
        return str(self.value)
