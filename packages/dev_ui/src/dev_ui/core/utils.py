from __future__ import annotations


def format_currency(value: float) -> str:
    """Format currency values with VND notation."""
    return f"{value:,.0f} VND"

def format_region(region: str) -> int:
    """Convert region string to integer."""
    if region == "Zone 1":
        return 1
    elif region == "Zone 2":
        return 2
    elif region == "Zone 3":
        return 3
    elif region == "Zone 4":
        return 4
    else:
        raise ValueError("Invalid region. Must be 'Zone 1', 'Zone 2', 'Zone 3', or 'Zone 4'.")
