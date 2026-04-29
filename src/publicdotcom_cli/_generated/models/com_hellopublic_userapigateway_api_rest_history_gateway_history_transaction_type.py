from enum import Enum


class ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionType(str, Enum):
    MONEY_MOVEMENT = "MONEY_MOVEMENT"
    POSITION_ADJUSTMENT = "POSITION_ADJUSTMENT"
    TRADE = "TRADE"

    def __str__(self) -> str:
        return str(self.value)
