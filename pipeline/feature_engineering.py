import pandas as pd 

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df['expiryDate'] = df['timestamp'] + pd.Timedelta(days=7)
    df['days_to_expiry'] = (df['expiryDate'] - df['timestamp']).dt.days
    if 'type' not in df.columns:
        if 'symbol' in df.columns:
            df['type'] = df['symbol'].apply(lambda x: 'CE' if 'CE' in str(x) else 'PE' if 'PE' in str(x) else 'UNK')
        else:
            raise ValueError("Both 'type' and 'symbol' columns are missing!")
    df = df[df['type'].isin(['CE', 'PE'])]
    df['type'] = df['type'].map({'CE': 0, 'PE': 1})
    return df