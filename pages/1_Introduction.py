import streamlit as st
import pandas as pd

# Load dataset (replace 'your_dataset.csv' with your actual file path)
# For demonstration, we'll create a sample dataset.

df = pd.read_csv("D:\\BS Data Science\\5th semester\\Introduction to Data Science\\Project\\E-commerce-Sales-Prediction-Dataset-Analysis\\Ecommerce_Sales_Prediction_Dataset.csv")

# Title of the application
st.title("Introduction to Data Science Project")

# Subheading for the Introduction section
st.header("Introduction")

# Brief description of the dataset and project objectives
st.write("""
    The dataset chosen for this project contains information about sales across different product categories, customer segments, 
    and marketing efforts. It includes the following features:
    
    - **Date**: Unique values representing the time of the sales.
    - **Product_Category**: Categories of products such as Sports, Toys, Home Decor, Fashion, and Electronics.
    - **Price** and **Discount**: Numerical columns representing product pricing and associated discounts.
    - **Customer_Segment**: Types of customers, categorized as Occasional, Premium, or Regular.
    - **Marketing_Spend**: Amount spent on marketing efforts.
    - **Units_Sold**: Number of units sold.
""")

# Project objectives
st.subheader("Project Objectives")
st.write("""
    The objective of this project is to:
    - Perform comprehensive Exploratory Data Analysis (EDA).
    - Preprocess the dataset for machine learning.
    - Apply a suitable machine learning model to derive actionable insights.
    - Present findings through an interactive web application using Streamlit.
""")

# Slicer for filtering the dataset
st.subheader("Explore the Dataset")
selected_category = st.selectbox("Filter by Product Category", options=["All"] + df["Product_Category"].unique().tolist())

selected_customer_segments = st.selectbox("Filter by Customer Segment", options=["All"] + df["Customer_Segment"].unique().tolist())

filtered_df = df
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Product_Category"] == selected_category]
if selected_customer_segments != "All":
    filtered_df = filtered_df[filtered_df["Customer_Segment"] == selected_customer_segments]

# Display the filtered dataset
st.write("### Dataset Records", filtered_df)
