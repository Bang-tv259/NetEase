from __future__ import annotations

from typing import Annotated

from fastapi import Depends

from cat.core.net_ease.constants import TaxConfig


def get_tax_config() -> TaxConfig:
    return TaxConfig()


TaxConfigDep = Annotated[TaxConfig, Depends(get_tax_config)]
