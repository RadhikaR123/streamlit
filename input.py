import streamlit as st
import pandas as pd


# button input

if st.button('Say hello', help='radhika'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    # ____________________________________________________

# Download input

# @st.cache
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode('utf-8')

# csv = convert_df("my_large_df, a,d,b,")

# st.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name='large_df.csv',
#     mime='text/csv',
# )

# ______________________________________

text_contents = '''This is some text'''
st.download_button('Download some text', text_contents )

# _________________________________-

with open("/home/navgurukul/Desktop/download.jpeg","rb") as file:
    btn = st.download_button(
        label="Download flower image",
        data=file,
        file_name="download.jpeg",
        mime="image/jpeg"
    )
# ______________________________________

# Chdeck box

agree = st.checkbox('I agree')

if agree:
     st.write('Great!')

    # _______________________________________________

#  st.radio


profession = st.radio(
     "What you want to be..?",
     ('Actor', 'Doctor', 'Engineer'))

if profession == 'Actor':
     st.write('good choice...')
elif profession== ' Doctor':
    st.write("Very good choice...")
else:
    st.write("best")

    # __________________________--------

# st.selectbox

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

# ____________________________________________---

# st.multiselect


options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

# _________________________________________________

# st.slider

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')




values = st.slider(
     'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)




from datetime import datetime, time
appointment = st.slider("schedule your appointment :", value =(time(11,30), time(12,50)))
st.write("you are scheduled for :", appointment)

start_time = st.slider("when do you start?", value=datetime(2022,2,2,12,30), format="MM/DD/YY - hh:mm")
st.write("your starting time is: ", start_time)

# _______________________________________________

# st.select_slider

num= st.select_slider("select your favourite number :", options=[1,2,3,4,5,6,7])
st. write("my favourite num is :", num)


# ________________________________--
#  number input

number = st.number_input('Insert a number')
st.write('The current number is ', number)
# ___________________________________-
# Text area(multiline text input)

txt = st.text_area('to analyze :', ''' my name is ..., i am a.............''')
st.write('sentiment:', txt)
# __________________________________

# date_input

# d = st.date_input(
#     "When's your birthday",
#     datetime.date(2022,12,9))
# st.write('Your birthday is:', d)

# Error

# ____________________________________

# Time_input

# t = st.time_input('set an alarm for', datetime.time(6, 15))
# st.write("alarm is set for ", t)

# Error
# ___________________________________________

# File uploader

uploaded_files = st.file_uploader("/home/navgurukul/Desktop/pythonClass/pandas/data.csv", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)