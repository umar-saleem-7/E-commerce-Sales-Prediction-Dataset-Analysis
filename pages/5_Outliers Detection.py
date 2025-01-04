import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("D:\\BS Data Science\\5th semester\\Introduction to Data Science\\Project\\E-commerce-Sales-Prediction-Dataset-Analysis\\Ecommerce_Sales_Prediction_Dataset.csv")

st.title("Outlier Detection")

# Function to detect outliers using IQR method
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Subplots for box plots of numerical columns
st.subheader("Box Plots for Outlier Detection")

# Get numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Create subplots
num_columns = len(numeric_columns)
fig, axes = plt.subplots(nrows=num_columns, ncols=1, figsize=(8, 4*num_columns))

# Plot each numeric column in a separate subplot
for i, column in enumerate(numeric_columns):
    sns.boxplot(data=df, x=column, ax=axes[i], palette="Set2")
    axes[i].set_title(f"Box Plot for {column}")
    axes[i].set_xlabel('')

# Adjust layout and display
plt.tight_layout()
st.pyplot(fig)

# Display outliers in each column
for column in numeric_columns:
    outliers = detect_outliers_iqr(df, column)
    if not outliers.empty:
        st.write(f"**Outliers in {column}:**")
        st.write(outliers)
