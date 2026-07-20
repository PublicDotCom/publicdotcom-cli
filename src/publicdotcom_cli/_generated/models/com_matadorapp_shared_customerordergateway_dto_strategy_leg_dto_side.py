from enum import Enum


class ComMatadorappSharedCustomerordergatewayDtoStrategyLegDtoSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

    def __str__(self) -> str:
        return str(self.value)
