
from textwrap import indent
import streamlit as st
import json
import pandas as pd

dic ={}
col1, col2 = st.columns(2)

with col1:
    number1 = int(st.number_input('Insert first number'))
    # data.append(number1)
    st.session_state["first_number"]= number1
    dic["num1"]=st.session_state["first_number"]
    # st.write(st.session_state)

with col2:
    number2 = int(st.number_input('Insert second number'))
    # data.append(number2)
    st.session_state["numbre2"]= number2
    dic["num2"]=st.session_state["numbre2"]
    # st.write(st.session_state)

button1 = st.button("+")
if button1:
    st.write("your answer is",number1+number2)
    st.session_state['operation']="additoin"
    st.session_state["answer"]= number1+number2
    dic["operatio"]=st.session_state["operation"]
    dic["ans"]=st.session_state["answer"]


button2 = st.button("-")
if button2:
    st.write("your answer is",number1-number2)
    st.session_state['operation']="subtraction"
    st.session_state["answer"]= number1-number2


button3 = st.button("*")
if button3:
    st.write("your answer is",number1*number2)
    st.session_state['operation']="Multiplication"
    st.session_state["answer"]= number1*number2

button = st.button("/")
if button:
    st.write("your answer is",number1/number2)
    st.session_state['operation']="divide"
    st.session_state["answer"]= number1/number2


button5= st.button("history")
if button5:
    st.write(st.session_state)




dic2={}
if len(dic)==4:
    dic2.update(dic)
else:
    pass

with open("state.json","a") as f:
    json.dump(dic2,f,indent=2)


datafram = st.button("press")

if datafram:
    st.dataframe(st.session_state)

        

