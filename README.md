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

Making Predictions: Send POST requests to /predict with JSON data (example data)
```bash
{
  "AMENITIES": 119.0,
  "time_of_day": 16.0,
  "day_of_week": 3.0,
  "month_of_year": 5.0,
  "CAPACITY": 6.0,
  "BUILDINGID": 23.0,
  "Total_Building_Meetings": 9933.0
}
```

## Interpreting the prediction
- Each prediction corresponds to a count, and each count represents a time duration of 30 minutes.




