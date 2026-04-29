from enum import Enum


class ComHellopublicUserapigatewayApiRestAccountAccountSettingsTradePermissions(str, Enum):
    BUY_AND_SELL = "BUY_AND_SELL"
    RESTRICTED_CLOSE_ONLY = "RESTRICTED_CLOSE_ONLY"
    RESTRICTED_NO_TRADING = "RESTRICTED_NO_TRADING"
    RESTRICTED_SETTLED_FUNDS_ONLY = "RESTRICTED_SETTLED_FUNDS_ONLY"

    def __str__(self) -> str:
        return str(self.value)
