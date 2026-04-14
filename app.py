from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# ✅ Load trained model
MODEL_PATH = "models/model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("❌ Model not found! Train model first.")

model = joblib.load(MODEL_PATH)
print("✅ Model Loaded Successfully!")


# ✅ Home route (for testing)
@app.route('/')
def home():
    return "🚀 AI Predictive Maintenance API is Running"


# ✅ API route (JSON input)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # 🔍 Validate input
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        temperature = float(data.get("temperature"))
        vibration = float(data.get("vibration"))
        current = float(data.get("current"))  # IoT current sensor

        # Prepare input
        features = np.array([[temperature, vibration, current]])

        # Prediction
        prediction = model.predict(features)[0]

        # Result
        result = "FAILURE RISK ⚠️" if prediction == 1 else "NORMAL ✅"

        return jsonify({
            "input": {
                "temperature": temperature,
                "vibration": vibration,
                "current": current
            },
            "prediction": int(prediction),
            "result": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# ✅ Run server
if __name__ == "__main__":
 app.run(debug=True, use_reloader=False)