import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

st.set_page_config(page_title="AI Credit Card Fraud Detection", page_icon="💳", layout="wide")

st.title("💳 AI-Powered Credit Card Fraud Detection")
st.markdown("### CTGAN-Based Synthetic Data Generation + Random Forest")
st.write("Enter the processed transaction values below and click **Predict**.")

st.sidebar.header("Transaction Features")

data = {}

# V1 to V28
for i in range(1, 29):
    data[f"V{i}"] = st.sidebar.number_input(f"V{i}", value=0.0, format="%.6f")

# Scaled features
data["scaled_amount"] = st.sidebar.number_input("Scaled Amount", value=0.0, format="%.6f")
data["scaled_time"] = st.sidebar.number_input("Scaled Time", value=0.0, format="%.6f")

input_df = pd.DataFrame([data])

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")

    st.subheader("Fraud Probability")
    st.progress(float(probability))
    st.write(f"Probability: **{probability:.2%}**")
