from enum import Enum


class ComMatadorappSharedCustomerordergatewayDtoStrategyQuoteDtoDebitCredit(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    UNDECIDED = "UNDECIDED"

    def __str__(self) -> str:
        return str(self.value)
