from enum import Enum


class SearchBondsBondStatusItem(str, Enum):
    CALLED = "CALLED"
    CONVERTED = "CONVERTED"
    DEFAULTED = "DEFAULTED"
    FUNGED = "FUNGED"
    LIQUIDATED = "LIQUIDATED"
    MATURED = "MATURED"
    OUTSTANDING = "OUTSTANDING"
    PRE_ISSUANCE = "PRE_ISSUANCE"
    PUT = "PUT"
    REPAID = "REPAID"
    REPURCHASED = "REPURCHASED"
    RESTRUCTURED = "RESTRUCTURED"
    TENDERED = "TENDERED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
