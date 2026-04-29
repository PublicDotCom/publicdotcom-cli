from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderGatewayOrderLegOpenCloseIndicator(str, Enum):
    CLOSE = "CLOSE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
