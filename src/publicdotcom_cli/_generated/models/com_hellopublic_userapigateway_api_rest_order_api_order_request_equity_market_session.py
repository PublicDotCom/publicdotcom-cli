from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderApiOrderRequestEquityMarketSession(str, Enum):
    CORE = "CORE"
    EXTENDED = "EXTENDED"
    TWENTY_FOUR_HOURS = "TWENTY_FOUR_HOURS"

    def __str__(self) -> str:
        return str(self.value)
