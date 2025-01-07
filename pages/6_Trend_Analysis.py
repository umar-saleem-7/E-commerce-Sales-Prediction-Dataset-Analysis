import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
file_path = "Ecommerce_Sales_Prediction_Dataset.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Page Configuration
st.set_page_config(page_title="Trend Analysis", page_icon="📈", layout="wide")

# Custom Styling
st.markdown(""" 
    <style>
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .plot-container { background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">📈 Trend Analysis</p>', unsafe_allow_html=True)

st.write("Trend analysis helps us understand how **sales and marketing spend change over time**. "
         "This is useful for identifying seasonal patterns, long-term growth, and the impact of promotions.")

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
category_filter = st.sidebar.multiselect("Select Product Category:", df["Product_Category"].unique(), default=df["Product_Category"].unique())
segment_filter = st.sidebar.multiselect("Select Customer Segment:", df["Customer_Segment"].unique(), default=df["Customer_Segment"].unique())

# Apply Filters
filtered_df = df[(df["Product_Category"].isin(category_filter)) & (df["Customer_Segment"].isin(segment_filter))]

# Group Data by Month (instead of Date)
trend_data = filtered_df.groupby(pd.Grouper(key="Date", freq="M"))[["Units_Sold", "Marketing_Spend"]].sum()

# Time Series Trend (Monthly)
st.markdown('<p class="sub-title">📅 Time Series Trend of Sales (Monthly)</p>', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=trend_data["Units_Sold"], marker="o", linewidth=2.5, ax=ax, color="darkblue", label="Units Sold")
ax.set_title("Units Sold Over Time (Monthly)", fontsize=14)
ax.set_xlabel("Month")
ax.set_ylabel("Total Units Sold")

st.pyplot(fig)

st.write("This plot shows how total units sold vary over months. **Spikes may indicate seasonal trends, marketing campaigns, or special events.**")

# Moving Average Trend (Monthly)
st.markdown('<p class="sub-title">🔄 Moving Average for Smoother Trends (Monthly)</p>', unsafe_allow_html=True)

trend_data["Units_Sold_MA"] = trend_data["Units_Sold"].rolling(window=3).mean()  # Using a 3-month window for a moving average

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=trend_data["Units_Sold"], marker="o", linewidth=1.5, ax=ax, color="gray", label="Monthly Sales")
sns.lineplot(data=trend_data["Units_Sold_MA"], marker="o", linewidth=2.5, ax=ax, color="red", label="3-Month Moving Avg")
ax.set_title("Sales with 3-Month Moving Average", fontsize=14)
ax.set_xlabel("Month")
ax.set_ylabel("Total Units Sold")

st.pyplot(fig)

st.write("A **3-month moving average** smooths out short-term fluctuations and helps identify long-term trends.")

# Marketing Spend vs. Sales Trend (Monthly)
st.markdown('<p class="sub-title">📊 Marketing Spend vs. Sales Over Time (Monthly)</p>', unsafe_allow_html=True)

fig, ax1 = plt.subplots(figsize=(12, 5))

ax2 = ax1.twinx()
ax1.plot(trend_data.index, trend_data["Marketing_Spend"], marker="o", color="green", label="Marketing Spend", linewidth=2)
ax2.plot(trend_data.index, trend_data["Units_Sold"], marker="o", color="blue", label="Units Sold", linewidth=2)

ax1.set_xlabel("Month")
ax1.set_ylabel("Marketing Spend", color="green")
ax2.set_ylabel("Units Sold", color="blue")
ax1.set_title("Marketing Spend vs. Sales Over Time (Monthly)")

ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

st.pyplot(fig)

st.write("This chart compares **marketing spend and units sold** on a monthly basis. If higher marketing spend leads to increased sales, we can infer a **positive impact of marketing efforts.**")

# Footer
st.markdown('<p style="text-align:center; color: #888; margin-top: 50px;">📌 Understanding trends helps in optimizing sales & marketing strategies.</p>', unsafe_allow_html=True)
