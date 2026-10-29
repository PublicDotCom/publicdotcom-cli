from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderGatewayOrderType(str, Enum):
    LIMIT = "LIMIT"
    LIMIT_ON_CLOSE = "LIMIT_ON_CLOSE"
    MARKET = "MARKET"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"

    def __str__(self) -> str:
        return str(self.value)
