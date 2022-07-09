import streamlit as st
import pandas as pd

df1 = pd.read_csv("/home/navgurukul/Documents/streamlit/history.csv")


col1 , col2 = st.columns(2)

with col1:
    number1 = st.number_input('Insert first number', value=0)
with col2:
    number2 = st.number_input('Insert first number', value= 0)
buttn = st.button("+")
if buttn:
    new_data = {"num1": number1, "num2":number2,"op": "addition(+)"}
    df1 = df1.append(new_data, ignore_index= True)
    df1.to_csv("/home/navgurukul/Documents/streamlit/history.csv")
st.dataframe(df1)