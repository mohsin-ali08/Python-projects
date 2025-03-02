import streamlit as st
from navbar import show_navbar
from footer import show_footer
from weather import get_weather
import base64

# Function to encode image in Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def main():
    st.set_page_config(page_title="Weather App", layout="wide")

    # Show Navbar
    show_navbar()

    # Load Local Image as Background
    bg_image_path = "assets/bg_img.jpg"
    bg_image_base64 = f"data:image/jpg;base64,{get_base64_image(bg_image_path)}"

    # Hero Section with Background Image
    st.markdown(
        f"""
        <style>
        .hero {{
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-top: 20px;
            color: white;
            background: url("{bg_image_base64}");
            background-size: cover;
            padding: 80px;
            border-radius: 12px;
            box-shadow: 0px 6px 15px rgba(0,0,0,0.4);
        }}
        .search-container {{
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }}
        .search-bar {{
            width: 50%;
            padding: 12px;
            font-size: 18px;
            border-radius: 8px;
            border: 1px solid #ccc;
            box-shadow: inset 0px 4px 8px rgba(0,0,0,0.1);
        }}
        </style>
        <div class='hero'>🌤️ Weather App</div>
        """,
        unsafe_allow_html=True
    )

    # Search Bar
    city = st.text_input("Enter city name", "Lahore", help="Type the name of the city")

    if st.button("Get Weather"):
        weather_data = get_weather(city)
        if weather_data:
            st.subheader(f"Weather in {city}")
            st.write(f"**Temperature:** {weather_data['temp']}°C")
            st.write(f"**Condition:** {weather_data['description']}")
            st.image(weather_data['icon'], caption=weather_data['description'])
        else:
            st.error("City not found!")

    # Show Footer
    show_footer()

if __name__ == "__main__":
    main()
