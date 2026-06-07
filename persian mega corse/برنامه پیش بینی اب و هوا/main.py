import streamlit as st
import plotly.express as px
from backend import get_data


# عنوان، ورودی متنی، لغزنده، جعبه انتخابی و زیرعنوان 
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecat Days", min_value= 1, max_value= 5,
                help= "Select the number of forecasted days")
option = st.selectbox("Select data to view", ["Temperature", "Sky"])
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # داده‌های دما/آسمان را دریافت کن
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":

            temperature = [item["main"]["temp"] / 10 for item in filtered_data]
            dates = [item["dt_txt"] for item in filtered_data]
            #یک نمودار دما ایجاد کردن
            figure = px.line(x = dates, y = temperature, labels = {"x": "Date", "y": "Temperature (c)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":r"D:\porgram\code\mega corse\weather forecast data app\images\clear.png",
                    "Rain":r"D:\porgram\code\mega corse\weather forecast data app\images\rain.png",
                    "Clouds":r"D:\porgram\code\mega corse\weather forecast data app\images\cloud.png",
                    "Snow":r"D:\porgram\code\mega corse\weather forecast data app\images\snow.png"}
            sky_conditions = [item["weather"][0]["main"] for item in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths,width= 115)
    except KeyError:
        st.write("That place doesn't exist")