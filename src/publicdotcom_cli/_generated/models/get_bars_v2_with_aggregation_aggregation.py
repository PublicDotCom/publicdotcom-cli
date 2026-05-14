from enum import Enum


class GetBarsV2WithAggregationAggregation(str, Enum):
    FIFTEEN_MINUTES = "FIFTEEN_MINUTES"
    FIVE_MINUTES = "FIVE_MINUTES"
    ONE_DAY = "ONE_DAY"
    ONE_HOUR = "ONE_HOUR"
    ONE_MINUTE = "ONE_MINUTE"
    ONE_MONTH = "ONE_MONTH"
    ONE_WEEK = "ONE_WEEK"
    ONE_YEAR = "ONE_YEAR"
    SIX_MONTHS = "SIX_MONTHS"
    TEN_MINUTES = "TEN_MINUTES"
    THIRTY_MINUTES = "THIRTY_MINUTES"
    THREE_MONTHS = "THREE_MONTHS"

    def __str__(self) -> str:
        return str(self.value)
