
from textwrap import indent
import streamlit as st
import json
import pandas as pd


df1 = pd.read_csv("/home/navgurukul/Documents/streamlit/pre_hist.csv")

dic ={}
col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input('Insert first number', value = 0)
    st.session_state["first_number"]= number1
    # dic["num1"]=number1
    # st.write(st.session_state)

with col2:
    number2 = st.number_input('Insert second number', value= 0)
    st.session_state["number2"]= number2
    # dic["num2"]=number2
    # st.write(st.session_state)

button1 = st.button("+")
if button1:
    st.write("your answer is",number1+number2)
    st.session_state['operation']="addition"
    st.session_state["answer"]= number1+number2
    dic = {"num1":number1,"operation":"+", "num2":number2,"ans":number1+number2}
    df1 = df1.append(dic, ignore_index = True)
    df1.to_csv("/home/navgurukul/Documents/streamlit/pre_hist.csv", index = False)
    # st.dataframe(df1)


button2 = st.button("-")
if button2:
    st.write("your answer is",number1-number2)
    st.session_state['operation']="subtraction"
    st.session_state["answer"]= number1-number2
    dic = {"num1":number1,"operation":"-", "num2":number2,"ans":number1-number2}
    df1 = df1.append(dic, ignore_index = True)
    df1.to_csv("/home/navgurukul/Documents/streamlit/pre_hist.csv", index = False)
    # st.dataframe(df1)


button3 = st.button("*")
if button3:
    st.write("your answer is",number1*number2)
    st.session_state['operation']="Multiplication"
    st.session_state["answer"]= number1*number2
    dic = {"num1":number1,"operation":"*", "num2":number2,"ans":number1*number2}
    df1 = df1.append(dic, ignore_index = True)
    df1.to_csv("/home/navgurukul/Documents/streamlit/pre_hist.csv", index = False)
    # st.dataframe(df1)


button = st.button("/")
if button:
    st.write("your answer is",number1/number2)
    st.session_state['operation']="divide"
    st.session_state["answer"]= number1/number2
    dic = {"num1":number1,"operation":"/", "num2":number2,"ans":number1/number2}
    df1 = df1.append(dic, ignore_index = True)
    df1.to_csv("/home/navgurukul/Documents/streamlit/pre_hist.csv", index = False)
    # st.dataframe(df1)


btn = st.button("last_operation")
if btn:
    st.write(st.session_state)

button5= st.button("history")
if button5:
    # df1 = df1.append(dic, ignore_index = True)
    # df1.to_csv("/home/navgurukul/Documents/streamlit/pre_hist.csv", index = False)
    st.dataframe(df1)







