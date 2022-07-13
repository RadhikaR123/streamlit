

import pandas as pd
import streamlit as st
import csv
import matplotlib.pyplot as plt
from datetime import date, datetime




current_date = date.today()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

st.title("Welcome to my app")
st.write("Date -",current_date)
st.write("time - ", current_time)



with st.sidebar:
    st.header("weather update")
    choice = st.selectbox("select location",('select city',"Pune","Delhi","Banglore"),0)

if choice== "Pune":
    st.title("Pune city weather")
    st.write("current weather report")
    
    col1, col2, col3 = st.columns(3)


    with open("pune_weather.csv","r") as f:
        file = csv.DictReader(f)
        for row in file:
            if dict(row)["datetime"] == str(current_date):
                col1.metric("Temperature", dict(row)["temp"])
                col2.metric("Wind-speed", dict(row)["humidity"] )
                col3.metric("Humidity", dict(row)["windspeed"])
    month = st.selectbox("enter month",['select month','june','july'], 0)
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
    elif month == "july":
        data = pd.read_csv("pune_weather.csv", skiprows=range(1,31), nrows=22)
        df1 = pd.DataFrame(data)
        st.dataframe(df1[["datetime", "temp", "humidity", "dew", "snow", "windspeed"]])
        # chart = data.plot(kind = 'scatter', x= 'datetime', y= 'temp')
        fig = plt.figure(figsize=(30,20))

        plt.plot(data['datetime'],data['temp'])
        plt.xlabel("Date of the month", fontdict={'fontsize': 35, 'fontweight': 'medium'})
        plt.ylabel('Temprature per day', fontdict={'fontsize': 35, 'fontweight': 'medium'})
        plt.title("temprature per day graph", fontdict={'fontsize': 40, 'fontweight': 'medium'})
        st.pyplot(fig)


















