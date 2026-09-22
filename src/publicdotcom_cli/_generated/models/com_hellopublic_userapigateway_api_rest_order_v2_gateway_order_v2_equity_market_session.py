from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderV2GatewayOrderV2EquityMarketSession(str, Enum):
    REGULAR = "REGULAR"
    REST_OF_DAY = "REST_OF_DAY"
    TWENTY_FOUR_HOURS = "TWENTY_FOUR_HOURS"

    def __str__(self) -> str:
        return str(self.value)
