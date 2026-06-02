from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from services.prediction_service import predict_risk
from services.risk_service import classify_risk

router = APIRouter()


# -----------------------------
# INPUT SCHEMA
# -----------------------------
class RiskRequest(BaseModel):
    features: List[List[float]]


# -----------------------------
# OVERALL CLIMATE CLASSIFIER
# -----------------------------
def overall_risk_level(score: float):
    if score < 40:
        return "LOW RISK"
    elif score < 70:
        return "MEDIUM RISK"
    else:
        return "HIGH RISK"


# -----------------------------
# ENDPOINT
# -----------------------------
@router.post("/climate/risk")
def climate_risk(req: RiskRequest):

    try:
        preds = predict_risk(req.features)

        # -----------------------------
        # ASSUMPTION:
        # preds = [flood_score, heatwave_score]
        # -----------------------------
        flood_score = preds[0]
        heatwave_score = preds[1]

        # convert to 0–100 safely (if model returns 0–1)
        flood_score = float(flood_score) * 100
        heatwave_score = float(heatwave_score) * 100

        # overall score (weighted average)
        overall_score = (0.6 * flood_score) + (0.4 * heatwave_score)

        return {
            "status": "success",

            "Flood Risk Score": f"{round(flood_score, 2)}/100",
            "Heatwave Risk Score": f"{round(heatwave_score, 2)}/100",
            "Overall Climate Risk Score": f"{round(overall_score, 2)}/100",

            "Flood Risk Level": classify_risk(flood_score),
            "Heatwave Risk Level": classify_risk(heatwave_score),
            "Overall Climate Risk": overall_risk_level(overall_score)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))