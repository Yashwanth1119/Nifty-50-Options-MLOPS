import streamlit as st
import pandas as pd
import joblib
from datetime import timedelta
from pipeline.prediction import make_prediction

# --- Page Configuration ---
st.set_page_config(page_title="Nifty 50 Options Predictor", layout="wide")
st.title("🔮 Nifty 50 Options IV Prediction App")
st.markdown("Upload your Option Chain CSV to predict **High/Low Implied Volatility** using ML.")

# --- Load Model & Scaler ---
try:
    model = joblib.load("artifacts/nifty_rf_model.joblib")
    scaler = joblib.load("artifacts/scaler.joblib")
except Exception as e:
    st.error(f"❌ Failed to load model/scaler: {e}")
    st.stop()

# --- File Upload ---
uploaded_file = st.file_uploader("📤 Upload Option Chain CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # --- Timestamp & Expiry Handling ---
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df['expiryDate'] = df['timestamp'] + timedelta(days=7)
        df['days_to_expiry'] = (df['expiryDate'] - df['timestamp']).dt.days
    else:
        st.error("❌ Missing 'timestamp' column in uploaded file.")
        st.stop()

    # --- Handle 'type' using 'symbol' fallback ---
    if 'type' not in df.columns:
        if 'symbol' in df.columns:
            df['type'] = df['symbol'].apply(
                lambda x: 'CE' if 'CE' in str(x) else ('PE' if 'PE' in str(x) else 'UNK')
            )
        else:
            st.error("❌ Missing both 'type' and 'symbol' columns in uploaded file.")
            st.stop()

    df = df[df['type'].isin(['CE', 'PE'])].copy()
    df['type'] = df['type'].map({'CE': 0, 'PE': 1})

    # --- Required Feature Check ---
    required_cols = ['strikePrice', 'openInterest', 'lastPrice', 'days_to_expiry', 'type']
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        st.error(f"❌ Missing required columns: {missing_cols}")
        st.stop()

    # --- Prediction ---
    try:
        features_df = df[required_cols].copy()
        predictions = make_prediction(features_df, model, scaler)
        df['High_IV_Prediction'] = predictions
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
        st.stop()

    # --- Display Results ---
    st.subheader("📄 Prediction Results")
    st.dataframe(df[['strikePrice', 'openInterest', 'lastPrice', 'days_to_expiry', 'type', 'High_IV_Prediction']].head(20))

    # --- Download Output ---
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Full Predictions CSV", data=csv, file_name="iv_predictions.csv", mime='text/csv')
