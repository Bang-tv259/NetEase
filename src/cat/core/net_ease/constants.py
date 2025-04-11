from __future__ import annotations

from pydantic import BaseModel

from cat.core.net_ease.entities import TaxBracket


class ConstantsSalary:
    LIMIT_BH = 46_800_000
    BHXH_RATE = 0.08
    BHYT_RATE = 0.015

    LIMIT_BHTN_V1 = 99_200_000
    LIMIT_BHTN_V2 = 88_200_000
    LIMIT_BHTN_V3 = 77_200_000
    LIMIT_BHTN_V4 = 69_000_000
    BHTN_RATE = 0.01

    BASIC_DEDUCTION = 11_000_000
    DEPENDENT_DEDUCTION = 4_400_000


class TaxConfig(BaseModel):
    BRACKETS: list[TaxBracket] = [
        TaxBracket(limit=5_000_000, rate=0.05),
        TaxBracket(limit=10_000_000, rate=0.10),
        TaxBracket(limit=18_000_000, rate=0.15),
        TaxBracket(limit=32_000_000, rate=0.20),
        TaxBracket(limit=52_000_000, rate=0.25),
        TaxBracket(limit=80_000_000, rate=0.30),
        TaxBracket(limit=float("inf"), rate=0.35),
    ]
