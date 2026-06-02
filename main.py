from pathlib import Path
import sys

# Add project root to sys.path for imports
sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI

from api.prediction_routes import router as prediction_router
from api.risk_routes import router as risk_router
from api.anomaly_routes import router as anomaly_router

app = FastAPI(title="Climate Guard AI")

@app.get("/")
def root():
    return {
        "message": "Welcome to Climate Guard AI API",
        "endpoints": {
            "predict": "POST /predict - Predict climate risk",
            "risk": "POST /risk - Classify risk levels",
            "anomaly": "POST /anomaly - Detect anomalies"
        }
    }

app.include_router(prediction_router)
app.include_router(risk_router)
app.include_router(anomaly_router)