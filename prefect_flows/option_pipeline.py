import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prefect import flow, task
from pipeline.data_ingestion import load_option_data
from pipeline.feature_engineering import add_features
from pipeline.model_training import train_model

@task
def ingest():
    return load_option_data("data/option_chain.csv")

@task
def engineer(df):
    return add_features(df)

@task
def train(df):
    return train_model(
        df,
        features=['strikePrice', 'openInterest', 'lastPrice', 'days_to_expiry', 'type'],
        target='high_iv',
        model_path="artifacts/nifty_rf_model.joblib",
        scaler_path="artifacts/scaler.joblib"
    )

@flow(name="NiftyOptions-FullPipeline")
def run_pipeline():
    raw = ingest()
    enriched = engineer(raw)
    enriched['high_iv'] = (enriched['impliedVolatility'] > enriched['impliedVolatility'].median()).astype(int)
    train(enriched)

if __name__ == "__main__":
    run_pipeline()
