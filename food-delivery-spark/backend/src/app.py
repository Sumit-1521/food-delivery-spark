import os
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Add this CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:8080"] if you use python -m http.server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ABSOLUTE PATHS
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(SCRIPT_DIR)
MODEL_PATH = os.path.join(BACKEND_DIR, "models", "model.pkl")

print(f"Model path: {MODEL_PATH}")

# Load model at startup (no Spark needed!)
model = joblib.load(MODEL_PATH)
print("Model loaded successfully!")

class DeliveryRequest(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Preparation_Time_min: float
    Courier_Experience_yrs: float

@app.post("/predict")
def predict_delivery_time(request: DeliveryRequest):
    try:
        # Convert to DataFrame for prediction
        input_data = pd.DataFrame([request.dict()])
        
        # Predict
        prediction = model.predict(input_data)[0]
        
        return {"predicted_delivery_time": round(float(prediction), 2)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Food Delivery Time Prediction API"}