from enum import Enum


class ComHellopublicUserapigatewayApiRestAccountAccountSettingsOptionsLevel(str, Enum):
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_3 = "LEVEL_3"
    LEVEL_4 = "LEVEL_4"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
