from enum import Enum


class ComHellopublicUserapigatewayApiRestPreflightPreflightSingleLegRequestEquityMarketSession(
    str, Enum
):
    CORE = "CORE"
    EXTENDED = "EXTENDED"
    TWENTY_FOUR_HOURS = "TWENTY_FOUR_HOURS"

    def __str__(self) -> str:
        return str(self.value)
