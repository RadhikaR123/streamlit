import streamlit as st
import pandas as pd
import numpy as np

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




df = pd.DataFrame(
    np.random.rand(50,20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)

data = pd.read_csv("/home/navgurukul/Desktop/pythonClass/pandas/data.csv")
df1 = pd.DataFrame(data)

st.dataframe(df1)



chart_data = pd.DataFrame(data)

st.area_chart(chart_data)

chart_data1 =  pd.DataFrame(
    np.random.randn(50,3),
    columns=['a','b','c']
)

st.bar_chart(chart_data1)
st.bar_chart(chart_data)