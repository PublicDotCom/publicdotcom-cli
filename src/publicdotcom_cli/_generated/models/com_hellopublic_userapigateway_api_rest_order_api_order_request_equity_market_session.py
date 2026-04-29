from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderApiOrderRequestEquityMarketSession(str, Enum):
    CORE = "CORE"
    EXTENDED = "EXTENDED"

    def __str__(self) -> str:
        return str(self.value)
