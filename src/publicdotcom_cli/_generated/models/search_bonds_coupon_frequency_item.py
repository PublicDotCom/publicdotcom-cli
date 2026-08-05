from enum import Enum


class SearchBondsCouponFrequencyItem(str, Enum):
    ANNUAL = "ANNUAL"
    AT_MATURITY = "AT_MATURITY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    SEMI_ANNUAL = "SEMI_ANNUAL"
    ZERO = "ZERO"

    def __str__(self) -> str:
        return str(self.value)
