

import pandas as pd
import streamlit as st
import csv
import matplotlib.pyplot as plt


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
    month = st.selectbox("enter month",('june','july'))
    if month == "june":
        data = pd.read_csv("pune_weather.csv", nrows=30)
        df1 = pd.DataFrame(data)
        st.dataframe(df1[["datetime", "temp", "humidity", "dew", "snow", "windspeed"]])
        # chart = data.plot(kind = 'scatter', x= 'datetime', y= 'temp')
        fig = plt.figure(figsize=(30,20))

        plt.plot(data['datetime'],data['temp'])
        plt.xlabel("Date of the month", fontdict={'fontsize': 35, 'fontweight': 'medium'})
        plt.ylabel('Temprature per day', fontdict={'fontsize': 35, 'fontweight': 'medium'})
        plt.title("temprature per day graph", fontdict={'fontsize': 40, 'fontweight': 'medium'})
        st.pyplot(fig)




















