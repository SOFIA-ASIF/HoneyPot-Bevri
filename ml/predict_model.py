import pandas as pd
import joblib
import os

# Get current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build relative path to random_forest_model.pkl
model_path = os.path.abspath(os.path.join(script_dir, "random_forest_model.pkl"))
try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build path to logs/features.csv
data_path = os.path.abspath(os.path.join(script_dir, "../logs/features.csv"))
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
