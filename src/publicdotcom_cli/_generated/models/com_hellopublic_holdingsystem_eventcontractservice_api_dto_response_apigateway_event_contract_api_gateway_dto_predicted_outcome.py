from enum import Enum


class ComHellopublicHoldingsystemEventcontractserviceApiDtoResponseApigatewayEventContractApiGatewayDtoPredictedOutcome(str, Enum):
    NO = "NO"
    YES = "YES"

    def __str__(self) -> str:
        return str(self.value)
