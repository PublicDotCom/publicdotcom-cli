from enum import Enum


class ComHellopublicUserapigatewayApiRestPreflightPreflightLegResponseOpenCloseIndicator(str, Enum):
    CLOSE = "CLOSE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
