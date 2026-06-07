# 🌤️ Weather Forecast App

A simple and interactive weather forecast web application built with **Streamlit** and **OpenWeatherMap API**.  
It displays temperature trends and sky conditions for any city over the next 1 to 5 days.

---

## 🚀 Features

- Enter any city name to get weather forecast
- Select number of forecast days (1 to 5)
- Choose between **Temperature** and **Sky** condition views
- Interactive line chart for temperature using Plotly
- Visual display of sky conditions with relevant icons

---

## 📁 Project Structure

```
weather-forecast-app/
├── main.py                 # Streamlit frontend
├── backend.py              # API call logic
├── images/                 # Weather condition icons
│   ├── clear.png
│   ├── rain.png
│   ├── clouds.png
│   └── snow.png
└── README.md
```

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install streamlit plotly requests
```

---

## 🔑 API Setup

This application uses the **[OpenWeatherMap 5 Day / 3 Hour Forecast API](https://openweathermap.org/forecast5)**.  
You need a free API key to use the service.

1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Create a free account
3. Navigate to your dashboard and copy your unique API key
4. Replace the `API_key` variable in `backend.py` with your key

```python
API_key = "your_api_key_here"
```

---

## ▶️ Usage

1. Run the Streamlit app:

```bash
streamlit run main.py
```

2. Enter a city name (e.g., `Tehran`, `London`, `Tokyo`)
3. Select the number of forecast days
4. Choose **Temperature** or **Sky** to view the data

---

## 📡 API Reference

This app uses the OpenWeatherMap Forecast API.

| Parameter | Description |
|-----------|-------------|
| `place` | City name (e.g., Tehran) |
| `forecast_days` | Number of days (1–5) |
| `API_key` | Your OpenWeatherMap API key |

**API Endpoint:**
```
http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}
```

---

## 📌 Notes

- Temperature is displayed in **Celsius** (converted from Kelvin)
- Sky conditions are mapped to local icons stored in the `images/` folder
- Invalid city names will trigger a user-friendly error message
- The API request is limited to 5 days (40 timestamps: 8 readings per day × 5 days)

