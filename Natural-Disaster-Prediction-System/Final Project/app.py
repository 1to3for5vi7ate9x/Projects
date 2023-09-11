from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)

# Load the trained model
with open('earthquake_model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('flood_model.pkl', 'rb') as file:  
    flood_model = pickle.load(file)

# Monthly heavy rainfall thresholds (based on the 90th percentile values we computed)
monthly_thresholds = {
    'JAN': 69.67, 'FEB': 73.60, 'MAR': 82.32, 'APR': 93.00, 'MAY': 134.50,
    'JUN': 272.60, 'JUL': 395.73, 'AUG': 363.41, 'SEP': 256.12, 'OCT': 160.40,
    'NOV': 103.36, 'DEC': 66.04
}


@app.route('/', methods=['GET', 'POST'])
def index():
    earthquake_prediction, flood_prediction, heavy_rainfall_prediction = None, None, None
    if request.method == 'POST':
            # Extract data from form
                latitude = float(request.form['latitude'])
                longitude = float(request.form['longitude'])
                depth = float(request.form['depth'])
            
            # Predict earthquake magnitude
                earthquake_prediction = model.predict([[latitude, longitude, depth]])[0]
            
            # Extract rainfall data
                monthly_rainfall = [
                    float(request.form[month]) for month in ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
            ]
            
            # Predict flood risk
                flood_prediction = flood_model.predict([monthly_rainfall])[0]
            
            # Predict heavy rainfall for the selected month and year
                selected_month = request.form['month']
                if float(request.form[selected_month]) > monthly_thresholds[selected_month]:
                    heavy_rainfall_prediction = "Yes"
                else:
                    heavy_rainfall_prediction = "No"
    return render_template('index.html', earthquake_prediction=earthquake_prediction, flood_prediction=flood_prediction, heavy_rainfall_prediction=heavy_rainfall_prediction)

if __name__ == '__main__':
    app.run(debug=True)

