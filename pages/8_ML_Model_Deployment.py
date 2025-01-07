import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load Dataset
file_path = "Ecommerce_Sales_Prediction_Dataset.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Convert 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Select Features and Target
X = df.drop(columns=["Date", "Units_Sold"])  # Features
y = df["Units_Sold"]  # Target Variable

# Define Categorical & Numerical Features
categorical_features = ["Product_Category", "Customer_Segment"]
numerical_features = ["Price", "Discount", "Marketing_Spend"]

# Preprocessing Pipeline
preprocessor = ColumnTransformer([
    ("num_scaler", StandardScaler(), numerical_features),
    ("cat_encoder", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])

# Define Model Pipeline
model = Pipeline([
    ("preprocessing", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Performance Metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Page Configuration
st.set_page_config(page_title="ML Model Prediction", page_icon="🤖", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title { font-size: 36px; font-weight: bold; text-align: center; color: white; background: #4CAF50; padding: 10px; border-radius: 10px; }
        .sub-title { font-size: 24px; font-weight: bold; color: white; background: #2E86C1; padding: 5px; border-radius: 5px; }
        .result-box { background: #f4f4f4; padding: 15px; border-radius: 10px; text-align: center; font-size: 20px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<p class="main-title">🤖 ML Model for Sales Prediction</p>', unsafe_allow_html=True)

st.write("This page demonstrates a **Random Forest Regression Model** trained to predict `Units_Sold`. "
         "Enter values below to get a sales prediction.")

# Model Performance Display
st.markdown('<p class="sub-title">📊 Model Performance</p>', unsafe_allow_html=True)
st.write(f"**R² Score:** {r2:.2f}")
st.write(f"**Mean Absolute Error (MAE):** {mae:.2f}")
st.write(f"**Root Mean Squared Error (RMSE):** {rmse:.2f}")

# User Input Form
st.markdown('<p class="sub-title">🎯 Predict Sales</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    product_category = st.selectbox("Product Category", df["Product_Category"].unique())
    price = st.number_input("Price", min_value=0.0, max_value=10000.0, value=500.0)
    discount = st.number_input("Discount", min_value=0.0, max_value=100.0, value=10.0)

with col2:
    customer_segment = st.selectbox("Customer Segment", df["Customer_Segment"].unique())
    marketing_spend = st.number_input("Marketing Spend", min_value=0.0, max_value=20000.0, value=5000.0)

# Convert Input to DataFrame
input_data = pd.DataFrame([[product_category, customer_segment, price, discount, marketing_spend]], 
                          columns=["Product_Category", "Customer_Segment", "Price", "Discount", "Marketing_Spend"])

# Make Prediction
if st.button("🔮 Predict Units Sold"):
    prediction = model.predict(input_data)[0]
    st.markdown(f'<p class="result-box">Predicted Units Sold: <strong>{int(prediction)}</strong></p>', unsafe_allow_html=True)

# Footer
st.markdown('<p style="text-align:center; color: #888; margin-top: 50px;">📌 This prediction is based on historical sales data.</p>', unsafe_allow_html=True)
