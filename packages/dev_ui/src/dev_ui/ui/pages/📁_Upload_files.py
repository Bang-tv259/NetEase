from __future__ import annotations

from io import BytesIO

import pandas as pd
import streamlit as st

from dev_ui.core.api import call_handle_upload_excel_to_api
from dev_ui.common.config import AppConfig


config = AppConfig()
# Main layout
st._config.set_option("theme.base", "light")
st.markdown("### Feature > Salary Converter")
st.markdown("## Salary Converter")


# Main function
st.markdown("### Upload an Excel file to calculate net salary")
uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])

if st.button("Analyze") and uploaded_file is not None:
    excel_bytes = call_handle_upload_excel_to_api(uploaded_file, config.backend_url)
    data_df = pd.read_excel(BytesIO(excel_bytes))
    st.write("### Result Preview")
    st.dataframe(data_df, use_container_width=True)
    st.download_button(
        label="📥 Download Processed Excel",
        data=excel_bytes,
        file_name="processed_salaries.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
