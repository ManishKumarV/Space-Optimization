# Space-Optimization-Challenge

## Preliminary Data Analysis and Insights

This repository contains code for preliminary data analysis and insights derived from various datasets related to meetings, room bookings, desk bookings, and building information. The code provides insights into meeting durations, meeting patterns, building popularity, floor usage, desk bookings, and amenities usage.

### Dependencies

Make sure you have the following Python packages installed in your environment:

- `os`
- `glob`
- `re`
- `math`
- `numpy`
- `pandas`
- `seaborn`
- `matplotlib`
- `folium`
- `geopy`
- `sklearn`
- `warnings`

You can install these packages using `pip`:

```bash
pip install -r requirements.txt
```

## FastAPI Model Deployment

This repository contains code for deploying a machine-learning model using FastAPI. The model, a Random Forest Classifier, predicts meeting room durations based on various features.

### Project Structure

- `app.py`: FastAPI application code.
- `random_forest_model.pkl`: Trained Random Forest model (pickle file).
- `data/`: Data folder containing the dataset used for training and testing.

Running the FastAPI App:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Access the app at http://localhost:8000.

Making Predictions: Use the UI (or) Send POST requests to /predict with JSON data (example data)

- Some of the features are categorical, so they need to be encoded before making predictions.
  &nbsp;(such as amenities, time of day, day of week, month of year, building id, etc.)
- Would be made easier with further development of the app and a front-end interface.

0{
  "AMENITIES": 5192,
  "time_of_day": 16,
  "day_of_week": 3,
  "month_of_year": 5,
  "CAPACITY": 6,
  "BUILDINGID": B029,
}

## Interpreting the prediction

- Each prediction categorises the given test scenario into 3 groups based onbooking duration: a quick booking, 2-4 hour duration or 4+ hours, etc.
- Additionally each prediction corresponds to a count, and each count represents a time duration of 30 minutes.
