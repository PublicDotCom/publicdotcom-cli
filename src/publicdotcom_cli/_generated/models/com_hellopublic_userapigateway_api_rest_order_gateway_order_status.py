from enum import Enum


class ComHellopublicUserapigatewayApiRestOrderGatewayOrderStatus(str, Enum):
    CANCELLED = "CANCELLED"
    EXPIRED = "EXPIRED"
    FILLED = "FILLED"
    NEW = "NEW"
    PARTIALLY_FILLED = "PARTIALLY_FILLED"
    PENDING_CANCEL = "PENDING_CANCEL"
    PENDING_REPLACE = "PENDING_REPLACE"
    QUEUED_CANCELLED = "QUEUED_CANCELLED"
    REJECTED = "REJECTED"
    REPLACED = "REPLACED"

    def __str__(self) -> str:
        return str(self.value)
