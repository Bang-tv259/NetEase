from __future__ import annotations

import pandas as pd
import streamlit as st

from dev_ui.core.api import call_handle_convert_gross_to_net_api
from dev_ui.core.utils import format_currency
from dev_ui.common.config import AppConfig


config = AppConfig()
# Main layout
st._config.set_option("theme.base", "light")
st.markdown("### Feature > Salary Converter")
st.markdown("## Salary Converter")


with st.form("salary_form"):
    col1, col2 = st.columns(2)

    with col1:
        salary = st.text_input("Gross Salary *", placeholder="Enter money salary...")
        wage_zone = st.selectbox("Wage zones *", ["Zone 1", "Zone 2", "Zone 3", "Zone 4"])

    with col2:
        dependent = st.text_input(
            "Dependent", placeholder="Enter the number of people..."
        )
        conversion_type = st.selectbox(
            "Type of conversion *", ["Gross to Net", "Net to Gross"]
        )

    # Button Convert
    submitted = st.form_submit_button("Convert")

    if submitted:
        result = call_handle_convert_gross_to_net_api(
            salary,
            dependent,
            config.backend_url,
        )

        # Display the result
        st.markdown("### Convert Result")
        st.markdown("*(Below is a reference result for the salary conversion feature)*")

        # Result Table
        result_data = {
            "Gross Salary": [format_currency(result["gross_salary"])],
            "Insurance": [format_currency(result["insurance_amount"])],
            "Personal Income Tax": [format_currency(result["personal_income_tax"])],
            "Net Salary": [format_currency(result["net_salary"])],
        }
        st.table(pd.DataFrame(result_data))

        # Detailed explanation table
        st.markdown("### Detailed explanation of salary calculation")
        details_data = {
            "Name": [
                "Type Convert",
                "Gross Salary",
                "Insurance (10.5%)",
                "Personal Income Tax",
                "Net Salary",
            ],
            "Description": [
                "Gross to net",
                format_currency(result["gross_salary"]),
                format_currency(result["insurance_amount"]),
                format_currency(result["personal_income_tax"]),
                format_currency(result["net_salary"]),
            ],
        }
        st.table(pd.DataFrame(details_data))
