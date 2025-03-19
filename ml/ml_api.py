from flask import Flask, request, jsonify
import joblib
import pandas as pd
from data_preprocess import preprocess_data

app = Flask(__name__)
model = joblib.load('ml/trained_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    processed = preprocess_data(df, is_training=False)
    prediction = model.predict(processed)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
