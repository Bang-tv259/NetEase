from __future__ import annotations

from io import BytesIO

from fastapi import File, Query, APIRouter, UploadFile
from fastapi.responses import StreamingResponse

from cat.api.dependencies import TaxConfigDep
from cat.core.net_ease.dto import SalaryOutput
from cat.core.net_ease.controller import handle_upload_excel, handle_convert_gross_to_net


router = APIRouter(prefix="/api", tags=["Gross to Net"])


@router.get("/net_salary/calculate/")
async def calculate_net_salary_api(
    tax_config_dep: TaxConfigDep,
    gross_salary: float = Query(...),
    number_of_dependents: int = Query(...),
    region: int = Query(...),
) -> SalaryOutput:
    return handle_convert_gross_to_net(gross_salary, number_of_dependents, region, tax_config_dep)


@router.post("/net_salary/upload/")
async def upload_excel(
    tax_config_dep: TaxConfigDep, file: UploadFile = File(...)
) -> StreamingResponse:
    """Handle the uploaded Excel file, process it, and return.

    The result is returned as a new Excel file.
    """
    # Save the new workbook to a BytesIO object
    new_wb = await handle_upload_excel(file, tax_config_dep)
    output = BytesIO()
    new_wb.save(output)
    output.seek(0)

    # Return the new file as a response
    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=processed_salaries.xlsx"},
    )

@router.get("/healthz")
def health_check():
    return {"status": "healthy"}