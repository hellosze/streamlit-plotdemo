import streamlit as st
import pandas as pd

st.write('Hello world')

penguin_df = pd.read_csv("penguins.csv")
# print(penguin_df.head())
st.dataframe(penguin_df)


uploaded_file = st.file_uploader("Choose a file")
uploaded_file_df = pd.read_csv(uploaded_file)
st.dataframe(uploaded_file_df)
