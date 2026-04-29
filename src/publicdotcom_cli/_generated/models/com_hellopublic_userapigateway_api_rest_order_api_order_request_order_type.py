from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderApiOrderRequestOrderType(str, Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"

    def __str__(self) -> str:
        return str(self.value)
