from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderOrderExpirationTimeInForce(str, Enum):
    DAY = "DAY"
    GTD = "GTD"

    def __str__(self) -> str:
        return str(self.value)
