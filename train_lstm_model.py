from flask import Flask, request, jsonify
import numpy as np
import joblib
import os
from tensorflow.keras.models import load_model

app = Flask(__name__)

# -----------------------------
# LOAD MODEL + SCALER
# -----------------------------
MODEL_PATH = "models/lstm_model.h5"
SCALER_PATH = "models/scaler.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("❌ LSTM model not found!")

if not os.path.exists(SCALER_PATH):
    raise FileNotFoundError("❌ Scaler not found!")

model = load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

print("✅ LSTM Model Loaded!")

TIME_STEPS = 10


# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route('/')
def home():
    return "🚀 LSTM Predictive Maintenance API Running"


# -----------------------------
# PREDICTION ROUTE
# -----------------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Expecting list of readings
        readings = data.get("readings")

        if not readings or len(readings) < TIME_STEPS:
            return jsonify({
                "error": f"Provide at least {TIME_STEPS} readings"
            }), 400

        # Convert to array
        X = np.array([
            [r['temperature'], r['vibration'], r['pressure']]
            for r in readings
        ])

        # Normalize
        X_scaled = scaler.transform(X)

        # Take last 10 readings
        X_seq = X_scaled[-TIME_STEPS:]

        # Reshape for LSTM → (1, time_steps, features)
        X_seq = np.reshape(X_seq, (1, TIME_STEPS, 3))

        # Predict
        prediction = model.predict(X_seq)[0][0]

        result = "⚠️ FAILURE RISK" if prediction > 0.5 else "✅ NORMAL"

        return jsonify({
            "prediction_probability": float(prediction),
            "result": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)