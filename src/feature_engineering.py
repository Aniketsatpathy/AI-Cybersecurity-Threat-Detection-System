def create_features(df):
    if 'sbytes' in df.columns and 'dbytes' in df.columns:
        df['byte_ratio'] = df['sbytes'] / (df['dbytes'] + 1)

    if 'Spkts' in df.columns and 'Dpkts' in df.columns:
        df['pkt_ratio'] = df['Spkts'] / (df['Dpkts'] + 1)

    return df