from enum import Enum


class ComMatadorappSharedCustomerordergatewayDtoOrderLegSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

    def __str__(self) -> str:
        return str(self.value)
