import streamlit as st
import codecs
import streamlit.components.v1 as stc



def st_calculator(cal_html, width=700,height=500):
    calc_file = codecs.open(cal_html,"r")
    page = calc_file.read()
    stc.html(page,width = width, height = height, scrolling = True)
with st.sidebar:
    st.title("Menu baar")
    choice = st.selectbox("which calculator you want to use",("simple","advanced"))
if choice == "simple":
    st.subheader("Use this simple calculator")
    st_calculator("/home/navgurukul/Documents/streamlit/calculator.html")
