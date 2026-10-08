from enum import Enum


class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventOutcomeApiGatewayDtoSettledOutcome(str, Enum):
    SETTLED_OUTCOME_NO = "SETTLED_OUTCOME_NO"
    SETTLED_OUTCOME_OTHER = "SETTLED_OUTCOME_OTHER"
    SETTLED_OUTCOME_UNSPECIFIED = "SETTLED_OUTCOME_UNSPECIFIED"
    SETTLED_OUTCOME_YES = "SETTLED_OUTCOME_YES"

    def __str__(self) -> str:
        return str(self.value)
