from enum import Enum


class ComHellopublicUserapigatewayApiRestHistoryGatewayHistoryTransactionSubType(str, Enum):
    DEPOSIT = "DEPOSIT"
    DEPOSIT_RETURNED = "DEPOSIT_RETURNED"
    DIVIDEND = "DIVIDEND"
    FEE = "FEE"
    INTEREST = "INTEREST"
    MISC = "MISC"
    REWARD = "REWARD"
    TRADE = "TRADE"
    TRANSFER = "TRANSFER"
    TREASURY_BILL_TRANSFER = "TREASURY_BILL_TRANSFER"
    WITHDRAWAL = "WITHDRAWAL"
    WITHDRAWAL_RETURNED = "WITHDRAWAL_RETURNED"

    def __str__(self) -> str:
        return str(self.value)
