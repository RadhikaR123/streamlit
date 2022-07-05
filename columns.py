import streamlit as st

col1,col2, col3 = st.columns(3)

with col1:
    st.header("a flower")
    st.image("/home/navgurukul/Desktop/download.jpeg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
