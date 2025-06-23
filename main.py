# main.py

from pipeline.data_ingestion import load_option_data
from pipeline.feature_engineering import add_features
from pipeline.model_training import train_and_save_model
from pipeline.prediction import make_prediction

import os

def main():
    print("📥 Step 1: Ingesting data...")
    df = load_option_data("data/option_chain.csv")

    print("🛠️ Step 2: Feature engineering...")
    df_features, target = add_features(df)

    print("🧠 Step 3: Training model...")
    model, scaler = train_and_save_model(df_features, target)

    print("📈 Step 4: Predicting on new data (for validation)...")
    preds = make_prediction(df_features, model, scaler)

    print("✅ Pipeline completed successfully.")

if __name__ == "__main__":
    main()
