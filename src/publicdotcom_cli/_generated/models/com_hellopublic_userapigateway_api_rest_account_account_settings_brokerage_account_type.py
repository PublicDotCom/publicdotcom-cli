from enum import Enum


class ComHellopublicUserapigatewayApiRestAccountAccountSettingsBrokerageAccountType(str, Enum):
    CASH = "CASH"
    MARGIN = "MARGIN"

    def __str__(self) -> str:
        return str(self.value)
