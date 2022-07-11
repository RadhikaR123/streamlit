import csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime

c_date=(date.today())
print(type(c_date))

with open("pune_weather.csv","r") as f:
    file = csv.DictReader(f)
    for row in file:
        if (dict(row)["datetime"]) == str(c_date):
            print("yes")
        else:
            pass
        

# data = pd.read_csv("pre_hist.csv")
# df1 = pd.DataFrame(data)
# # print(df1)
# # for row in range(3):
# #     print(df1[row])

# # print(data["num1"])
# # st.dataframe(df1[["num1","num2"]])

# fig = plt.figure(figsize=(10,5))

# plt.bar(data['num1'],data['num2'])
# plt.xlabel("fgghj")
# plt.ylabel('khug')
# plt.title("radhika")
# st.pyplot(fig)