import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("D:\\BS Data Science\\5th semester\\Introduction to Data Science\\Project\\E-commerce-Sales-Prediction-Dataset-Analysis\\Ecommerce_Sales_Prediction_Dataset.csv")

st.title("Trend Analysis (Month-Wise)")

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Create a new column for the month and year
df['YearMonth'] = df['Date'].dt.to_period('M')

# Aggregate the data by month to analyze the trend
trend_data = df.groupby('YearMonth')['Units_Sold'].sum().reset_index()

# Convert 'YearMonth' back to a datetime format for plotting
trend_data['YearMonth'] = trend_data['YearMonth'].dt.to_timestamp()

# Create a line plot to visualize the trend on a month-wise basis
plt.figure(figsize=(10, 6))
sns.lineplot(data=trend_data, x='YearMonth', y='Units_Sold')
plt.title('Units Sold Over Time (Month-Wise)')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.grid(True)

# Display the plot
st.pyplot(plt)