from numpy import column_stack
import pandas as pd
import streamlit as st

df = pd.read_csv('/home/navgurukul/Documents/streamlit/weatherDAta.csv')
print(df.to_string())
# df2 = df.to_string()
df1 = pd.DataFrame(df)
df2 = df1.loc[[i for i in range(10,24)]]
st.dataframe(df2, column_stack=[])























