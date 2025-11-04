import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app title
st.title("💡 Health Risk Prediction App")
st.write("This app predicts the health risk or medical cost based on Age, BMI, and Smoking status.")

# Input fields
age = st.number_input("Enter Age (in years):", min_value=1, max_value=120, value=25)
bmi = st.number_input("Enter BMI:", min_value=10.0, max_value=60.0, value=22.0)
smoker_status = st.selectbox("Smoker:", ["No", "Yes"])

# Convert smoker input to numeric (0 or 1)
smoker_yes = 1 if smoker_status == "Yes" else 0

# Predict button
if st.button("Predict"):
    input_data = np.array([[age, bmi, smoker_yes]])
    prediction = model.predict(input_data)
    st.success(f"🩺 Predicted Output: {prediction[0]:.2f}")

# Footer
st.markdown("---")
st.caption("Developed by Hrishikesh Bhapkar | Streamlit App for ML Model")
