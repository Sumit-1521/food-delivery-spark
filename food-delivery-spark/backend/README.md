# Food Delivery Time Prediction using PySpark and React UI

## Overview

This project aims to predict food delivery times using a machine learning model built with PySpark. The backend is developed using FastAPI, which serves as an API for the frontend React application. The project includes data preprocessing, model training, and a user-friendly interface for making predictions.

## Backend Setup

### Prerequisites

- Python 3.7 or higher
- Java 8 or higher (for PySpark)
- Node.js and npm (for frontend)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd food-delivery-spark/backend
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure that the dataset `food_delivery.csv` is located in the `data` directory.

### Running the Backend

1. Start the FastAPI application:
   ```
   uvicorn src.app:app --reload
   ```

2. The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

- **POST /predict**
  - Description: Make a prediction for delivery time based on input features.
  - Request Body:
    ```json
    {
      "Distance_km": <float>,
      "Weather": "<string>",
      "Traffic_Level": "<string>",
      "Time_of_Day": "<string>",
      "Vehicle_Type": "<string>",
      "Preparation_Time_min": <int>,
      "Courier_Experience_yrs": <int>
    }
    ```
  - Response:
    ```json
    {
      "prediction": <float>
    }
    ```

## Frontend Setup

### Installation

1. Navigate to the frontend directory:
   ```
   cd food-delivery-spark/frontend
   ```

2. Install the required Node.js packages:
   ```
   npm install
   ```

### Running the Frontend

1. Start the React application:
   ```
   npm start
   ```

2. The application will be available at `http://localhost:3000`.

## Usage

- Use the frontend interface to input the required features for prediction.
- Submit the form to receive the predicted delivery time.

## Project Structure

```
food-delivery-spark
├── backend
│   ├── src
│   │   ├── train.py
│   │   ├── predict.py
│   │   ├── preprocess.py
│   │   ├── app.py
│   │   └── models
│   │       └── delivery_model
│   ├── data
│   │   └── food_delivery.csv
│   ├── requirements.txt
│   └── README.md
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── services
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
├── project-report.md
└── README.md
```

## Conclusion

This project demonstrates the integration of a machine learning model with a web application to provide real-time predictions for food delivery times. The backend handles data processing and model inference, while the frontend offers an interactive user experience.