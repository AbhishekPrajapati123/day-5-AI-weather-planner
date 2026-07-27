 # The main Streamlit application
#AI weather planner.
import streamlit as st
import requests
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
st.set_page_config(page_title="AI Weather Planner", page_icon="🌤️", layout="centered")
st.title("🌤️ Day 5: AI Weather-Aware Planner")
st.write("This app integrates a **Real-Time Weather API** (Tool) with an LLM to generate smart recommendations.")

# --- TOOL INTEGRATION FUNCTIONS (Directly answers Day 5 Objective) ---

def get_coordinates(city_name):
    """Tool 1: Converts a city name into Latitude and Longitude using Open-Meteo Geocoding API."""
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    response = requests.get(geocode_url).json()
    if "results" in response and len(response["results"]) > 0:
        # We add [0] to access the first city returned in the list
        data = response["results"][0] 
        return data["latitude"], data["longitude"], data.get("country", "Unknown")
    return None, None, None

def get_weather(lat, lon):
    """Tool 2: Fetches current weather metrics for specific coordinates."""
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(weather_url).json()
    if "current_weather" in response:
        return response["current_weather"]
    return None

# --- STREAMLIT UI ---

city = st.text_input("Enter City Name:", placeholder="e.g., Bhilai, Mumbai, London")

if st.button("Get Weather & AI Plan 🚀"):
    if not api_key:
        st.error("Please configure your GROQ_API_KEY in your environment or .env file.")
    elif not city:
        st.warning("Please enter a city name first!")
    else:
        with st.spinner("Fetching live weather data..."):
            # 1. Execute Tool 1: Geocoding
            lat, lon, country = get_coordinates(city)
            
            if lat is None:
                st.error("City not found. Please try another name.")
            else:
                # 2. Execute Tool 2: Weather retrieval
                weather_data = get_weather(lat, lon)
                
                if weather_data is None:
                    st.error("Could not fetch weather data.")
                else:
                    temp = weather_data["temperature"]
                    windspeed = weather_data["windspeed"]
                    weather_code = weather_data["weathercode"]
                    
                    # Display the raw tool data to the user
                    st.success(f"Successfully retrieved live data for **{city.title()}, {country}**!")
                    
                    col1, col2 = st.columns(2)
                    col1.metric(label="Current Temperature", value=f"{temp}°C")
                    col2.metric(label="Wind Speed", value=f"{windspeed} km/h")
                    
                    # 3. Feed the real-time tool data into the LLM
                    with st.spinner("Analyzing data with AI..."):
                        try:
                            client = Groq(api_key=api_key)
                            
                            prompt = f"""
                            You are a helpful travel assistant. A user wants to know what to wear and do in {city}, {country} today.
                            The real-time weather API (our integrated tool) has returned the following live data:
                            - **Temperature**: {temp}°C
                            - **Wind Speed**: {windspeed} km/h
                            - **Weather Code**: {weather_code} (0=Clear, 1-3=Partly Cloudy, 51-67=Rain/Drizzle, 71-86=Snow, 95-99=Thunderstorm)
                            
                            Based on this EXACT data:
                            1. Advise the user on what type of clothing is appropriate (e.g., layers, jackets, umbrellas).
                            2. Suggest 2 indoor or outdoor activities that fit this specific current weather.
                            3. Keep your advice brief, engaging, and highly practical.
                            """
                            
                            response = client.chat.completions.create(
                                model="llama-3.1-8b-instant",
                                messages=[
                                    {"role": "system", "content": "You are an AI travel consultant utilizing live API tools."},
                                    {"role": "user", "content": prompt}
                                ],
                                temperature=0.6,
                                max_tokens=500
                            )
                            
                            ai_advice = response.choices[0].message.content
                            st.subheader("🤖 Live AI Recommendation")
                            st.write(ai_advice)
                            
                        except Exception as e:
                            st.error(f"LLM generation failed: {e}")