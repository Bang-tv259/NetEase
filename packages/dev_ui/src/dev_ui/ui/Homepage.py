from __future__ import annotations

import streamlit as st


st.set_page_config(page_title="AvePoint: NetEase ", layout="wide", page_icon="🏡")
st._config.set_option("theme.base", "light")
st.header("🏡 AvePoint: NetEase ")

# Introduction section
st.subheader("Introduction")
st.write("""
Welcome to AvePoint: NetEase.\n\n
This application is designed to help you calculate net
salary from gross salary, and provides the ability to upload an Excel file to calculate
net salary for multiple employees quickly and accurately.
""")

# Gross to Net salary calculation feature
st.subheader("💬_Gross_Net - Calculate Gross to Net Salary")
st.write("""
To calculate the net salary from the gross salary, simply input the gross salary
amount into the corresponding field, and the application will automatically calculate
taxes and social security deductions to provide the accurate net salary.
""")
st.write("Steps to use this feature:")
st.write("1. Enter the Gross salary into the input field.")
st.write("2. Enter Dependent person.")
st.write("3. Click 'Convert' to get the net salary result.")

# Upload Excel file feature
st.subheader("📁_Upload_files - Upload an Excel File and Calculate Net Salary")
st.write("""
The application also supports uploading an Excel file containing salary information
for multiple employees. You can upload the file, and the application will automatically
calculate the net salary for all employees in the file.
""")
st.write("Steps to use this feature:")
st.write(
    "1. Click 'Upload File' to select your Excel file containing salary information."
)
st.write("2. Click 'Analyze' to get the net salary result.")
st.write(
    "3. The application will calculate the net salary for all employees and return the "
    "results in a table or a new Excel file."
)
