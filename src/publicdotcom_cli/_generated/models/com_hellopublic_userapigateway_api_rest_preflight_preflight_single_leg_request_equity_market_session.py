from enum import Enum


class ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestEquityMarketSession(
    str, Enum
):
    CORE = "CORE"
    EXTENDED = "EXTENDED"

    def __str__(self) -> str:
        return str(self.value)
