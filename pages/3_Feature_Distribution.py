import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:\\BS Data Science\\5th semester\\Introduction to Data Science\\Project\\E-commerce-Sales-Prediction-Dataset-Analysis\\Ecommerce_Sales_Prediction_Dataset.csv")

st.title("Feature Distributions")
st.subheader("Numerical Feature Distributions")
fig, axes = plt.subplots(1, 2, figsize=(15, 5))
sns.histplot(df["Price"], kde=True, ax=axes[0]).set_title("Price Distribution")
sns.histplot(df["Discount"], kde=True, ax=axes[1]).set_title("Discount Distribution")

st.pyplot(fig)

fig, axes = plt.subplots(1, 2, figsize=(15, 5))
sns.histplot(df["Marketing_Spend"], kde=True, ax=axes[0]).set_title("Marketing Spend Distribution")
sns.histplot(df["Units_Sold"], kde=True, ax=axes[1]).set_title("Units Sold Distribution")
st.pyplot(fig)


st.subheader("Categorical Feature Counts")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.countplot(data=df, x="Product_Category", ax=axes[0]).set_title("Product Category Counts")
sns.countplot(data=df, x="Customer_Segment", ax=axes[1]).set_title("Customer Segment Counts")
st.pyplot(fig)
