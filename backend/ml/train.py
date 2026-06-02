from pathlib import Path
import sys

# Add project root to sys.path
root_path = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(root_path))

import pandas as pd
from backend.preprocessing.cleaning import clean_data
from backend.preprocessing.feature_engineering import create_features

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# load data
train_df = pd.read_csv(root_path / "datasets/raw/DailyDelhiClimateTrain.csv")

# In this dataset, we predict 'meantemp'
target_col = "meantemp"

# preprocess
train_df = clean_data(train_df)
train_df = create_features(train_df)

# split
X = train_df.drop([target_col, "date"], axis=1)
y = train_df[target_col]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# model
model = RandomForestRegressor()  # Changed to Regressor for temperature prediction
model.fit(X_train, y_train)

# Save model
model_path = Path(__file__).parent / "models" / "climate_model.pkl"
joblib.dump(model, model_path)

print("Model trained successfully.")