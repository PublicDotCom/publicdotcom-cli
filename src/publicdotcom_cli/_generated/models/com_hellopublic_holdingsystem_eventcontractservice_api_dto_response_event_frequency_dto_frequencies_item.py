from enum import Enum


class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseEventFrequencyDtoFrequenciesItem(str, Enum):
    ALL = "ALL"
    FIFTEEN_MINUTES = "FIFTEEN_MINUTES"
    ONCE = "ONCE"
    ONE_DAY = "ONE_DAY"
    ONE_HOUR = "ONE_HOUR"
    ONE_MONTH = "ONE_MONTH"
    ONE_WEEK = "ONE_WEEK"
    ONE_YEAR = "ONE_YEAR"

    def __str__(self) -> str:
        return str(self.value)
