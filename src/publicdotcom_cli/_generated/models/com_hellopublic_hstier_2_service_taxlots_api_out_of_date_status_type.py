from enum import Enum


class ComHellopublicHstier2ServiceTaxlotsApiOutOfDateStatusType(str, Enum):
    CORPORATE_ACTION_UNDERWAY = "CORPORATE_ACTION_UNDERWAY"
    LOT_ASSIGNED = "LOT_ASSIGNED"
    NOT_REPORTED_YET = "NOT_REPORTED_YET"
    ORDER_OR_TRADE_ON_SYMBOL_TODAY = "ORDER_OR_TRADE_ON_SYMBOL_TODAY"
    PRE_EXISTING_OPEN_ORDER_ON_SYMBOL = "PRE_EXISTING_OPEN_ORDER_ON_SYMBOL"

    def __str__(self) -> str:
        return str(self.value)
