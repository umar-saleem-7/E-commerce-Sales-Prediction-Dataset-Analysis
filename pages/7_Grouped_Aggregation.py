import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset (update file path if needed)
file_path = "Ecommerce_Sales_Prediction_Dataset.csv"
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Page Configuration
st.set_page_config(page_title="EDA - Sales Group Aggregation", page_icon="📊", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .plot-container { background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">📊 Group Aggregation - Sales by Category and Customer Segment</p>', unsafe_allow_html=True)

# Introduction Text
st.write("""
    This page showcases the **Sales by Product Category** and **Customer Segment**. By aggregating the data, we can identify how 
    **units sold**, **marketing spend**, and **total sales** vary across different product categories and customer segments.
    This analysis is key to understanding the overall sales performance and customer preferences.
""")

# Group Data by Product Category and Customer Segment
sales_by_category_segment = df.groupby(["Product_Category", "Customer_Segment"]).agg(
    Total_Sales=("Price", "sum"), 
    Total_Units_Sold=("Units_Sold", "sum"),
    Total_Marketing_Spend=("Marketing_Spend", "sum")
).reset_index()

# Visualizations

# Total Sales by Product Category and Customer Segment
st.markdown('<p class="sub-title">📊 Total Sales by Category and Customer Segment</p>', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="Product_Category", y="Total_Sales", hue="Customer_Segment", data=sales_by_category_segment, ax=ax)
ax.set_title("Total Sales by Category and Customer Segment", fontsize=14)
ax.set_xlabel("Product Category")
ax.set_ylabel("Total Sales")

# Move the legend outside the plot area
ax.legend(title='Customer Segment', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

st.pyplot(fig)

st.write("The bar chart above shows **total sales** for each **Product Category** segmented by **Customer Segment**. It helps us understand which categories and customer groups contribute the most to sales.")

# Total Units Sold by Product Category and Customer Segment
st.markdown('<p class="sub-title">📦 Total Units Sold by Category and Customer Segment</p>', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="Product_Category", y="Total_Units_Sold", hue="Customer_Segment", data=sales_by_category_segment, ax=ax)
ax.set_title("Total Units Sold by Category and Customer Segment", fontsize=14)
ax.set_xlabel("Product Category")
ax.set_ylabel("Total Units Sold")

# Move the legend outside the plot area
ax.legend(title='Customer Segment', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

st.pyplot(fig)

st.write("The bar chart above illustrates the **total number of units sold** for each **Product Category** and **Customer Segment**. This helps in analyzing which categories and segments are more active in terms of sales volume.")

# Total Marketing Spend by Product Category and Customer Segment
st.markdown('<p class="sub-title">💰 Total Marketing Spend by Category and Customer Segment</p>', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x="Product_Category", y="Total_Marketing_Spend", hue="Customer_Segment", data=sales_by_category_segment, ax=ax)
ax.set_title("Total Marketing Spend by Category and Customer Segment", fontsize=14)
ax.set_xlabel("Product Category")
ax.set_ylabel("Total Marketing Spend")

# Move the legend outside the plot area
ax.legend(title='Customer Segment', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

st.pyplot(fig)

st.write("This chart compares the **total marketing spend** for each **Product Category** and **Customer Segment**. It allows us to evaluate how much marketing budget is allocated to each category and segment.")

# Footer
st.markdown('<p style="text-align:center; color: #888; margin-top: 50px;">📌 Group aggregation helps in identifying sales patterns across categories and segments.</p>', unsafe_allow_html=True)