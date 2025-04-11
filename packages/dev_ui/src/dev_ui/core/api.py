from __future__ import annotations

from typing import Any

import requests
from dev_ui.core.utils import format_region

def call_handle_convert_gross_to_net_api(
    gross_salary: float,
    number_of_dependents: int,
    wage_zone: str,
    api_base_url: str,
) -> dict[str, Any]:
    """Call the API to convert gross salary to net salary.

    Args:
        gross_salary (float): The gross salary amount.
        number_of_dependents (int): The number of dependents.
        wage_zone (str): The wage zone (1, 2, 3, or 4).
        api_base_url (str): The base URL of the API.

    Returns:
        dict[str, Any]: The response from the API.

    Raises:
        HTTPError: If the API request fails.
        RequestException: If there is a network error.
        Exception: For any other exceptions.
    """
    endpoint = f"{api_base_url}/api/net_salary/calculate/"
    params = {
        "gross_salary": gross_salary,
        "number_of_dependents": number_of_dependents,
        "region": format_region(wage_zone),
    }

    try:
        response = requests.get(endpoint, params=params, timeout=20)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"[HTTP ERROR] {http_err} - Status Code: {response.status_code}")
        raise
    except requests.exceptions.RequestException as req_err:
        print(f"[REQUEST ERROR] {req_err}")
        raise
    except Exception as err:
        print(f"[UNEXPECTED ERROR] {err}")
        raise


def call_handle_upload_excel_to_api(
    uploaded_file,
    api_base_url: str,
):
    endpoint = f"{api_base_url}/api/net_salary/upload/"
    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    }
    try:
        response = requests.post(endpoint, files=files, timeout=20)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as http_err:
        print(f"[HTTP ERROR] {http_err} - Status Code: {response.status_code}")
        raise
    except requests.exceptions.RequestException as req_err:
        print(f"[REQUEST ERROR] {req_err}")
        raise
    except Exception as err:
        print(f"[UNEXPECTED ERROR] {err}")
        raise
