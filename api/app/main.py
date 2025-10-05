from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Initialize FastAPI app
app = FastAPI(title="RFM Customer Segmentation API")

# Define paths dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load models
model_path = os.path.join(MODEL_DIR, "kmeans_model.pkl")
scaler_path = os.path.join(MODEL_DIR, "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Define input schema
class RFMInput(BaseModel):
    recency: float
    frequency: float
    monetary: float

@app.get("/")
def root():
    return {"message": "RFM API is running successfully."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: RFMInput):
    # Convert input to array
    X = np.array([[data.recency, data.frequency, data.monetary]])
    
    # Log-transform + scale
    X_log = np.log1p(X)
    X_scaled = scaler.transform(X_log)
    
    # Predict cluster
    cluster = int(model.predict(X_scaled)[0])
    
    return {"cluster": cluster, "input_data": data.dict()}
