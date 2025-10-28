# streamlit_app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 🔹 Load trained model
model = joblib.load("randomforest.pkl")

st.title("Air Quality CO Concentration Predictor by Satyam")
st.markdown("""
This app predicts **CO concentration (CO(GT))** based on environmental parameters.
""")

# 🔹 User input sliders
st.sidebar.header("Input Parameters")

def user_input_features():
    PT08_S1_CO = st.sidebar.number_input("PT08.S1(CO)", min_value=0, max_value=2000, value=1000)
    NMHC_GT = st.sidebar.number_input("NMHC(GT)", min_value=0, max_value=500, value=100)
    C6H6_GT = st.sidebar.number_input("C6H6(GT)", min_value=0.0, max_value=50.0, value=10.0)
    PT08_S2_NMHC = st.sidebar.number_input("PT08.S2(NMHC)", min_value=0, max_value=2000, value=1000)
    NOx_GT = st.sidebar.number_input("NOx(GT)", min_value=0, max_value=2000, value=100)
    PT08_S3_NOx = st.sidebar.number_input("PT08.S3(NOx)", min_value=0, max_value=2000, value=1000)
    NO2_GT = st.sidebar.number_input("NO2(GT)", min_value=0, max_value=500, value=100)
    PT08_S4_NO2 = st.sidebar.number_input("PT08.S4(NO2)", min_value=0, max_value=2000, value=1000)
    PT08_S5_O3 = st.sidebar.number_input("PT08.S5(O3)", min_value=0, max_value=2000, value=1000)
    T = st.sidebar.number_input("Temperature (T °C)", min_value=-10.0, max_value=50.0, value=20.0)
    RH = st.sidebar.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
    AH = st.sidebar.number_input("Absolute Humidity (AH)", min_value=0.0, max_value=5.0, value=1.0)
    
    data = {
        "PT08.S1(CO)": PT08_S1_CO,
        "NMHC(GT)": NMHC_GT,
        "C6H6(GT)": C6H6_GT,
        "PT08.S2(NMHC)": PT08_S2_NMHC,
        "NOx(GT)": NOx_GT,
        "PT08.S3(NOx)": PT08_S3_NOx,
        "NO2(GT)": NO2_GT,
        "PT08.S4(NO2)": PT08_S4_NO2,
        "PT08.S5(O3)": PT08_S5_O3,
        "T": T,
        "RH": RH,
        "AH": AH
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# 🔹 Display user input
st.subheader("User Input Parameters")
st.write(input_df)

# 🔹 Predict CO(GT)
prediction = model.predict(input_df)
st.subheader("Predicted CO Concentration (CO(GT))")
st.write(f"{prediction[0]:.2f} ppm")
