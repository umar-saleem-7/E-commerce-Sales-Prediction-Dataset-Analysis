import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load Dataset
file_path = "Ecommerce_Sales_Prediction_Dataset.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Page Configuration
st.set_page_config(page_title="Outlier Detection", page_icon="⚠️", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #D32F2F; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .sub-sub-title {font-size: 24px; font-weight: bold; padding: 5px; border-radius: 5px;text-align: center; }
        .plot-container { background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">⚠️ Outlier Detection</p>', unsafe_allow_html=True)

st.write("Outliers are extreme values that can skew data distribution and affect model performance. "
         "Here, we detect outliers using **Boxplots, Z-score, and IQR methods**.")

# Define Numerical Columns for Outlier Analysis
numerical_cols = ["Price", "Discount", "Marketing_Spend", "Units_Sold"]

# Boxplot Visualization with Outlier Points Highlighted
st.markdown('<p class="sub-title">📦 Boxplot with Outliers Highlighted</p>', unsafe_allow_html=True)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Boxplots with Outliers Highlighted", fontsize=16)

for idx, col in enumerate(numerical_cols):
    ax = axes[idx // 2, idx % 2]
    
    # Calculate IQR for outlier detection
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Plot Boxplot
    sns.boxplot(y=df[col], ax=ax, color="lightblue", showfliers=False)  # Hide default outliers
    
    # Mark Outliers (IQR Method)
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
    ax.scatter([0] * len(outliers), outliers, color="red", label="Outliers", zorder=3)

    ax.set_title(col)
    ax.legend()

st.pyplot(fig)

st.write("The red dots represent detected **outliers based on the IQR method**. "
         "These points lie **outside 1.5 times the interquartile range (IQR)** beyond Q1 and Q3.")

# Z-score Method
st.markdown('<p class="sub-title">📊 Z-score Outlier Detection</p>', unsafe_allow_html=True)

z_threshold = 3  # Common threshold for Z-score outliers
outliers_zscore = {}

for col in numerical_cols:
    z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
    outliers_zscore[col] = df[z_scores > z_threshold]

for col, outliers in outliers_zscore.items():
    st.write(f"**{col}** has **{len(outliers)} potential outliers** using Z-score method.")

st.write("Z-score detects outliers by measuring how many standard deviations a value is away from the mean. "
         "**Values with Z-score > 3 are considered outliers.**")

# Display Outliers Detected using Z-score Method
st.markdown('<p class="sub-sub-title">📋 Z-score Outlier Data</p>', unsafe_allow_html=True)

for col, outliers in outliers_zscore.items():
    if not outliers.empty:
        st.write(f"**Outliers in {col} (Z-score Method):**")
        st.dataframe(outliers)


# IQR Method
st.markdown('<p class="sub-title">📉 Interquartile Range (IQR) Method</p>', unsafe_allow_html=True)

outliers_iqr = {}

for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_iqr[col] = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

for col, outliers in outliers_iqr.items():
    st.write(f"**{col}** has **{len(outliers)} potential outliers** using IQR method.")

st.write("The **IQR method** identifies outliers as values falling **1.5 times the interquartile range** beyond Q1 and Q3.")

# Display Outliers Detected using IQR Method
st.markdown('<p class="sub-sub-title">📋 IQR Outlier Data</p>', unsafe_allow_html=True)

for col, outliers in outliers_iqr.items():
    if not outliers.empty:
        st.write(f"**Outliers in {col} (IQR Method):**")
        st.dataframe(outliers)

# Footer
st.markdown('<p style="text-align:center; color: #888; margin-top: 50px;">📌 Identifying and handling outliers is crucial for accurate predictions.</p>', unsafe_allow_html=True)



