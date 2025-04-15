# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uNHwj64f_Auq386UrYeq69qLR7VDydAl
"""

import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('xgboost_model.pkl')

# Function to predict productivity improvement index
def predict_productivity(income_before, crop_yield_after, farm_size,
                         seeds_purchased, fertilizers_purchased,
                         crop_yield_before):
    input_data = pd.DataFrame({
        'income_before': [income_before],
        'crop_yield_after': [crop_yield_after],
        'farm_size': [farm_size],
        'seeds_purchased': [seeds_purchased],
        'fertilizers_purchased': [fertilizers_purchased],
        'crop_yield_before': [crop_yield_before]
    })

    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit interface with styling
st.set_page_config(page_title="Productivity Predictor", page_icon="🌱", layout="wide")

# Header
st.title("🌾 Productivity Improvement Index Predictor")
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f5;
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Input fields
st.markdown("### Enter Your Data Below:")
income_before = st.number_input("Income Before (in currency)", min_value=0)
crop_yield_after = st.number_input("Crop Yield After", min_value=0)
farm_size = st.number_input("Farm Size (in acres)", min_value=0.0)
seeds_purchased = st.number_input("Seeds Purchased (in kg)", min_value=0.0)
fertilizers_purchased = st.number_input("Fertilizers Purchased (in kg)", min_value=0.0)
crop_yield_before = st.number_input("Crop Yield Before", min_value=0)

# Prediction button
if st.button("Predict"):
    prediction = predict_productivity(income_before, crop_yield_after, farm_size,
                                      seeds_purchased, fertilizers_purchased,
                                      crop_yield_before)
    st.success(f"The predicted Productivity Improvement Index is: **{prediction:.4f}**",
                icon="✅")

