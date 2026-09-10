from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderApiOrderRequestOrderClass(str, Enum):
    BRACKET = "BRACKET"
    OCO = "OCO"
    OTO = "OTO"
    SIMPLE = "SIMPLE"

    def __str__(self) -> str:
        return str(self.value)
