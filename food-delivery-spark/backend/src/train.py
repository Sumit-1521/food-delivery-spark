import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import numpy as np

# ABSOLUTE PATHS
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(SCRIPT_DIR)
DATA_PATH = os.path.join(BACKEND_DIR, "data", "food_delivery.csv")
MODEL_PATH = os.path.join(BACKEND_DIR, "models", "model.pkl")

print(f"Data path: {DATA_PATH}")
print(f"Model path: {MODEL_PATH}")

if not os.path.exists(DATA_PATH):
    print("ERROR: Data file not found!")
    exit(1)

# Load data with pandas (no Spark needed!)
print("Loading data...")
df = pd.read_csv(DATA_PATH)
print(f"Loaded {len(df)} records")

# Drop Order_ID and clean data
df = df.drop(columns=['Order_ID'])
df = df.dropna()
print(f"After cleaning: {len(df)} records")

# Define features
categorical_cols = ["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"]
numeric_cols = ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs"]

X = df[categorical_cols + numeric_cols]
y = df["Delivery_Time_min"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# Create preprocessor and pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train model
print("Training...")
pipeline.fit(X_train, y_train)

# Evaluate - use np.sqrt instead of squared=False
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.4f}")

# Save model
os.makedirs(os.path.join(BACKEND_DIR, "models"), exist_ok=True)
joblib.dump(pipeline, MODEL_PATH)
print(f"Model saved to: {MODEL_PATH}")