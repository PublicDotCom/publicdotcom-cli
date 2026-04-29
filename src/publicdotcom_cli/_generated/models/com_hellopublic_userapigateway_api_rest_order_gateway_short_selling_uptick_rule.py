from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderGatewayShortSellingUptickRule(str, Enum):
    NOT_TRIGGERED = "NOT_TRIGGERED"
    TRIGGERED = "TRIGGERED"

    def __str__(self) -> str:
        return str(self.value)
