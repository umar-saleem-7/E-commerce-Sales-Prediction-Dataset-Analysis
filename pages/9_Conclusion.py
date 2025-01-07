import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load Dataset
file_path = "Ecommerce_Sales_Prediction_Dataset.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Page Configuration
st.set_page_config(page_title="Conclusion", page_icon="🏁", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .highlight { background: #f4f4f4; padding: 10px; border-radius: 10px; }
        .footer { text-align: center; color: #888; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">🏁 Conclusion & Interactive Summary</p>', unsafe_allow_html=True)

st.write("This page summarizes the project’s findings with key insights, model performance, and recommendations for improvement. "
         "Additionally, interactive charts allow further exploration of the dataset!")

# Key Insights Section
st.markdown('<p class="sub-title">📌 Key Insights</p>', unsafe_allow_html=True)
st.markdown("""
- **📈 Sales Trends:** Some product categories had consistent sales, while others fluctuated.
- **🎯 Impact of Marketing Spend:** Strong correlation between marketing spend and units sold.
- **⚖ Discount Analysis:** Higher discounts didn’t always guarantee higher sales.
- **👥 Customer Behavior:** Premium customers exhibited different buying patterns.
""")

# Create Tabs for Interactive Visualizations
tab1, tab2, tab3 = st.tabs(["📊 Sales Trends", "🔗 Feature Relationships", "📌 Model Performance"])

# Sales Trends Visualization (Monthly Aggregation)
with tab1:
    st.markdown('<p class="sub-title">📈 Monthly Sales Trends</p>', unsafe_allow_html=True)

    # Aggregate Sales Data by Month
    df["Year-Month"] = df["Date"].dt.to_period("M")  # Convert to Year-Month format
    monthly_sales = df.groupby("Year-Month")["Units_Sold"].sum().reset_index()
    monthly_sales["Year-Month"] = monthly_sales["Year-Month"].astype(str)  # Convert period to string for plotting

    # Create Line Chart
    fig_monthly_trend = px.line(monthly_sales, x="Year-Month", y="Units_Sold",
                                title="Monthly Units Sold Over Time", markers=True)

    st.plotly_chart(fig_monthly_trend, use_container_width=True)

# Feature Relationships Visualization
with tab2:
    st.markdown('<p class="sub-title">🔗 Feature Relationships</p>', unsafe_allow_html=True)
    
    # Correlation Heatmap
    fig_corr, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(df[["Price", "Discount", "Marketing_Spend", "Units_Sold"]].corr(), annot=True, cmap="Blues", fmt=".2f", linewidths=0.5, ax=ax)
    
    st.pyplot(fig_corr)

# Model Performance Recap
with tab3:
    st.markdown('<p class="sub-title">📌 Model Performance Summary</p>', unsafe_allow_html=True)
    st.write("""
    - **R² Score:** Measures model's ability to explain variance.
    - **MAE (Mean Absolute Error):** Average error in prediction.
    - **RMSE (Root Mean Squared Error):** Penalizes larger errors.
    """)
    
    # Placeholder for metrics (Replace with actual values from ML page)
    r2_score_value = "-0.11"
    mae_value = "6.13"
    rmse_value = "7.74"

    st.metric(label="📊 R² Score", value=r2_score_value)
    st.metric(label="📉 Mean Absolute Error (MAE)", value=mae_value)
    st.metric(label="📏 Root Mean Squared Error (RMSE)", value=rmse_value)

# Future Improvements
st.markdown('<p class="sub-title">🚀 Future Improvements</p>', unsafe_allow_html=True)
st.markdown("""
- **🔄 Hyperparameter Tuning:** Optimize model for better accuracy.
- **📅 Seasonal Analysis:** Consider trends based on holidays/events.
- **📊 More Features:** Include competitor pricing, regional demand, etc.
""")

# Final Message
st.markdown('<p class="sub-title">🙏 Thank You for Exploring!</p>', unsafe_allow_html=True)
st.write("This project highlights how **Data Science & Machine Learning** can drive sales predictions. "
         "Feel free to extend this model, add features, and enhance predictions!")

# Footer
st.markdown('<p class="footer">📌 Created by Umar Saleem | Data Science Project | 2025</p>', unsafe_allow_html=True)
