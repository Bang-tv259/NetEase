from __future__ import annotations

from pydantic import BaseModel


class SalaryOutput(BaseModel):
    gross_salary: float
    net_salary: float
    insurance_amount: float
    personal_income_tax: float
