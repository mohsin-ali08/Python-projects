import streamlit as st

def show_navbar():
    st.markdown(
        """
        <style>
        .navbar {
            background-color: #333;
            padding: 15px;
            text-align: center;
            font-size: 20px;
            color: white;
            font-weight: bold;
            border-radius: 8px;
        }
        </style>
        <div class='navbar'>🌍 Weather App - Live Weather Updates</div>
        """,
        unsafe_allow_html=True
    )
