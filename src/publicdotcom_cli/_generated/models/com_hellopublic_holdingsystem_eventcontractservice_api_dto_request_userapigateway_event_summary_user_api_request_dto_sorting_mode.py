from enum import Enum


class ComHellopublicHoldingsystemEventcontractserviceApiDtoRequestUserapigatewayEventSummaryUserApiRequestDtoSortingMode(str, Enum):
    EXPIRATION = "EXPIRATION"
    RECENTLY_ADDED = "RECENTLY_ADDED"
    VOLUME = "VOLUME"

    def __str__(self) -> str:
        return str(self.value)
