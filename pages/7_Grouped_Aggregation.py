import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("D:\\BS Data Science\\5th semester\\Introduction to Data Science\\Project\\E-commerce-Sales-Prediction-Dataset-Analysis\\Ecommerce_Sales_Prediction_Dataset.csv")

st.title("Grouped Aggregations")

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Create a new column for the month and year
df['YearMonth'] = df['Date'].dt.to_period('M')

# Grouping by Product Category
st.subheader("Aggregation by Product Category")

product_category_agg = df.groupby('Product_Category').agg(
    total_sales=('Units_Sold', 'sum'),
    average_price=('Price', 'mean'),
    total_marketing_spend=('Marketing_Spend', 'sum')
).reset_index()

# Displaying the aggregated data
st.write(product_category_agg)

# Visualization for Product Category Aggregation
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
sns.barplot(data=product_category_agg, x='Product_Category', y='total_sales', ax=ax, palette="Set2")
ax.set_title('Total Units Sold by Product Category')
ax.set_xlabel('Product Category')
ax.set_ylabel('Total Units Sold')
plt.xticks(rotation=45)
st.pyplot(fig)

# Grouping by Customer Segment
st.subheader("Aggregation by Customer Segment")

customer_segment_agg = df.groupby('Customer_Segment').agg(
    total_sales=('Units_Sold', 'sum'),
    average_price=('Price', 'mean'),
    total_marketing_spend=('Marketing_Spend', 'sum')
).reset_index()

# Displaying the aggregated data
st.write(customer_segment_agg)

# Visualization for Customer Segment Aggregation
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
sns.barplot(data=customer_segment_agg, x='Customer_Segment', y='total_sales', ax=ax, palette="Set1")
ax.set_title('Total Units Sold by Customer Segment')
ax.set_xlabel('Customer Segment')
ax.set_ylabel('Total Units Sold')
plt.xticks(rotation=45)
st.pyplot(fig)

# Grouping by Year and Month (Time Aggregation)
st.subheader("Aggregation by Month")

# Aggregating data by YearMonth for time-based analysis
monthly_agg = df.groupby('YearMonth').agg(
    total_sales=('Units_Sold', 'sum'),
    total_marketing_spend=('Marketing_Spend', 'sum'),
    average_price=('Price', 'mean')
).reset_index()

# Convert 'YearMonth' period to datetime for plotting
monthly_agg['YearMonth'] = monthly_agg['YearMonth'].dt.to_timestamp()

# Displaying the aggregated data
st.write(monthly_agg)

# Visualization for Time Aggregation (Monthly Trend)
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
sns.lineplot(data=monthly_agg, x='YearMonth', y='total_sales', marker='o', color='b')
ax.set_title('Total Units Sold by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Total Units Sold')
plt.xticks(rotation=45)
st.pyplot(fig)
