from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pickle
import pandas as pd


# Create the FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the pickled Random Forest model
with open('random_forest_model.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

# Test case for prediction
test_features = [[230, 16, 1, 7, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]


# Define a route to render the HTML form
@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Define a route to handle preprocessing and prediction
@app.post("/predict")
async def predict(
    request: Request,
    AMENITIES: int = Form(...),
    BUILDINGID: str = Form(...),
    CAPACITY: int = Form(...),
    time_of_day: str = Form(...),
    day_of_week: int = Form(...),
    month_of_year: int = Form(...),

):
    try:
        # Prepare the features for prediction
        features = {'AMENITIES_en': 230,
                    'time_of_day': int(time_of_day[:2]),
                    'day_of_week': day_of_week,
                    'month_of_year': month_of_year,
                    'CAPACITY': CAPACITY,
                    'BUILDINGID_B029': 0,
                    'BUILDINGID_B030': 0,
                    'BUILDINGID_B031': 0,
                    'BUILDINGID_B033': 0,
                    'BUILDINGID_B039': 0,
                    'BUILDINGID_B042': 0,
                    'BUILDINGID_B044': 1,
                    'BUILDINGID_B047': 0,
                    'BUILDINGID_B060': 0,
                    'BUILDINGID_B072': 0,
                    'BUILDINGID_Other': 0
                    }

        features[BUILDINGID] = 1

        # Perform predictions using the loaded model
        if CAPACITY == -1:
            prediction = str(rf_model.predict(test_features)[0])
        else:
            prediction = str(rf_model.predict([list(features.values())])[0])

        # Convert the prediction to a meaningful output
        if prediction == 'z':
            prediction = 'Under 2 hours'
        elif prediction == 'A':
            prediction = '2-4 hours'
        else:
            prediction = 'Over 4 hours'

        # Render the prediction along with the input form
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "prediction": prediction},
        )

    except Exception as e:
        return {'error': str(e)}
