from enum import Enum


class GetEventContractBarsPeriod(str, Enum):
    ALL = "ALL"
    DAY = "DAY"
    MONTH = "MONTH"
    WEEK = "WEEK"

    def __str__(self) -> str:
        return str(self.value)
