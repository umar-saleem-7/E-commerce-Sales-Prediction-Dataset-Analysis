# 🛒 E-Commerce Sales Prediction Dashboard

![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red) 
![Python](https://img.shields.io/badge/Built%20with-Python-blue) 
![Machine Learning](https://img.shields.io/badge/Powered%20by-Machine%20Learning-green)

## 📌 Project Overview

This **E-Commerce Sales Prediction Dashboard** is a **Streamlit-powered web application** that allows users to:

- **📊 Explore Sales Data** using interactive visualizations.
- **🔍 Perform Exploratory Data Analysis (EDA)** on key features.
- **📈 Identify Trends & Anomalies** in sales patterns.
- **🤖 Train a Machine Learning Model** to predict `Units_Sold`.
- **📌 Gain Insights & Business Recommendations** for optimization.

---

## 📂 Dataset Information

This project uses an **E-Commerce Sales dataset** from Kaggle with the following columns:

| Column Name            | Description |
|------------------------|-------------|
| `Date`                | Date of transaction |
| `Product_Category`    | Category of product (Sports, Toys, Fashion, etc.) |
| `Price`               | Product price (Float) |
| `Discount`            | Discount applied (Float) |
| `Customer_Segment`    | Type of customer (Premium, Regular, Occasional) |
| `Marketing_Spend`     | Advertising spend (Float) |
| `Units_Sold`          | Number of units sold (Integer) |

---

## 🚀 Project Workflow

1️⃣ **Introduction Page**  
   📌 Overview of the project, purpose, and workflow.

2️⃣ **Data Overview**  
   📊 View raw dataset with filtering options and statistical summaries.

3️⃣ **Exploratory Data Analysis (EDA)**  
   🔹 **Feature Distributions:** Histograms & Count Plots  
   🔹 **Relationship Analysis:** Correlations, Pair Plots, Heatmaps  
   🔹 **Outlier Detection:** Boxplots, IQR, Z-score analysis  
   🔹 **Trend Analysis:** Time-series insights with moving averages  
   🔹 **Grouped Aggregation:** Category-wise sales analysis  

4️⃣ **Machine Learning Model Deployment**  
   🤖 **Regression Model** to predict `Units_Sold` based on:  
   - Price  
   - Discount  
   - Marketing Spend  
   - Product Category  
   - Customer Segment  

   ✅ **Model Performance Evaluation** using:  
   - R² Score  
   - Mean Absolute Error (MAE)  
   - Root Mean Squared Error (RMSE)  

5️⃣ **Conclusion Page**  
   📌 Key insights, model results, future improvements, and recommendations.

---

## 🛠️ Installation & Running the App

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/umar-saleem-7/E-commerce-Sales-Prediction-Dataset-Analysis.git
cd ecommerce-sales-prediction

pip install -r requirements.txt

streamlit run Home.py

