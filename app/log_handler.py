import csv
from datetime import datetime
import sys
import os
import requests

# Path to your CSV log file
CSV_LOG_FILE = "../logs/features.csv"
PREDICTION_API_URL = "http://127.0.0.1:5000/predict"  # Change if needed

def log_activity(activity_code, ip_frequency, user_agent_encoded, activity_encoded):
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(CSV_LOG_FILE), exist_ok=True)

        # Prepare the log entry
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hour = datetime.now().hour
        day = datetime.now().day
        weekday = datetime.now().weekday()

        # Make a prediction request to the API
        data = {
            "activity_code": activity_code,
            "IP Frequency": ip_frequency,
            "User Agent Encoded": user_agent_encoded,
            "Activity Encoded": activity_encoded,
            "Hour": hour,
            "Day": day,
            "Weekday": weekday
        }

        response = requests.post(PREDICTION_API_URL, json=data)
        prediction = response.json().get("prediction", "Error")

        # Prepare the log entry with prediction
        log_entry = [
            activity_code, ip_frequency, user_agent_encoded, activity_encoded,
            timestamp, hour, day, weekday, "", prediction
        ]

        # Check if file exists to write header
        file_exists = os.path.isfile(CSV_LOG_FILE)

        # Write to CSV
        with open(CSV_LOG_FILE, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            if not file_exists:
                writer.writerow(['activity_code', 'IP Frequency', 'User Agent Encoded', 'Activity Encoded',
                                 'Timestamp', 'Hour', 'Day', 'Weekday', 'malicious', 'Predicted'])  # Header
            writer.writerow(log_entry)

        print(f"Successfully logged: Prediction {prediction} for activity code {activity_code}")

    except Exception as e:
        print(f"Error logging activity: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 5:
        activity_code, ip_frequency, user_agent_encoded, activity_encoded = sys.argv[1:]
        log_activity(activity_code, ip_frequency, user_agent_encoded, activity_encoded)
    else:
        print("Usage: python log_handler.py <activity_code> <ip_frequency> <user_agent_encoded> <activity_encoded>")