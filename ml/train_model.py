import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from datetime import datetime

# File paths
features_file = r"C:\xampp\htdocs\HoneyPot\logs\features.csv"
model_path = r"C:\xampp\htdocs\HoneyPot\ml\random_forest_model.pkl"

# Load existing data
def load_features(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Feature-engineered data loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading feature-engineered data: {e}")
        exit()

# Create synthetic malicious data
def create_synthetic_data():
    synthetic_data = pd.DataFrame({
        "activity_code": [3, 4, 5],
        "IP Frequency": [7, 5, 6],
        "User Agent Encoded": [1, 1, 0],
        "Activity Encoded": [2, 1, 3],
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")] * 3,
        "Hour": [15, 15, 15],
        "Day": [23, 23, 23],
        "Weekday": [6, 6, 6],
        "malicious": [1, 1, 1]
    })

    # Append synthetic data to the original dataset
    data = load_features(features_file)
    data = pd.concat([data, synthetic_data], ignore_index=True)

    # Save the updated dataset back to the CSV file
    data.to_csv(features_file, index=False)
    print("Synthetic data added successfully!")

# Split the data
def split_data(data):
    X = data.drop(columns=["malicious", "Timestamp"], errors='ignore')
    y = data["malicious"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Data split into training and testing sets successfully!")
    return X_train, X_test, y_train, y_test

# Train the model
def train_model(X_train, y_train):
    # Ensure all features are numeric
    X_train = X_train.select_dtypes(include=[np.number])
    y_train = y_train.astype(int)

    print("Data types after filtering non-numeric columns:")
    print(X_train.dtypes)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model training completed!")
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    # Ensure X_test only contains numeric columns, similar to training
    X_test = X_test.select_dtypes(include=[np.number])
    y_test = y_test.astype(int)
    
    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")

    # Print classification report and confusion matrix
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Save the trained model
def save_model(model, file_path):
    try:
        joblib.dump(model, file_path)
        print(f"\nTrained model saved to {file_path}")
    except Exception as e:
        print(f"Error saving the model: {e}")

# Main process
create_synthetic_data()
data = load_features(features_file)

print("Label distribution before splitting:")
print(data['malicious'].value_counts())

X_train, X_test, y_train, y_test = split_data(data)
print("Training label distribution:")
print(y_train.value_counts())
print("\nTesting label distribution:")
print(y_test.value_counts())

model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test)
save_model(model, model_path)
