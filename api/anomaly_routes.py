from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from services.anomaly_service import detect_anomaly

router = APIRouter()


# -----------------------------
# INPUT SCHEMA
# -----------------------------
class AnomalyInput(BaseModel):
    features: List[float]

@router.post("/anomaly")
def anomaly(payload: AnomalyInput):
    result = detect_anomaly(payload.features)
    return {
        "status": "success",
        "anomaly_summary": {
            "temperature": "Abnormal" if "Temperature" in result else "Normal",
            "rainfall": "Abnormal" if "Rainfall" in result else "Normal",
            "humidity": "Abnormal" if "Humidity" in result else "Normal",
        },
        "raw_output": result,
    }