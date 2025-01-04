import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("D:\\BS Data Science\\5th semester\\Introduction to Data Science\\Project\\E-commerce-Sales-Prediction-Dataset-Analysis\\Ecommerce_Sales_Prediction_Dataset.csv")

st.title("Data Overview")
st.subheader("Summary Statistics")
st.write(df.describe())

st.subheader("Data Types")
st.write(df.dtypes)
st.subheader("Unique Values per Column")
st.write(df.nunique())

st.subheader("Missing Value Analysis")
st.write(df.isnull().sum())
