import pandas as pd
import streamlit as st
import numpy as np



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