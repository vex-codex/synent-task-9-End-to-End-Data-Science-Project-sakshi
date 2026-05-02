import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🏠 House Price Prediction App")

st.write("Enter property details to predict price")

# Inputs
area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Number of Bedrooms", min_value=0)
age = st.number_input("House Age (years)", min_value=0)

# Prediction
if st.button("Predict Price"):
    data = np.array([[area, bedrooms, age]])
    prediction = model.predict(data)
    
    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")