from __future__ import annotations


def format_currency(value: float) -> str:
    """Format currency values with VND notation."""
    return f"{value:,.0f} VND"
