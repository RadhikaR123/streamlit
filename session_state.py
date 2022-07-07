import streamlit as st
import csv
import json

if 'data' not in st.session_state:
    st.session_state['data']= {}
if 'data1' not in st.session_state:
    st.session_state['data1']= {}

def in_callback():
    st.session_state['data']['key']=number
    st.session_state['data']['key1']=number1
# def in_callback1():
#      st.session_state['data1']['key1']=number1


number = st.number_input('inser a num', on_change= in_callback )
number1 = st.number_input('inser an num', on_change= in_callback)
st.write(st.session_state['data'])
# st.write(st.session_state['data1'])

with open("state.json","a") as f:
    json.dump(st.session_state['data'],f,indent=2)




