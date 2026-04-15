import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

DROP_COLS = ['id']
CAT_COLS = ['proto', 'service', 'state']

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.drop(columns=DROP_COLS, errors='ignore')
    df = df.dropna()
    return df

def encode_data(df):
    encoders = {}
    for col in CAT_COLS:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoders[col] = le
    return df, encoders

def scale_data(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler