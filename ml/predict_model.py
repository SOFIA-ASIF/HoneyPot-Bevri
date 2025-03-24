import pandas as pd
import joblib

# Load the trained model
model_path = r"C:\xampp\htdocs\HoneyPot\ml\random_forest_model.pkl"
try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Load the data for prediction
data_path = r"C:\xampp\htdocs\HoneyPot\logs\features.csv"
try:
    data = pd.read_csv(data_path)
    print("Data loaded successfully!")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Drop non-numeric columns and the label (if present)
features = data.drop(columns=["malicious", "Timestamp"], errors='ignore')

try:
    # Make predictions
    predictions = model.predict(features)
    data["Predicted"] = predictions

    # Print the predictions
    print(data[["activity_code", "malicious", "Predicted"]])
except Exception as e:
    print(f"Error during prediction: {e}")
