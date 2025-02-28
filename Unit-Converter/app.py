import streamlit as st
import time
import random

# Define conversion factors
conversion_factors = {
    'length': {'meters': 1, 'centimeters': 100},
    'area': {'square meters': 1, 'square centimeters': 10000},
    'speed': {'meters per second': 1, 'kilometers per hour': 3.6}
}

def convert_units(value, from_unit, to_unit, conversion_type):
    result = value * conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit]
    formula = f"{value} {from_unit} × {conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit]} = {result:.5f} {to_unit}"
    return result, formula

# Apply responsive CSS with dark/light mode support
st.markdown("""
    <style>
        body { font-family: Arial, sans-serif; }
        .stApp {
            max-width: 700px;
            margin: auto;
            border-radius: 10px;
            padding: 20px;
            transition: all 0.3s ease-in-out;
        }
        .dark-mode {
            background: #1e1e1e;
            color: white;
        }
        .light-mode {
            background: white;
            color: black;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Theme selection
theme = st.radio("Select Theme", ["Light", "Dark"], horizontal=True)
mode_class = "dark-mode" if theme == "Dark" else "light-mode"
st.markdown(f'<div class="stApp {mode_class}">', unsafe_allow_html=True)

st.title("🌟 Smart Unit Converter 🌟")

# Select conversion type
conversion_type = st.selectbox("Choose a category", list(conversion_factors.keys()))

# Input value
value = st.number_input("Enter value", min_value=0.0, step=0.1)

# Select units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", list(conversion_factors[conversion_type].keys()))
with col2:
    to_unit = st.selectbox("To", list(conversion_factors[conversion_type].keys()))

# Convert button
if st.button("Convert", use_container_width=True):
    with st.spinner("Converting..."):
        time.sleep(random.uniform(0.5, 1.5))
    result, formula = convert_units(value, from_unit, to_unit, conversion_type)
    st.success(f"✅ {value} {from_unit} = {result:.5f} {to_unit}")
    st.info(f"Formula: {formula}")

st.markdown('</div>', unsafe_allow_html=True)