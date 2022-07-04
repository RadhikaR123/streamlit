import streamlit as st

st.header("Hello....**_I_ **am** going to ceate an awesome app /**")

st.write('Hello, *World!* :sunglasses: ')

st.markdown('Streamlit is **_really_ cool**.')
st.caption('This is a string that explains something above.')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x
