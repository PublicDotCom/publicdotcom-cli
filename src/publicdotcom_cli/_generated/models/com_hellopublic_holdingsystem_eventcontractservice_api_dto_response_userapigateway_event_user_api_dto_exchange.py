from enum import Enum


class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseUserapigatewayEventUserApiDtoExchange(str, Enum):
    CDNA = "CDNA"
    EMULATOR = "EMULATOR"
    EXCHANGE_UNSPECIFIED = "EXCHANGE_UNSPECIFIED"
    KALSHI = "KALSHI"
    PMUS = "PMUS"

    def __str__(self) -> str:
        return str(self.value)
