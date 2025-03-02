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

    # Custom CSS for Stylish UI
    st.markdown(
        f"""
        <style>
        .search-box {{
            padding: 12px;
            font-size: 18px;
            border-radius: 8px;
            border: none;
            width: 50%;
            box-shadow: inset 0px 4px 8px rgba(0,0,0,0.1);
        }}
        .btn {{
            margin-top: 10px;
            padding: 12px 24px;
            font-size: 18px;
            color: white;
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }}
        .btn:hover {{
            background: linear-gradient(135deg, #a777e3, #6e8efb);
        }}
        .weather-card {{
            margin-top: 20px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            text-align: center;
            box-shadow: 0px 6px 15px rgba(0,0,0,0.4);
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Weather App Interface
    st.title("🌤️ Weather App")
    city = st.text_input("Enter city name", "Lahore", key="city_input")
    if st.button("Get Weather", key="weather_btn"):
        weather_data = get_weather(city)
        if weather_data:
            st.markdown(
                f"""
                <div class='weather-card'>
                    <h2>Weather in {city}</h2>
                    <p><strong>Temperature:</strong> {weather_data['temp']}°C</p>
                    <p><strong>Condition:</strong> {weather_data['description']}</p>
                    <img src='{weather_data['icon']}' alt='weather icon'>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("City not found!")

    # Show Footer
    show_footer()

if __name__ == "__main__":
    main()
