from enum import Enum


class GetBarsV2Period(str, Enum):
    ALL = "ALL"
    DAY = "DAY"
    FIVE_YEARS = "FIVE_YEARS"
    HALF_YEAR = "HALF_YEAR"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    SINCE_PURCHASE = "SINCE_PURCHASE"
    TEN_YEARS = "TEN_YEARS"
    WEEK = "WEEK"
    YEAR = "YEAR"
    YTD = "YTD"

    def __str__(self) -> str:
        return str(self.value)
