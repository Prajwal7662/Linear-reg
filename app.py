import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="💡 Insurance Cost Prediction App", page_icon="💡", layout="centered")

st.title("💡 Insurance Cost Prediction App")
st.write("Predict medical insurance cost based on **Age, BMI & Smoking habits**.")

# Try to load model
try:
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    st.error("❌ model.pkl not found! Please upload or include it in the same folder as app.py.")
    st.stop()

# Input fields
age = st.number_input("Enter Age", min_value=18, max_value=100, step=1)
bmi = st.number_input("Enter BMI (Body Mass Index) — leave 0 if unknown", min_value=0.0, max_value=60.0, step=0.1)
smoker = st.selectbox("Are you a smoker?", ["No", "Yes"])

# Predict BMI if not known
if bmi == 0:
    st.info("📏 You didn’t enter BMI — estimating based on Age.")
    bmi = 18 + (age - 18) * 0.2  # simple formula (can adjust)
    st.write(f"Estimated BMI: **{bmi:.1f}**")

# Convert smoker to numeric
smoker_value = 1 if smoker == "Yes" else 0

# Prepare input data
input_data = np.array([[age, bmi, smoker_value]])

# Predict
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Insurance Cost: ₹{prediction[0]:,.2f}")
