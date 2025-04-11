from __future__ import annotations

from typing import TYPE_CHECKING

from cat.core.net_ease.constants import ConstantsSalary


if TYPE_CHECKING:
    from cat.core.net_ease.constants import TaxConfig


def calculate_personal_deduction(number_of_dependents: float) -> float:
    return ConstantsSalary.BASIC_DEDUCTION + (
        ConstantsSalary.DEPENDENT_DEDUCTION * number_of_dependents
    )


def calculate_insurance(gross_salary: float, region: int) -> float:
    # BHXH
    if gross_salary * ConstantsSalary.BHXH_RATE > ConstantsSalary.LIMIT_BH * ConstantsSalary.BHXH_RATE:
        bhxh_amount = ConstantsSalary.LIMIT_BH * ConstantsSalary.BHXH_RATE
    else:
        bhxh_amount = gross_salary * ConstantsSalary.BHXH_RATE

    # BHYT
    if gross_salary * ConstantsSalary.BHYT_RATE > ConstantsSalary.LIMIT_BH * ConstantsSalary.BHYT_RATE:
        bhyt_amount = ConstantsSalary.LIMIT_BH * ConstantsSalary.BHYT_RATE
    else:
        bhyt_amount = gross_salary * ConstantsSalary.BHYT_RATE

    # BHTN
    if region == 1:
        if gross_salary * ConstantsSalary.BHTN_RATE > ConstantsSalary.LIMIT_BHTN_V1 * ConstantsSalary.BHTN_RATE:
            bhtn_amount = ConstantsSalary.LIMIT_BHTN_V1 * ConstantsSalary.BHTN_RATE
        else:
            bhtn_amount = gross_salary * ConstantsSalary.BHTN_RATE
    elif region == 2:
        if gross_salary * ConstantsSalary.BHTN_RATE > ConstantsSalary.LIMIT_BHTN_V2 * ConstantsSalary.BHTN_RATE:
            bhtn_amount = ConstantsSalary.LIMIT_BHTN_V2 * ConstantsSalary.BHTN_RATE
        else:
            bhtn_amount = gross_salary * ConstantsSalary.BHTN_RATE
    elif region == 3:
        if gross_salary * ConstantsSalary.BHTN_RATE > ConstantsSalary.LIMIT_BHTN_V3 * ConstantsSalary.BHTN_RATE:
            bhtn_amount = ConstantsSalary.LIMIT_BHTN_V3 * ConstantsSalary.BHTN_RATE
        else:
            bhtn_amount = gross_salary * ConstantsSalary.BHTN_RATE
    elif region == 4:
        if gross_salary * ConstantsSalary.BHTN_RATE > ConstantsSalary.LIMIT_BHTN_V4 * ConstantsSalary.BHTN_RATE:
            bhtn_amount = ConstantsSalary.LIMIT_BHTN_V4 * ConstantsSalary.BHTN_RATE
        else:
            bhtn_amount = gross_salary * ConstantsSalary.BHTN_RATE

    return bhtn_amount + bhyt_amount + bhxh_amount


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
