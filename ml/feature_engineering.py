import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

# File paths
cleaned_log_path = r"C:\xampp\htdocs\HoneyPot\logs\cleaned_request_log.csv"
features_path = r"C:\xampp\htdocs\HoneyPot\logs\features.csv"

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        exit()

def feature_engineering(data):
    label_encoder = LabelEncoder()

    # IP Frequency
    ip_frequency = data['ip'].value_counts().to_dict()
    data['IP Frequency'] = data['ip'].map(ip_frequency)

    # User Agent Encoding
    data['User Agent Encoded'] = label_encoder.fit_transform(data['user_agent'].astype(str))

    # Activity Encoding
    data['Activity Encoded'] = label_encoder.fit_transform(data['activity'].astype(str))

    # Timestamp Features (Hour, Day, Weekday)
    data['Timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')
    data['Hour'] = data['Timestamp'].dt.hour
    data['Day'] = data['Timestamp'].dt.day
    data['Weekday'] = data['Timestamp'].dt.weekday

    # Adding a dummy 'malicious' column (for testing purposes)
    data['malicious'] = 0

    # Drop unnecessary columns
    data = data.drop(columns=['timestamp', 'user_agent', 'activity', 'ip', 'username', 'password'])
    return data

def save_features(data, file_path):
    try:
        data.to_csv(file_path, index=False)
        print(f"Feature-engineered data saved to {file_path}")
    except Exception as e:
        print(f"Error saving feature-engineered data: {e}")

# Main process
data = load_data(cleaned_log_path)
features = feature_engineering(data)
save_features(features, features_path)
