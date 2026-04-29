from enum import Enum


class ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionDirection(str, Enum):
    INCOMING = "INCOMING"
    OUTGOING = "OUTGOING"

    def __str__(self) -> str:
        return str(self.value)
