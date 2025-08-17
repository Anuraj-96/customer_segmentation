import streamlit as st
import numpy as np
import pandas as pd
import joblib

#Load model
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')
encoder = joblib.load("encoder.pkl")

# Cluster name mapping
cluster_names = {
    0: "Budget-Conscious Essential Needs Shoppers",
    1: "High-Spend Active Buyers",
    2: "Luxury Lifestyle Consumers",
    3: "Price-Sensitive Light Shoppers"
}

# App title
st.set_page_config(page_title="Customer Segmentation Predictor", layout="centered")
st.title("👥 Customer Segmentation Predictor")
st.markdown("Predict customer segments based on their features.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, step=1)
income = st.number_input("Annual Income (in Lakhs INR)", min_value=0.0, step=0.1)
total_spent = st.number_input("Total Spending (in Lakhs INR)", min_value=0.0, step=0.1)
numdealspurchases = st.number_input("Number of Purchases during Deals or Discounts", min_value=0, max_value =60 ,step=1)
numwebpurchases = st.number_input("Number of Web Purchases", min_value=0,max_value =60, step=1)
numstorepurchases = st.number_input("Number of Store Purchases", min_value=0,max_value =60, step=1)
marital_status = st.selectbox("Marital Status", ["Married", "Divorced", "Widow", "In Relationship", "Single"])
total_children = st.number_input("Number of Children",min_value=0,step=1)

#Predict button
if st.button("Predict Cluster"):
    # Prepare numerical data
    num_data = np.array([[age, total_spent,income,numdealspurchases, numwebpurchases,numstorepurchases,total_children]])
    num_scaled = scaler.transform(num_data)

    # Encode categorical
    cat_data = pd.DataFrame([[marital_status]], columns=["marital_status"])
    cat_encoded = encoder.transform(cat_data)

    # Combine
    final_features = np.hstack([num_scaled, cat_encoded])

    # Predict
    cluster = kmeans.predict(final_features)[0]

    # Map to cluster name
    cluster_label = cluster_names.get(cluster, f"Cluster {cluster}")

    st.success(f"This customer belongs to: **{cluster_label}**")
