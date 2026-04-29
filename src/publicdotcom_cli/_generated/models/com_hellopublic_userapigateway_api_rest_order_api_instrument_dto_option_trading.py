from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderApiInstrumentDtoOptionTrading(str, Enum):
    BUY_AND_SELL = "BUY_AND_SELL"
    DISABLED = "DISABLED"
    LIQUIDATION_ONLY = "LIQUIDATION_ONLY"

    def __str__(self) -> str:
        return str(self.value)
