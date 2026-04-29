from enum import Enum


class ComHellopublicUserapigatewayApiRestMarketdataQuoteGatewayQuoteOutcome(str, Enum):
    SUCCESS = "SUCCESS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
