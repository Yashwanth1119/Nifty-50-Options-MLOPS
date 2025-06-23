import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from pipeline.prediction import predict

st.title("📈 Nifty 50 Options IV Predictor")

uploaded_file = st.file_uploader("Upload Option Chain CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    # Assume preprocessing is already done or minimal here
    prediction = predict(df[['strikePrice', 'openInterest', 'lastPrice', 'days_to_expiry', 'type']],
                         model_path="../artifacts/nifty_rf_model.joblib",
                         scaler_path="../artifacts/scaler.joblib")
    st.write("Predictions (High IV = 1):")
    st.dataframe(prediction)