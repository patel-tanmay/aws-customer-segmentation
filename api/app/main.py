from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np

app = FastAPI(title="RFM Customer Segmentation API")

# Load model and scaler
model = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.post("/predict")
def predict_rfm(recency: float, frequency: float, monetary: float):
    # Log and scale
    X = np.log1p([[recency, frequency, monetary]])
    X_scaled = scaler.transform(X)
    cluster = model.predict(X_scaled)[0]
    return {"cluster": int(cluster)}
