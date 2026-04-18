from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class PredictionInput(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Preparation_Time_min: float
    Courier_Experience_yrs: float

# Load the trained model
model_path = "models/delivery_model"
model = PipelineModel.load(model_path)

@app.post("/predict")
def predict(input_data: PredictionInput):
    input_dict = input_data.dict()
    
    # Convert input data to DataFrame
    spark = SparkSession.builder.appName("FoodDeliveryPrediction").getOrCreate()
    input_df = spark.createDataFrame([input_dict])
    
    # Make predictions
    predictions = model.transform(input_df)
    predicted_time = predictions.select("prediction").first()[0]
    
    spark.stop()
    
    return {"predicted_delivery_time": predicted_time}