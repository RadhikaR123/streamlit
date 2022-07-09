
import pandas as pd
import streamlit as st
import csv

with st.sidebar:
    st.header("weather update")
    choice = st.selectbox("select location",("Pune","Delhi","Banglore"))

if choice== "Pune":
    st.title("Pune city weather")
    st.write("current weather report")
    col1, col2, col3 = st.columns(3)

    with open("pune_weather.csv","r") as f:
        file = csv.DictReader(f)
        for row in file:
            if dict(row)["datetime"] == "2022-07-09":
                
                col1.metric("Temperature", dict(row)["temp"])
                col2.metric("Wind-speed", dict(row)["humidity"] )
                col3.metric("Humidity", dict(row)["windspeed"])






















