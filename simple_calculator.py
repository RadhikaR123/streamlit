
from pyrsistent import b
import streamlit as st
import csv

def add(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def mult(a,b):
    return a*b

def division(a,b):
    return a/b

header = ["first_number","second_number","operation","answer"]
f= open('history.csv',"a",encoding ='UTF8') 
writer = csv.writer(f)
writer.writerow(header)

col1, col2 = st.columns(2)

data = []
with col1:
    number1 = int(st.number_input('Insert first number'))
    # data.append(number1)

with col2:
    number2 = int(st.number_input('Insert second number'))
    # data.append(number2)


if st.button('+'):
    data = [number1,number2,"+",number1+number2]
    st.write("your answer is :",add(number1,number2))
    if len(data) ==4:
        writer.writerow(data)
    else:
        pass

    
# elif st.button('-'):
#     st.write("your answer is :",subtraction(number1,number2))
#     data.append("-")
#     data.append(number1-number2)

# elif st.button('*'):
#     st.write("your answer is :",mult(number1,number2))
#     data.append("*")
#     data.append(number1*number2)


# elif st.button('/'):
#     st.write("your answer is :",division(number1,number2))
#     data.append("/")
#     data.append(number1/number2)

print(data)







        

