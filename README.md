# 🩺 Health Risk Prediction using Streamlit


This project is a **Streamlit web application** that predicts health risk (or medical cost) based on three key input parameters — **Age**, **BMI**, and **Smoking Status** — using a pre-trained machine learning model.

Link - https://linear-reg-5ty8ozfeagjhhun8qerurv.streamlit.app/

---

## 📁 Project Structure
├── app.py # Streamlit application
├── best_model.pkl # Trained ML model
├── requirements.txt # Required Python libraries
└── README.md # Project documentation

---

## 🚀 How to Run the App

### 1️⃣ Install Required Libraries
Open your terminal or command prompt and run:
```bash
pip install -r requirements.txt
2️⃣ Run the Streamlit App
After installation, start the web app with:

bash
Copy code
streamlit run app.py
3️⃣ Use the App
Enter Age (in years)

Enter BMI (Body Mass Index)

Select Smoker status (Yes/No)

Click Predict to see the predicted output

🧠 Model Information
Model file: best_model.pkl

Input features:

age

bmi

smoker_yes (1 if smoker, 0 if not)

Output: Predicted health risk or medical cost (continuous value)

🧰 Technologies Used
Python

Streamlit (Web Framework)

Scikit-learn (Machine Learning)

NumPy, Pandas


💬 Notes
Ensure your model file (best_model.pkl) is in the same directory as app.py before running the app.


