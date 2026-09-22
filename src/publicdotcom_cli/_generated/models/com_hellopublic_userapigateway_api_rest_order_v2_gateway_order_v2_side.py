from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2Side(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

    def __str__(self) -> str:
        return str(self.value)
