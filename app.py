from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and label encoder
model = joblib.load('packaging_strength_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return 'Packaging Strength Prediction API is running.'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Example: expects data = {"features": [list of features]}
    features = data.get('features')
    if features is None:
        return jsonify({'error': 'No features provided.'}), 400

    # Convert to DataFrame for model input
    X = pd.DataFrame([features])

    # If label encoding is needed for a specific column, do it here
    # Example: X['column'] = label_encoder.transform(X['column'])
    # (Uncomment and adjust as needed)

    prediction = model.predict(X)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True) 