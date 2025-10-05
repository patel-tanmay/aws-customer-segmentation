# inference.py
from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# Create Flask app
app = Flask(__name__)

# -----------------------------
# Load Models
# -----------------------------
MODEL_DIR = "/opt/ml/model"
model = joblib.load(os.path.join(MODEL_DIR, "kmeans_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))

# -----------------------------
# Health Check (SageMaker requirement)
# -----------------------------
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "healthy"}), 200

# -----------------------------
# Inference Endpoint (SageMaker requirement)
# -----------------------------
@app.route("/invocations", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    
    # Expect JSON like: {"recency": 5, "frequency": 10, "monetary": 200}
    recency = data.get("recency")
    frequency = data.get("frequency")
    monetary = data.get("monetary")

    # Validate input
    if None in [recency, frequency, monetary]:
        return jsonify({"error": "Missing one of recency, frequency, or monetary"}), 400

    # Prepare and predict
    X = np.array([[recency, frequency, monetary]])
    X_log = np.log1p(X)
    X_scaled = scaler.transform(X_log)
    cluster = int(model.predict(X_scaled)[0])

    return jsonify({
        "cluster": cluster,
        "input_data": data
    }), 200
