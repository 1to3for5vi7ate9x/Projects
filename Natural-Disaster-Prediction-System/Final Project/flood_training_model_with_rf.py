import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load the rainfall dataset again
rainfall_df = pd.read_csv('rainfall_improved_dataset.csv')

# Calculate the 90th percentile for the JJAS rainfall data
threshold =  rainfall_df['JJAS'].quantile(0.90)

# Create a binary flood risk variable
rainfall_df['Flood_Risk'] = rainfall_df['JJAS'].apply(lambda x: 1 if x > threshold else 0)

# Display the last few rows of the updated dataset
#print(rainfall_df.tail())
#rainfall_df.tail()

data_for_training = rainfall_df[~rainfall_df['Parameter'].isin(["Mean", "Standard deviation", "Coefficient of variation"])]

X_rain = data_for_training[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].fillna(0)
y_rain = data_for_training['Flood_Risk']
# Split the dataset into training and test sets
X_train_rain, X_test_rain, y_train_rain, y_test_rain = train_test_split(X_rain, y_rain, test_size=0.2, random_state=42)

# Train a random forest classifier
flood_model = RandomForestClassifier(n_estimators=100, random_state=42)
flood_model.fit(X_train_rain, y_train_rain)

# Predict on the test set
y_pred_rain = flood_model.predict(X_test_rain)

# Calculate the accuracy
accuracy = accuracy_score(y_test_rain, y_pred_rain)

#print(accuracy)
accuracy

# Calculate the 90th percentile for each month in the dataset
monthly_thresholds = rainfall_df[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].quantile(0.90)

monthly_thresholds

#Heavy rainfall thresholds (90th percentile values) for each month:
'''\[
\begin{{align*}}
\text{{JAN}} & : 69.67 \text{{ mm}} \\
\text{{FEB}} & : 73.60 \text{{ mm}} \\
\text{{MAR}} & : 82.32 \text{{ mm}} \\
\text{{APR}} & : 93.00 \text{{ mm}} \\
\text{{MAY}} & : 134.50 \text{{ mm}} \\
\text{{JUN}} & : 272.60 \text{{ mm}} \\
\text{{JUL}} & : 395.73 \text{{ mm}} \\
\text{{AUG}} & : 363.41 \text{{ mm}} \\
\text{{SEP}} & : 256.12 \text{{ mm}} \\
\text{{OCT}} & : 160.40 \text{{ mm}} \\
\text{{NOV}} & : 103.36 \text{{ mm}} \\
\text{{DEC}} & : 66.04 \text{{ mm}} \\
\end{{align*}}
\]'''

# Save the trained model to a file
model_filename = 'flood_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(flood_model, file)

model_filename





