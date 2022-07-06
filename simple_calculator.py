import streamlit as st


def add(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def mult(a,b):
    return a*b

def division(a,b):
    return a/b


col1, col2 = st.columns(2)


with col1:
    number1 = st.number_input('Insert first number')

with col2:
    number2 = st.number_input('Insert second number')



if st.button('+'):
    st.write(add(number1,number2))
elif st.button('-'):
    st.write(subtraction(number1,number2))
elif st.button('*'):
    st.write(mult(number1,number2))
elif st.button('/'):
    st.write(division(number1,number2))


        

