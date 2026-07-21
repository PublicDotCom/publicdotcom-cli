from enum import Enum


class GetBarsV2TradingSessionToggle(str, Enum):
    ALL_SESSIONS = "ALL_SESSIONS"
    REGULAR_AND_EXTENDED_HOURS = "REGULAR_AND_EXTENDED_HOURS"
    REGULAR_HOURS = "REGULAR_HOURS"

    def __str__(self) -> str:
        return str(self.value)
