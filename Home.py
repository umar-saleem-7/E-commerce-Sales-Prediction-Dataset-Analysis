import streamlit as st

# Page Configuration
st.set_page_config(page_title="E-Commerce Sales Prediction", page_icon="🛒", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title { font-size: 42px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 15px; border-radius: 10px; }
        .sub-title { font-size: 28px; font-weight: bold; color: white; background: #2E86C1; padding: 10px; border-radius: 5px;}
        .highlight { background: #f4f4f4; padding: 15px; border-radius: 10px; font-size: 18px; }
        .footer { text-align: center; color: #888; margin-top: 50px; font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">🛒 E-Commerce Sales Prediction Dashboard</p>', unsafe_allow_html=True)

# Introduction
st.markdown("""
**Welcome to the E-Commerce Sales Prediction App!** 🚀  
This interactive dashboard allows users to:
- **📊 Explore Sales Data** through Visualizations & Insights.
- **🔍 Perform Exploratory Data Analysis (EDA)** on various features.
- **🤖 Build & Test a Machine Learning Model** to predict `Units_Sold`.
- **📈 Identify Trends & Business Opportunities** for optimization.
""")

# Project Workflow Overview
st.markdown('<p class="sub-title">🔄 Project Workflow</p>', unsafe_allow_html=True)
st.markdown("""
1️⃣ **Data Overview:** View the dataset, apply filters & get statistics.  
2️⃣ **EDA (Exploratory Data Analysis):** Analyze distributions, relationships & trends.  
3️⃣ **Outlier Detection:** Detect unusual data points for better accuracy.  
4️⃣ **Machine Learning Model:** Train a regression model to predict future sales.  
5️⃣ **Conclusion & Insights:** Summarize findings & future improvements.  
""")

# Navigation Guide
st.markdown('<p class="sub-title">📌 Navigate Through Pages</p>', unsafe_allow_html=True)
st.write("""
👉 **Data Overview** - View the dataset & apply filters.  
👉 **EDA Analysis** - Explore feature distributions, correlations & trends.  
👉 **Outlier Detection** - Identify and handle anomalies.  
👉 **ML Model** - Train a model & predict sales.  
👉 **Conclusion** - Summarize findings & next steps.  
""")

# Footer
st.markdown('<p class="footer">📌 Created by Umar Saleem | Data Science Project | 2025</p>', unsafe_allow_html=True)
