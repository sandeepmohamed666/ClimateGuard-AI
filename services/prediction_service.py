import os
import joblib
import numpy as np

# Load model
model_path = os.path.join(
    os.path.dirname(__file__),
    "..", "backend", "ml", "models", "climate_model.pkl"
)

model = joblib.load(model_path)


# -------------------------------
# LABEL MAPPING
# -------------------------------

RAINFALL_LABELS = {
    0: "Low Risk",
    1: "Medium Risk",
    2: "High Risk"
}

HEATWAVE_LABELS = {
    0: "Safe",
    1: "Warning",
    2: "Critical"
}


# -------------------------------
# PREDICTION FUNCTIONS
# -------------------------------

def predict_risk(data: list):
    """
    Generic risk prediction.
    data = [[feature1, feature2, ...]]
    """
    prediction = model.predict(np.array(data))
    return prediction.tolist()


def predict_rainfall_risk(data: list):
    """
    Predict rainfall risk using the trained model.
    Returns class predictions (0, 1, or 2).
    """
    prediction = model.predict(np.array(data))
    return prediction.tolist()


def predict_risk_heatwave(data: list):
    """
    Predict heatwave risk using the trained model.
    Returns class predictions (0, 1, or 2).
    """
    prediction = model.predict(np.array(data))
    return prediction.tolist()