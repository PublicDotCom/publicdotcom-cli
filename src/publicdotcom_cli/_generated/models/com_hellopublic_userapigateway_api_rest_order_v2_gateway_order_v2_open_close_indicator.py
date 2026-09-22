from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2OpenCloseIndicator(str, Enum):
    CLOSE = "CLOSE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
