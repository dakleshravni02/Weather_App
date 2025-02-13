
import streamlit as st
import requests

# OpenWeather API Key
API_KEY = "Enter your API KEY"  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
        return weather_info
    else:
        return None

# Streamlit UI
st.title("Real-Time Weather App")
city_name = st.text_input("Enter city name:", "")

if city_name:
    weather_data = get_weather(city_name)
    if weather_data:
        st.subheader(f"Weather Report for {weather_data['City']}")
        st.write(f"**Temperature:** {weather_data['Temperature']}")
        st.write(f"**Weather:** {weather_data['Weather']}")
        st.write(f"**Humidity:** {weather_data['Humidity']}")
        st.write(f"**Wind Speed:** {weather_data['Wind Speed']}")
    else:
        st.error("City not found or invalid API key.")


# In[ ]:




