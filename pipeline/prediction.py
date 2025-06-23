import joblib
import pandas as pd

def predict(data: pd.DataFrame, model_path: str, scaler_path: str):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    X = scaler.transform(data)
    return model.predict(X)