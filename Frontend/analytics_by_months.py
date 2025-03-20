import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"

def analytics_months_tab():
    # Fetch API data
    response = requests.post(f"{API_URL}/monthly_summary/")
    monthly_summary = response.json()

    # Debugging: Show raw API response
    # st.write("API Response:", monthly_summary)

    # Convert API response to DataFrame
    df = pd.DataFrame(monthly_summary)

    # Debugging: Check DataFrame columns
    # st.write("Columns in DataFrame:", df.columns.tolist())

    # Check if expected columns are present
    # expected_columns = ['expense_month', 'month_name', 'total']
    # if not all(col in df.columns for col in expected_columns):
    #     st.error(f"Expected columns {expected_columns} not found. Found columns: {df.columns.tolist()}")
    #     return  # Exit if columns are missing

    # Rename columns for readability
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)

    # Sort by 'Month Number' descending
    df_sorted = df.sort_values(by="Month Number", ascending=False)
    df_sorted.set_index("Month Number", inplace=True)

    # Title
    st.title("Expense Breakdown By Months")

    # Bar chart visualization
    st.bar_chart(data=df_sorted.set_index("Month Name")['Total'], use_container_width=True)

    # Format Total as currency/decimal
    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    # Display final table
    st.table(df_sorted.sort_index())  # Sorted ascending for readability
