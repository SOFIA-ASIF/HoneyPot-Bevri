import pandas as pd
import requests
import json

import os

# Get current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build relative path to features.csv
features_path = os.path.abspath(os.path.join(script_dir, "../logs/features.csv"))

def get_latest_log():
    try:
        data = pd.read_csv(features_path)
        
        # Drop the 'malicious' column if it exists
        if 'malicious' in data.columns:
            data = data.drop(['malicious'], axis=1)
        
        latest_log = data.tail(1).to_dict(orient='records')[0]  # Get the latest row
        return latest_log
    except Exception as e:
        print(f"Error reading log file: {e}")
        return None

def send_to_api(log):
    url = "http://127.0.0.1:5000/predict"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(log))
        return response.json()
    except Exception as e:
        print(f"Error sending data to API: {e}")
        return None

# Get the latest log and send it to the prediction API
latest_log = get_latest_log()
if latest_log:
    prediction = send_to_api(latest_log)
    print(f"Prediction: {prediction}")
else:
    print("No valid log data found.")
