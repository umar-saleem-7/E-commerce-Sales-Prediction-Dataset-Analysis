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
st.set_page_config(page_title="Feature Distribution", page_icon="📊", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .plot-container { background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">📊 Feature Distribution</p>', unsafe_allow_html=True)

st.write("This page provides an overview of the distribution of numerical and categorical features in the dataset. "
         "Understanding distributions helps in identifying patterns, anomalies, and potential preprocessing steps.")

# Separate Numerical & Categorical Columns
numerical_cols = ["Price", "Discount", "Marketing_Spend", "Units_Sold"]
categorical_cols = ["Product_Category", "Customer_Segment"]

# Subplots for Numerical Columns
st.markdown('<p class="sub-title">📈 Numerical Feature Distributions</p>', unsafe_allow_html=True)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Numerical Features Distribution", fontsize=16)

for idx, col in enumerate(numerical_cols):
    ax = axes[idx // 2, idx % 2]
    sns.histplot(df[col], bins=30, kde=True, ax=ax, color="blue")
    ax.set_title(col)

st.pyplot(fig)

st.write("The histograms above show the distribution of numerical features. The **KDE (Kernel Density Estimation) curves** "
         "help us visualize the probability density of each variable.")

# Subplots for Categorical Columns
st.markdown('<p class="sub-title">🛍️ Categorical Feature Distributions</p>', unsafe_allow_html=True)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Categorical Features Distribution", fontsize=16)

for idx, col in enumerate(categorical_cols):
    ax = axes[idx]
    sns.countplot(x=col, data=df, palette="deep", ax=ax)
    ax.set_title(col)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30)

st.pyplot(fig)

st.write("The bar charts above show the distribution of categorical variables. This helps us understand the composition "
         "of different categories in the dataset.")

# Footer
st.markdown('<p style="text-align:center; color: #888; margin-top: 50px;">📌 Understanding distributions is key to feature engineering and model performance.</p>', unsafe_allow_html=True)
