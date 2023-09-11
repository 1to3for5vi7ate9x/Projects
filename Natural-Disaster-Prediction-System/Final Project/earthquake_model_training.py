#Model training

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error



# Load the dataset for earthquake
df = pd.read_csv('earthquake_dataset.csv')

# Split the dataset into training and test sets
X = df[['Latitude', 'Longitude', 'Depth']]
y = df['Magnitude']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

mse
#print(mse)

# Save the trained model to a file
model_filename = 'earthquake_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

model_filename

