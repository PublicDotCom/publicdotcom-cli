from enum import Enum


class ComMatadorappSharedCustomerordergatewayDtoOrderLegType0OpenCloseIndicator(str, Enum):
    CLOSE = "CLOSE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
