
import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_by_months import analytics_months_tab



st.markdown(
    """
    <style>
    /* Change entire background */
    .stApp {
        background-color: #f5f5f5;  /* Soft light grey */
    }

    /* Optional: Card-like container for inputs */
     .stDataFrame, .stTextInput, .stSelectbox, .stButton {
        background-color: #ffffff;  /* White for card effect */
        border-radius: 10px;
        padding: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* Optional: Change Tab Highlight Color */
    .css-1hynsf2 {
        color: #ff5733 !important; /* Tab Text Color */
    }
    .css-1hynsf2[data-testid="stMarkdownContainer"] {
        color: #ff5733 !important;
    }

    
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_months_tab()