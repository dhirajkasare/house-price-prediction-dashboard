import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="House Price Prediction", layout="centered")

st.title("House Price Prediction Dashboard")
st.write("Enter house details to predict the price")

# Load model
model = joblib.load("house_price_model.pkl")

# User inputs
area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, value=3000)
bedrooms = st.slider("Bedrooms", 1, 10, 3)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
floors = st.slider("Floors", 1, 5, 2)
year_built = st.number_input("Year Built", 1900, 2025, 2010)

location = st.selectbox("Location", ["Downtown", "Suburban", "Urban", "Rural"])
condition = st.selectbox("Condition", ["Excellent", "Good", "Fair", "Poor"])
garage = st.selectbox("Garage", ["Yes", "No"])

# Predict button
if st.button("Predict House Price"):
    new_house = pd.DataFrame({
        "Area": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Floors": [floors],
        "YearBuilt": [year_built],
        "Location": [location],
        "Condition": [condition],
        "Garage": [garage]
    })

    prediction = model.predict(new_house)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
