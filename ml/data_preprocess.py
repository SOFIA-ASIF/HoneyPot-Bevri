import pandas as pd

def preprocess_data(df, is_training=True):
    df['ua_length'] = df['user_agent'].apply(len)
    df['param_length'] = df['params'].apply(len)
    df['endpoint_code'] = df['endpoint'].astype('category').cat.codes

    features = df[['ua_length', 'param_length', 'endpoint_code']]

    if is_training and 'label' in df.columns:
        labels = df['label']
        return features, labels
    return features
