# Food Delivery Time Prediction using PySpark and React UI

## Overview

This project aims to predict food delivery times using a machine learning model built with PySpark and a user-friendly interface developed with React. The backend handles data processing, model training, and predictions, while the frontend provides an interactive UI for users to input data and receive predictions.

## Frontend Setup

### Prerequisites

- Node.js (version 14 or higher)
- npm (Node Package Manager)

### Installation

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required dependencies:
   ```
   npm install
   ```

### Running the Application

To start the React application, run the following command in the `frontend` directory:
```
npm start
```
This will launch the application in your default web browser at `http://localhost:3000`.

### Project Structure

- `public/`: Contains static files such as the HTML template and images.
- `src/`: Contains the source code for the React application.
  - `components/`: Reusable components for the UI.
  - `pages/`: Page components for the application.
  - `services/`: API service files for handling requests to the backend.
  - `App.tsx`: Main entry point for the React application.
  - `index.tsx`: Renders the React application into the DOM.

### API Integration

The frontend communicates with the backend API to fetch predictions. Ensure that the backend server is running before making requests from the frontend.

### Usage

1. Input the required parameters for the delivery prediction in the provided fields.
2. Click the "Predict" button to receive the estimated delivery time.
3. The prediction will be displayed on the screen.

## Conclusion

This project demonstrates the integration of a machine learning model with a web application, providing a practical solution for predicting food delivery times. The combination of PySpark for data processing and React for the frontend creates a robust and efficient system.