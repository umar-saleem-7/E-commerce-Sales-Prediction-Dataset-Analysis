import streamlit as st
import pandas as pd

# Load Dataset
file_path = "Ecommerce_Sales_Prediction_Dataset.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Page Configuration
st.set_page_config(page_title="Data Overview", page_icon="📊", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        body { background-color: #f7f7f7; }
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .data-box { background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">📊 Data Overview</p>', unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
category_filter = st.sidebar.multiselect("Select Product Category:", df["Product_Category"].unique(), default=df["Product_Category"].unique())
segment_filter = st.sidebar.multiselect("Select Customer Segment:", df["Customer_Segment"].unique(), default=df["Customer_Segment"].unique())

# Apply Filters
filtered_df = df[(df["Product_Category"].isin(category_filter)) & (df["Customer_Segment"].isin(segment_filter))]

# Display Filtered Data
st.markdown('<p class="sub-title">📂 Dataset</p>', unsafe_allow_html=True)
st.dataframe(filtered_df)

# Show Summary Statistics
st.markdown('<p class="sub-title">📊 Statistical Summary</p>', unsafe_allow_html=True)
st.write("Below is the summary of the key numerical features in the dataset.")
st.dataframe(filtered_df.describe())

# Additional Insights
st.markdown('<p class="sub-title">📌 Key Insights</p>', unsafe_allow_html=True)
st.write(f"✔️ **Total Records Displayed:** {len(filtered_df)}")  
st.write(f"✔️ **Total Unique Categories:** {filtered_df['Product_Category'].nunique()}")  
st.write(f"✔️ **Average Price:** {filtered_df['Price'].mean():.2f}")  
st.write(f"✔️ **Average Units Sold:** {filtered_df['Units_Sold'].mean():.2f}")  

# Footer
st.markdown('<p style="text-align:center; color: #888; margin-top: 50px;">📌 Use the sidebar to filter the dataset and explore key metrics.</p>', unsafe_allow_html=True)
