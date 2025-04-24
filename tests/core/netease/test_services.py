import pytest

from cat.core.net_ease.constants import ConstantsSalary, TaxConfig
from cat.core.net_ease.services import (
    calculate_insurance,
    calculate_personal_deduction,
    calculate_tax,
)


def test_calculate_personal_deduction() -> None:
    assert calculate_personal_deduction(0) == ConstantsSalary.BASIC_DEDUCTION
    assert (
        calculate_personal_deduction(2)
        == ConstantsSalary.BASIC_DEDUCTION + 2 * ConstantsSalary.DEPENDENT_DEDUCTION
    )


@pytest.mark.parametrize(
    "gross_salary, region, expected",
    [
        (
            20_000_000,
            1,
            pytest.approx(
                min(20_000_000, ConstantsSalary.LIMIT_BH) * ConstantsSalary.BHXH_RATE
                + min(20_000_000, ConstantsSalary.LIMIT_BH) * ConstantsSalary.BHYT_RATE
                + min(20_000_000, ConstantsSalary.LIMIT_BHTN_V1)
                * ConstantsSalary.BHTN_RATE
            ),
        ),
        (
            100_000_000,
            2,
            pytest.approx(
                ConstantsSalary.LIMIT_BH * ConstantsSalary.BHXH_RATE
                + ConstantsSalary.LIMIT_BH * ConstantsSalary.BHYT_RATE
                + ConstantsSalary.LIMIT_BHTN_V2 * ConstantsSalary.BHTN_RATE
            ),
        ),
    ],
)
def test_calculate_insurance(gross_salary, region, expected):
    assert calculate_insurance(gross_salary, region) == expected


def test_calculate_tax():
    tax_config = TaxConfig()

    # Case: 4,000,000 income → 5% bracket only
    assert calculate_tax(4_000_000, tax_config) == 4_000_000 * 0.05

    # Case: 10,000,000 income → spans 5% + 10%
    expected_tax = 5_000_000 * 0.05 + (10_000_000 - 5_000_000) * 0.10
    assert calculate_tax(10_000_000, tax_config) == expected_tax

    # Case: 50,000,000 income → spans multiple brackets
    expected_tax = (
        5_000_000 * 0.05
        + 5_000_000 * 0.10
        + 8_000_000 * 0.15
        + 14_000_000 * 0.20
        + (50_000_000 - 32_000_000) * 0.25
    )
    assert calculate_tax(50_000_000, tax_config) == expected_tax
