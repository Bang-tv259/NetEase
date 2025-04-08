from __future__ import annotations

from typing import TYPE_CHECKING

from cat.core.net_ease.constants import ConstantsSalary


if TYPE_CHECKING:
    from cat.core.net_ease.constants import TaxConfig


def calculate_personal_deduction(number_of_dependents: float) -> float:
    return ConstantsSalary.BASIC_DEDUCTION + (
        ConstantsSalary.DEPENDENT_DEDUCTION * number_of_dependents
    )


def calculate_insurance(gross_salary: float) -> float:
    return gross_salary * (
        ConstantsSalary.BHXH_RATE + ConstantsSalary.BHYT_RATE + ConstantsSalary.BHTN_RATE
    )


def calculate_tax(pre_tax_income: float, tax_config: TaxConfig) -> float:
    tax = 0
    previous_limit = 0
    for bracket in tax_config.BRACKETS:
        limit, rate = bracket.limit, bracket.rate
        if pre_tax_income > previous_limit:
            taxable_income = min(pre_tax_income, limit) - previous_limit
            tax += taxable_income * rate
            previous_limit = limit
        else:
            break

    return tax
