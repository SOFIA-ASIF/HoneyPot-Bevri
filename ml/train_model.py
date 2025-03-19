import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from data_preprocess import preprocess_data

df = pd.read_csv('logs/request_log.csv', names=['timestamp', 'ip', 'user_agent', 'endpoint', 'params', 'label'])
X, y = preprocess_data(df)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'ml/trained_model.pkl')
print("Model trained and saved.")
