import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="💡 Insurance Cost Prediction App", page_icon="💡")

st.title("💡 Insurance Cost Prediction App")
st.write("Predict medical insurance cost based on **Age, BMI, and Smoking habits** — No model.pkl needed!")

# Training data (small built-in dataset)
age = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60])
bmi = np.array([19, 22, 25, 27, 30, 33, 35, 28, 26])
smoker = np.array([0, 0, 0, 1, 1, 1, 0, 0, 1])
charges = np.array([2000, 2500, 3000, 12000, 15000, 18000, 4000, 5000, 20000])

# Train model automatically
X = np.column_stack((age, bmi, smoker))
model = LinearRegression()
model.fit(X, charges)

# User input
user_age = st.number_input("Enter your Age:", min_value=18, max_value=100, value=25)
user_bmi = st.number_input("Enter your BMI (if unknown, enter 0):", min_value=0.0, max_value=60.0, value=22.0)
user_smoker = st.selectbox("Do you smoke?", ["No", "Yes"])

# Auto-estimate BMI if 0
if user_bmi == 0:
    user_bmi = 18 + (user_age - 18) * 0.25
    st.info(f"📏 Estimated BMI: {user_bmi:.1f}")

smoker_val = 1 if user_smoker == "Yes" else 0

if st.button("Predict Insurance Cost"):
    input_data = np.array([[user_age, user_bmi, smoker_val]])
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Insurance Cost: ₹{prediction[0]:,.2f}")

st.markdown("---")
st.markdown("👨‍💻 Developed by **Prajwal Mavkar** | Streamlit ML Demo App")
