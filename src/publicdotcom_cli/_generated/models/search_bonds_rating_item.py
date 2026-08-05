from enum import Enum


class SearchBondsRatingItem(str, Enum):
    A = "A"
    AA = "AA"
    AAA = "AAA"
    AA_MINUS = "AA-"
    AA_PLUS = "AA+"
    A_1 = "A-1"
    A_1_PLUS = "A-1+"
    A_2 = "A-2"
    A_3 = "A-3"
    A_MINUS = "A-"
    A_PLUS = "A+"
    B = "B"
    BB = "BB"
    BBB = "BBB"
    BBB_MINUS = "BBB-"
    BBB_PLUS = "BBB+"
    BB_MINUS = "BB-"
    BB_PLUS = "BB+"
    B_MINUS = "B-"
    B_PLUS = "B+"
    C = "C"
    CC = "CC"
    CCC = "CCC"
    CCC_MINUS = "CCC-"
    CCC_PLUS = "CCC+"
    D = "D"
    NR = "NR"
    SP_1 = "SP-1"
    SP_1_PLUS = "SP-1+"

    def __str__(self) -> str:
        return str(self.value)
