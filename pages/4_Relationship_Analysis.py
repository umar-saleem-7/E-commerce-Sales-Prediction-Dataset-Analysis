import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:\\BS Data Science\\5th semester\\Introduction to Data Science\\Project\\E-commerce-Sales-Prediction-Dataset-Analysis\\Ecommerce_Sales_Prediction_Dataset.csv")

st.title("Relationships Between Features")

# Correlation Analysis
st.subheader("Correlation Heatmap")
# Select only numeric columns for correlation analysis
numeric_df = df.select_dtypes(include=["number"])
if numeric_df.empty:
    st.warning("No numeric columns available for correlation analysis.")
else:
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Pairwise Relationships
st.subheader("Pairwise Relationships")
try:
    pairplot_fig = sns.pairplot(df, diag_kind="kde", hue="Customer_Segment")
    st.pyplot(pairplot_fig)
except ValueError as e:
    st.error(f"Error in pairwise plotting: {e}")