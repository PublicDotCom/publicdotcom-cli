from enum import Enum


class SearchBondsTreasurySubtypeItem(str, Enum):
    BILL = "BILL"
    BOND = "BOND"
    FLOATING = "FLOATING"
    NOTE = "NOTE"
    STRIPS = "STRIPS"
    TIPS = "TIPS"

    def __str__(self) -> str:
        return str(self.value)
