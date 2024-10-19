import streamlit as st
import pandas as pd
import numpy as np

st.write('Hello world')

penguin_df = pd.read_csv("penguins.csv")
# print(penguin_df.head())
st.dataframe(penguin_df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  uploaded_file_df = pd.read_csv(uploaded_file)
  st.dataframe(uploaded_file_df)
