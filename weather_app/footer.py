import streamlit as st

def show_footer():
    st.markdown(
        """
        <style>
        .footer {
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: gray;
            margin-top: 50px;
        }
        </style>
        <div class='footer'>© 2025 Weather App | Developed by Mohsin Ali</div>
        """,
        unsafe_allow_html=True
    )
