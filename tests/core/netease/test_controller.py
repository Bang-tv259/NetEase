from io import BytesIO

import pytest
from fastapi import UploadFile
from openpyxl import Workbook
from pytest_mock import MockerFixture

from cat.core.net_ease.constants import TaxBracket, TaxConfig
from cat.core.net_ease.controller import (
    handle_convert_gross_to_net,
    handle_upload_excel,
)
from cat.core.net_ease.dto import SalaryOutput

tax_config = TaxConfig(
    BRACKETS=[
        TaxBracket(limit=5_000_000, rate=0.05),
        TaxBracket(limit=10_000_000, rate=0.10),
        TaxBracket(limit=18_000_000, rate=0.15),
        TaxBracket(limit=32_000_000, rate=0.20),
        TaxBracket(limit=52_000_000, rate=0.25),
        TaxBracket(limit=80_000_000, rate=0.30),
        TaxBracket(limit=float("inf"), rate=0.35),
    ]
)


def test_handle_convert_gross_to_net(mocker: MockerFixture):
    mock_insurance = mocker.patch("cat.core.net_ease.controller.calculate_insurance")
    mock_insurance.return_value = 10_000_000
    mock_deduction = mocker.patch(
        "cat.core.net_ease.controller.calculate_personal_deduction"
    )
    mock_deduction.return_value = 5_000_000
    mock_tax = mocker.patch("cat.core.net_ease.controller.calculate_tax")
    mock_tax.return_value = 2_000_000

    output = handle_convert_gross_to_net(
        gross_salary=20_000_000,
        number_of_dependents=2,
        region=1,
        tax_config_dep=tax_config,
    )

    assert isinstance(output, SalaryOutput)
    assert output.gross_salary == 20_000_000
    assert output.net_salary == 8_000_000
    assert output.insurance_amount == 10_000_000
    assert output.personal_income_tax == 2_000_000


@pytest.mark.asyncio
async def test_handle_upload_excel(tmp_path):
    # Tạo workbook giả
    wb = Workbook()
    ws = wb.active
    ws.append(["ID", "Employee Name", "Gross Salary", "Number of Dependents", "Region"])
    ws.append([1, "Alice", 20000000, 2, 1])
    ws.append([2, "Bob", 30000000, 1, 2])

    # Lưu vào bytes
    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    # Tạo UploadFile giả
    upload_file = UploadFile(
        filename="tests/data_test/data_test_gross_net.xlsx", file=file_stream
    )

    # Gọi hàm upload
    result_wb = await handle_upload_excel(upload_file, tax_config)

    assert isinstance(result_wb, Workbook)

    result_sheet = result_wb.active
    rows = list(result_sheet.iter_rows(values_only=True))

    # Header + 2 nhân viên
    assert len(rows) == 3
    assert rows[0] == (
        "ID",
        "Employee Name",
        "Gross Salary",
        "Number of Dependents",
        "Region",
        "Net Salary",
    )
    assert rows[1][1] == "Alice"
    assert isinstance(rows[1][-1], float)  # Net Salary
