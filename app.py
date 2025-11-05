import streamlit as st
import pickle
import numpy as np

# --- Custom Page Style ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #e3f2fd, #fce4ec);
}
h1 {
    color: #2E86C1;
    text-align: center;
    font-size: 2.5em;
    font-weight: bold;
}
h4 {
    color: #616161;
    text-align: center;
    font-style: italic;
}
footer, header {visibility: hidden;}
div.stButton > button {
    background-color: #2E86C1;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 50%;
    margin: auto;
    display: block;
    font-size: 16px;
}
div.stButton > button:hover {
    background-color: #1B4F72;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# --- Title Section ---
st.markdown(
    """
    <h1>💡 Insurance Cost Prediction App</h1>
    <h4>Predict medical insurance costs based on Age, BMI & Smoking habits</h4>
    """,
    unsafe_allow_html=True
)

# --- Load the trained model ---
model = pickle.load(open("model.pkl", "rb"))

# --- Input Section ---
st.markdown("### 🧾 Enter Your Details Below:")

age = st.number_input("Enter Age:", min_value=18, max_value=100, value=25)

# Option to calculate BMI automatically
bmi_known = st.radio("Do you know your BMI?", ["Yes", "No"])

if bmi_known == "Yes":
    bmi = st.number_input("Enter BMI:", min_value=10.0, max_value=50.0, value=22.5)
else:
    height = st.number_input("Enter Height (in cm):", min_value=100.0, max_value=250.0, value=170.0)
    weight = st.number_input("Enter Weight (in kg):", min_value=30.0, max_value=200.0, value=65.0)
    bmi = round(weight / ((height / 100) ** 2), 2)
    st.info(f"🧮 Calculated BMI: **{bmi}**")

smoker = st.selectbox("Are you a smoker?", ["No", "Yes"])
smoker_value = 1 if smoker == "Yes" else 0

# --- Prediction Button ---
if st.button("🔍 Predict Insurance Cost"):
    features = np.array([[age, bmi, smoker_value]])
    prediction = model.predict(features)
    st.success(f"💰 Estimated Insurance Cost: ₹{prediction[0]:,.2f}")

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #444; font-size: 16px;'>
        👨‍💻 Developed by <b>Prajwal Mavkar</b> | Streamlit App for Insurance Prediction
    </div>
    """,
    unsafe_allow_html=True
)
