from fastapi import FastAPI
import pickle
from pydantic import BaseModel


# Create a FastAPI web app
app = FastAPI()

# Load the pickled Random Forest model
with open('random_forest_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

# Define a route for a simple "Hello, World!" message
@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Create a Pydantic model for input data validation
class PredictionInput(BaseModel):
    AMENITIES: float
    time_of_day: float
    day_of_week: float
    month_of_year: float
    CAPACITY: float
    BUILDINGID: float
    Total_Building_Meetings: float

# Define the prediction route
@app.post('/predict')
def predict(input_data: PredictionInput):
    try:
        # Extract feature values from the input_data object
        features = [
            input_data.AMENITIES,
            input_data.time_of_day,
            input_data.day_of_week,
            input_data.month_of_year,
            input_data.CAPACITY,
            input_data.BUILDINGID,
            input_data.Total_Building_Meetings
        ]

        # Perform predictions using the loaded model
        prediction = int(rf_model.predict([features])[0])  # Convert prediction to int

        # Create a JSON response
        response = {
            'prediction': prediction
        }

        return response

    except Exception as e:
        return {'error': str(e)}

# Run the FastAPI app using uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
