from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderGatewayLegInstrumentType(str, Enum):
    EQUITY = "EQUITY"
    OPTION = "OPTION"

    def __str__(self) -> str:
        return str(self.value)
