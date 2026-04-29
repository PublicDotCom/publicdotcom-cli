from enum import Enum


class ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestOpenCloseIndicator(
    str, Enum
):
    CLOSE = "CLOSE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
