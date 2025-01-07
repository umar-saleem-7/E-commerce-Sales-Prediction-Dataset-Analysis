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
st.set_page_config(page_title="Relationship Analysis", page_icon="🔗", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .plot-container { background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">🔗 Relationship Analysis</p>', unsafe_allow_html=True)

st.write("This page explores relationships between different numerical features in the dataset. "
         "Identifying patterns between variables helps in feature selection and predictive modeling.")

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
category_filter = st.sidebar.multiselect("Select Product Category:", df["Product_Category"].unique(), default=df["Product_Category"].unique())
segment_filter = st.sidebar.multiselect("Select Customer Segment:", df["Customer_Segment"].unique(), default=df["Customer_Segment"].unique())

# Apply Filters
filtered_df = df[(df["Product_Category"].isin(category_filter)) & (df["Customer_Segment"].isin(segment_filter))]

# Scatter Plots
st.markdown('<p class="sub-title">📈 Scatter Plot Analysis</p>', unsafe_allow_html=True)

scatter_pairs = [
    ("Price", "Units_Sold"),
    ("Marketing_Spend", "Units_Sold"),
    ("Discount", "Units_Sold"),
    ("Price", "Marketing_Spend")
]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Feature Relationships (Scatter Plots)", fontsize=16)

for idx, (x, y) in enumerate(scatter_pairs):
    ax = axes[idx // 2, idx % 2]
    sns.scatterplot(x=filtered_df[x], y=filtered_df[y], alpha=0.6, ax=ax, color="blue")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(f"{x} vs {y}")

st.pyplot(fig)

st.write("The scatter plots above reveal important relationships between variables. "
         "For instance, we can observe how marketing spend affects units sold, or how discounts influence purchase behavior.")

# Correlation Heatmap
st.markdown('<p class="sub-title">🔍 Correlation Heatmap</p>', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10, 6))
corr_matrix = filtered_df[["Price", "Discount", "Marketing_Spend", "Units_Sold"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="Blues", fmt=".2f", linewidths=0.5, ax=ax)

st.pyplot(fig)

st.write("The heatmap above shows the correlation between numerical features. **A correlation closer to +1 or -1 indicates a strong relationship, while values near 0 suggest weak correlation.** "
         "This helps in identifying which features are useful for predictive modeling.")

# Footer
st.markdown('<p style="text-align:center; color: #888; margin-top: 50px;">📌 Use this analysis to understand feature relationships and improve model performance.</p>', unsafe_allow_html=True)

from scipy.stats import pearsonr, spearmanr, kendalltau

st.markdown('<p class="sub-title">📊 Pairwise Statistical Analysis</p>', unsafe_allow_html=True)

numerical_features = ["Price", "Discount", "Marketing_Spend", "Units_Sold"]
pairwise_results = []

# Compute Pairwise Correlations
for i in range(len(numerical_features)):
    for j in range(i + 1, len(numerical_features)):
        feature1, feature2 = numerical_features[i], numerical_features[j]
        
        pearson_corr, _ = pearsonr(filtered_df[feature1], filtered_df[feature2])
        spearman_corr, _ = spearmanr(filtered_df[feature1], filtered_df[feature2])
        kendall_corr, _ = kendalltau(filtered_df[feature1], filtered_df[feature2])
        
        pairwise_results.append({
            "Feature 1": feature1,
            "Feature 2": feature2,
            "Pearson Correlation": round(pearson_corr, 2),
            "Spearman Correlation": round(spearman_corr, 2),
            "Kendall Correlation": round(kendall_corr, 2),
        })

# Convert to DataFrame for Display
pairwise_df = pd.DataFrame(pairwise_results)

# Display Table
st.write("The table below shows the correlation coefficients between different numerical features. "
         "These values help in understanding **linear and rank-based relationships** between variables.")
st.dataframe(pairwise_df.style.background_gradient(cmap="coolwarm"))


# Pair Plot for Comprehensive Pairwise Analysis
st.markdown('<p class="sub-title">📊 Pairwise Feature Relationships</p>', unsafe_allow_html=True)

st.write("Pairwise relationships between features provide a holistic view of data patterns and interdependencies. "
         "This can uncover clusters, trends, or other useful insights.")

# Create Pair Plot
pairplot_cols = ["Price", "Discount", "Marketing_Spend", "Units_Sold"]  # Select relevant columns
sns.pairplot(filtered_df[pairplot_cols], diag_kind="kde", corner=True, palette="husl")

# Display the Plot
st.pyplot(plt.gcf())

st.write("The pair plot above shows pairwise scatter plots for numerical features, "
         "along with density distributions on the diagonal.")
