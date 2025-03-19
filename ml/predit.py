import pandas as pd
import joblib
from data_preprocess import preprocess_data

df = pd.read_csv('logs/request_log.csv', names=['timestamp', 'ip', 'user_agent', 'endpoint', 'params'])
model = joblib.load('ml/trained_model.pkl')

latest = df.tail(1)
processed = preprocess_data(latest, is_training=False)
pred = model.predict(processed)
print(f"Prediction for latest log: {pred[0]}")
