import pandas as pd
from sklearn.preprocessing import StandardScaler

def make_prediction(df, model, scaler):
    df_clean = df.copy()
    df_clean = df_clean.dropna()
    df_scaled = scaler.transform(df_clean)
    preds = model.predict(df_scaled)
    return preds
