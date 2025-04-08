from __future__ import annotations

from pydantic import Field, BaseModel


class TaxBracket(BaseModel):
    limit: float = Field(..., description="Maximum income for this tax bracket (VND)")
    rate: float = Field(..., description="Tax rate for income within this bracket")
