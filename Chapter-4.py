#How to deal with data
import streamlit as st
import pandas as pd

st.title("Hello Coders!")

file = st.file_uploader("Upload your file here",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary")
    st.write(df.describe())

if file:
    city = df['city'].unique()
    selected_city = st.selectbox("Select The city",city)
    filtered_dataframe = df[df['city'] == selected_city]
    st.dataframe(filtered_dataframe)