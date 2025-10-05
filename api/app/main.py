from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Initialize FastAPI app
app = FastAPI(title="RFM Customer Segmentation API")

# --- Dynamically resolve the model directory ---
# Current file is inside: /home/sagemaker-user/rfm_project/api/app/main.py
# main.py → app → api → rfm_project → models
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "models"))

print("✅ Looking for models in:", MODEL_DIR)


# --- Load models ---
model = joblib.load(os.path.join(MODEL_DIR, "kmeans_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))

# --- Define schema ---
class RFMInput(BaseModel):
    recency: float
    frequency: float
    monetary: float

@app.get("/")
def root():
    return {"message": "RFM API is running successfully!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: RFMInput):
    X = np.array([[data.recency, data.frequency, data.monetary]])
    X_log = np.log1p(X)
    X_scaled = scaler.transform(X_log)
    cluster = int(model.predict(X_scaled)[0])
    return {"cluster": cluster, "input_data": data.dict()}
