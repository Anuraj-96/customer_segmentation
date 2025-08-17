# 👥 Customer Segmentation App

A Streamlit web app that segments customers into distinct groups using **KMeans clustering**.  
This tool helps businesses understand customer profiles based on **demographics, income, spending habits, purchase behavior, and family status**.  

---

## 🧩 Customer Clusters
Currently, the model identifies **4 customer segments**:

| Cluster | Label                                | Key Traits |
|---------|--------------------------------------|------------|
| 0       | Budget-Conscious Essential Needs Shoppers | Older, family-heavy, low spend, conservative buyers |
| 1       | High-Spend Active Buyers             | High income, high spend, very active across web & store |
| 2       | Luxury Lifestyle Consumers           | Wealthy, discretionary spenders, not price sensitive |
| 3       | Price-Sensitive Light Shoppers       | Low income & spend, often single, low engagement |

---

[Check The Live App HERE](https://customersegmentation-7hdwnx5kylyggupn3fbjee.streamlit.app/)

---

## 🛠️ Tech Stack
- Python
- Predict customer cluster based on input data
- Streamlit (frontend)
- pandas, numpy, joblib

---

## 🚀 Features
- Predict customer cluster based on input data  
- Uses **StandardScaler** for feature scaling  
- Handles categorical data (e.g., marital status) with OneHotEncoder  
- Maps each cluster to a **business-friendly name** for easier interpretation  
- Interactive UI built with **Streamlit**  
