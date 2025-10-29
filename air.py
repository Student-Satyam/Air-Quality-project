# ✅ Streamlit Frontend for Linear Regression Air Quality Model
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("linearr.pkl")

st.set_page_config(page_title="Air Quality CO Predictor", layout="centered")

# App title
st.title("🌫️ Air Quality CO Concentration Predictor")
st.markdown("""
This app predicts **CO concentration (CO(GT))** using a trained Linear Regression model  
based on environmental and gas sensor readings.
""")

st.caption("⚠️ Note: Model accuracy (R² ≈ 0.51). Predictions are approximate and for educational use only.")

# Sidebar for inputs
st.sidebar.header("Input Environmental Parameters")

def user_input_features():
    data = {
        "PT08.S1(CO)": st.sidebar.number_input("PT08.S1(CO)", min_value=0, max_value=2000, value=1000),
        "NMHC(GT)": st.sidebar.number_input("NMHC(GT)", min_value=0, max_value=500, value=100),
        "C6H6(GT)": st.sidebar.number_input("C6H6(GT)", min_value=0.0, max_value=50.0, value=10.0),
        "PT08.S2(NMHC)": st.sidebar.number_input("PT08.S2(NMHC)", min_value=0, max_value=2000, value=1000),
        "NOx(GT)": st.sidebar.number_input("NOx(GT)", min_value=0, max_value=2000, value=100),
        "PT08.S3(NOx)": st.sidebar.number_input("PT08.S3(NOx)", min_value=0, max_value=2000, value=1000),
        "NO2(GT)": st.sidebar.number_input("NO2(GT)", min_value=0, max_value=500, value=100),
        "PT08.S4(NO2)": st.sidebar.number_input("PT08.S4(NO2)", min_value=0, max_value=2000, value=1000),
        "PT08.S5(O3)": st.sidebar.number_input("PT08.S5(O3)", min_value=0, max_value=2000, value=1000),
        "T": st.sidebar.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=20.0),
        "RH": st.sidebar.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=50.0),
        "AH": st.sidebar.number_input("Absolute Humidity (AH)", min_value=0.0, max_value=5.0, value=1.0)
    }
    return pd.DataFrame(data, index=[0])

# Get user input
input_df = user_input_features()

# Display user inputs
st.subheader("📊 Your Input Data")
st.write(input_df)

# Predict CO concentration
prediction = model.predict(input_df)
prediction = np.clip(prediction, 0, None)  # avoid negatives

# Display prediction
st.subheader("Predicted CO Concentration (CO(GT))")
st.metric(label="CO Concentration", value=f"{prediction[0]:.2f} ppm")

# Safety messages
if prediction[0] <= 9:
    st.success("✅ Safe to go outside 🌤️")
elif prediction[0] <= 35:
    st.warning("⚠️ Moderate pollution – limit outdoor activity 😷")
else:
    st.error("🚫 High CO level – stay indoors!")

# Footer note
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Linear Regression.")
