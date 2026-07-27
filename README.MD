# 🌤️ AI Weather-Aware Travel & Outfit Planner

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://day-5-ai-weather-planner.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![API](https://img.shields.io/badge/API-Open--Meteo-brightgreen.svg)](https://open-meteo.com/)
[![Groq API](https://img.shields.io/badge/Groq-Llama_3.1-orange.svg)](https://groq.com/)

A real-time, context-aware AI application that retrieves live weather data and generates smart travel, activity, and outfit recommendations. Built for **Day 5: Tool Integration**, this app demonstrates how to connect a Large Language Model to the real world using external APIs.

👉 **[Launch Live Web Application](https://day-5-ai-weather-planner.streamlit.app)**

---

## ✨ Features

*   **Real-World Tool Integration:** Connects the LLM to live internet data instead of relying solely on pre-trained knowledge.
*   **Live Geocoding:** Uses the Open-Meteo Geocoding API to convert any city name globally into exact latitude and longitude coordinates.
*   **Real-Time Weather Data:** Fetches live temperature, wind speed, and weather condition codes using the free Open-Meteo API (no OAuth or API keys required).
*   **AI-Powered Recommendations:** Feeds the exact real-time weather metrics into Groq's **Llama-3.1-8b-instant** model to generate highly practical, location-aware clothing and activity advice.

## 🌐 Live Deployment

This application is deployed live on Streamlit Community Cloud and ready to use:  
🔗 **Live Link:** [https://day-5-ai-weather-planner.streamlit.app](https://day-5-ai-weather-planner.streamlit.app)

## 🛠️ Tech Stack

*   **Frontend/UI:** [Streamlit](https://streamlit.io/)
*   **External Tool/API:** [Open-Meteo](https://open-meteo.com/) (Geocoding & Weather Forecast)
*   **LLM Provider:** [Groq API](https://groq.com/)
*   **Language Model:** `llama-3.1-8b-instant`
*   **HTTP Requests:** `requests`

---

## 🚀 How to Run Locally

Follow these steps to run the Day 5 Tool Integration project on your local machine:

### 1. Set Up the Project Folder
```bash
mkdir Day5_Tool_Integration
cd Day5_Tool_Integration
