import pandas as pd
import joblib
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model_path = "ml//random_forest_model.pkl"
try:
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the POST request
        data = request.get_json()

        # Convert the JSON data to a DataFrame
        df = pd.DataFrame([data])
        
        # Drop any unnecessary columns that the model wasn't trained on
        if "Timestamp" in df.columns:
            df = df.drop(columns=["Timestamp"])

        # Make predictions
        prediction = model.predict(df)

        # Prepare the response
        response = {
            "prediction": int(prediction[0]),  # Convert numpy int64 to regular int
            "status": "success"
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e), "status": "failure"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
