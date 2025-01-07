import streamlit as st

# Page Configuration
st.set_page_config(page_title="E-Commerce Sales Analysis", page_icon="🛒", layout="wide")


# Custom Styling
st.markdown("""
    <style>
        body { background-color: #f7f7f7; }
        .big-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .data-box { background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
        .highlight { background-color: #f0f0f0; padding: 10px; border-radius: 5px; }
        .footer { text-align: center; font-size: 14px; margin-top: 50px; color: #888; }
    </style>
""", unsafe_allow_html=True)


# Title and Introduction
st.markdown('<p class="big-title">📊 E-Commerce Sales Analysis & Prediction 🛍️</p>', unsafe_allow_html=True)
st.write("Welcome to the **E-Commerce Sales Analysis & Prediction App**! This interactive platform allows you to explore sales trends, "
         "perform in-depth Exploratory Data Analysis (EDA), and predict future sales using Machine Learning models.")

# Sections Overview
st.markdown('<p class="sub-title">📌 Project Overview</p>', unsafe_allow_html=True)
st.markdown("""
- 🛍️ **Understand Sales Trends** across different product categories.
- 📈 **Analyze the Impact** of discounts, marketing spend, and customer segments.
- 🤖 **Predict Future Sales** using Machine Learning models.
- 🔍 **Gain Insights** through interactive visualizations and data exploration.
""")

# Dataset Preview
st.markdown('<p class="sub-title">📂 Dataset Overview</p>', unsafe_allow_html=True)
st.markdown("""
The dataset contains **E-commerce sales transactions**, including:
- **Date** 📅 (Unique sales dates)
- **Product Category** 🏷️ (Sports, Toys, Home Decor, Fashion, Electronics)
- **Price & Discount** 💰 (Product pricing and applied discounts)
- **Customer Segment** 🎯 (Premium, Regular, Occasional customers)
- **Marketing Spend** 📢 (Advertising expenses)
- **Units Sold** 📊 (Total number of items sold per transaction)
""")

# Footer
st.markdown('<p class="footer">🚀 Created by Umar Saleem | Data Science Project | 2025</p>', unsafe_allow_html=True)
