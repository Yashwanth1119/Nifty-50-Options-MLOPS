import pandas as pd

def load_option_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df
