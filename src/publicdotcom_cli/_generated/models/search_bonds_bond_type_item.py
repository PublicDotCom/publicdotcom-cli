from enum import Enum


class SearchBondsBondTypeItem(str, Enum):
    AGENCY = "AGENCY"
    CD = "CD"
    CORPORATE = "CORPORATE"
    GOVERNMENT = "GOVERNMENT"
    MUNICIPAL = "MUNICIPAL"
    TREASURY = "TREASURY"

    def __str__(self) -> str:
        return str(self.value)
