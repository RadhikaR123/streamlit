import streamlit as st
import codecs
import streamlit.components.v1 as stc
import simple_calculator as sc



# def st_calculator(cal_html, width=700,height=700):
#     calc_file = codecs.open(cal_html,"r")
#     page = calc_file.read()
#     stc.html(page,width = width, height = height, scrolling = True)


with st.sidebar:
    st.title("Menu baar")
    choice = st.selectbox("which calculator you want to use",("simple","advanced","History"))


if choice == "simple":
    st.header("Use this simple calculator")
    sc
    # st_calculator("/home/navgurukul/Documents/streamlit/calculator.html", width=700, height=700)
elif choice == "advanced":
    st.subheader("You will be able to use this feature soon.... :smile:")
else:
    st.title("This is all about the app")
    st.header("Developer : **Radhika Rajoriya**")
    st.write("This app is developed under the supervision of Mr Siddhartha Jain on july 5,2022.")
    '''This enables you to use it's basic and advanced features as well
    kindly write your valuable feedback about the app..
    Thank you..'''

    num= st.select_slider("Kindly rate us between 1 to 5 :", options=[1,2,3,4,5])
    st. write("Thanks for giving us:", num, "rating")

