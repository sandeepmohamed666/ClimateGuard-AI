from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.prediction_service import (
    predict_rainfall_risk,
    predict_risk_heatwave,
)

router = APIRouter()


# -----------------------------
# INPUT SCHEMA
# -----------------------------
class RainfallRequest(BaseModel):
    features: List[List[float]]


class HeatwaveRequest(BaseModel):
    features: List[List[float]]


# -----------------------------
# ENDPOINTS
# -----------------------------
@router.post("/rainfall/predict")
def predict_rainfall(req: RainfallRequest):
    try:
        result = predict_rainfall_risk(req.features)
        return {
            "status": "success",
            "prediction_type": "Rainfall Risk Prediction",
            "classes": ["Low Risk", "Medium Risk", "High Risk"],
            "prediction": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/heatwave/predict")
def predict_heatwave(req: HeatwaveRequest):
    try:
        result = predict_risk_heatwave(req.features)
        return {
            "status": "success",
            "prediction_type": "Heatwave Risk Prediction",
            "classes": ["Safe", "Warning", "Critical"],
            "prediction": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))