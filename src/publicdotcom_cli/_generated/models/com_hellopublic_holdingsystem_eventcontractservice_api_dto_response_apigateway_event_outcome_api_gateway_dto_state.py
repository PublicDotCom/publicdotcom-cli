from enum import Enum


class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoState(str, Enum):
    STATE_CLOSED = "STATE_CLOSED"
    STATE_HALTED = "STATE_HALTED"
    STATE_NEW = "STATE_NEW"
    STATE_OPEN = "STATE_OPEN"
    STATE_SETTLED = "STATE_SETTLED"
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
