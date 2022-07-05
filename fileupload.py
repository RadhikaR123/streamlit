from encodings import utf_8
from io import StringIO
import streamlit as st

upload_file = st.file_uploader("/home/navgurukul/Desktop/streamlit/streamlit/chart.py")
if upload_file is not None:

    byte_data = upload_file.getvalue()
    # st.write(byte_data)

    string_io = StringIO(upload_file.getvalue().decode("utf-8"))
    # st.write(string_io)

    string_data = string_io.read()
    st.write(string_data)

