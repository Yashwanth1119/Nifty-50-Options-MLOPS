import pandas as pd
import numpy as np

def add_features(df: pd.DataFrame):
    df = df.copy()

    # Add option type if not present
    if 'type' not in df.columns:
        if 'symbol' in df.columns:
            df['type'] = df['symbol'].apply(
                lambda x: 'CE' if 'CE' in str(x) else ('PE' if 'PE' in str(x) else 'UNK')
            )
        else:
            df['type'] = 'CE'  # default fallback

    df = df[df['type'].isin(['CE', 'PE'])].copy()
    df['type'] = df['type'].map({'CE': 0, 'PE': 1})

    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['expiryDate'] = df['timestamp'] + pd.Timedelta(days=7)
    df['days_to_expiry'] = (df['expiryDate'] - df['timestamp']).dt.days

    df = df.dropna(subset=['impliedVolatility', 'openInterest', 'lastPrice', 'strikePrice'])

    median_iv = df['impliedVolatility'].median()
    df['high_iv'] = (df['impliedVolatility'] > median_iv).astype(int)

    features = ['strikePrice', 'openInterest', 'lastPrice', 'days_to_expiry', 'type']
    target = 'high_iv'

    return df[features], df[target]
