import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecat Days", min_value= 1, max_value= 5,
                help= "Select the number of forecasted days")
option = st.selectbox("Select data to view", "Temperature", "sky")
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    date = []
    temp = []
    temp = [days * i for i in temp]
    return date, temp 

d, t = get_data(days)

figure = px.line(x = d, y = t, labels = {"x": "Date", "y": "Temperature (c)"})
st.plotly_chart(figure)