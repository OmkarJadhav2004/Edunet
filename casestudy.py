#Air Quality Index in Urban Area
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('air_quality_data.csv')

# Ensure correct column names
df.rename(columns={"Wind Speed": "Wind_Speed", "Traffic Volume": "Traffic"}, inplace=True)

# Check if AQI exists; if not, calculate using a simplified formula (example)
if 'AQI' not in df.columns:
    df['AQI'] = (df['PM2.5'] * 0.5 + df['PM10'] * 0.3 + df['NO2'] * 0.2).astype(int)

# Handle missing values
df.dropna(inplace=True)

# Feature selection
features = ['PM2.5', 'PM10', 'NO2', 'CO', 'Temperature', 'Humidity', 'Wind_Speed', 'Traffic']
target = 'AQI'

# Splitting data
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict AQI
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f"MAE: {mae:.2f}, MSE: {mse:.2f}, R² Score: {r2:.2f}")

# Print actual vs predicted AQI values (first 10)
output_df = pd.DataFrame({"Actual AQI": y_test.values, "Predicted AQI": y_pred.astype(int)})
print("\nSample AQI Predictions:")
print(output_df.head(10))
