import requests
import pandas as pd

def make_prediction(log_data):
    try:
        # Prediction API URL
        url = "http://127.0.0.1:5000/predict"
        
        # Make the POST request to the prediction API
        response = requests.post(url, json=log_data)
        result = response.json()
        return result.get("prediction", "Error")
    except Exception as e:
        print(f"Prediction API error: {e}")
        return "Error"

def predict_and_log():
    # Load the latest log data from CSV
    data = pd.read_csv(r"C:\xampp\htdocs\HoneyPot\logs\features.csv")
    
    # Get the last log entry for prediction
    last_entry = data.iloc[-1].to_dict()
    prediction = make_prediction(last_entry)
    
    # Add prediction to the data and save it
    data.at[data.index[-1], "Predicted"] = prediction
    data.to_csv(r"C:\xampp\htdocs\HoneyPot\logs\features.csv", index=False)
    print(f"Prediction: {prediction}")

predict_and_log()
