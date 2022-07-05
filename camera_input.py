import streamlit as st

# picture = st.camera_input("take a picture")
# if picture:
#     st.image(picture)



img_file_buffer = st.camera_input("**upload picture**")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))