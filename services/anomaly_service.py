from sklearn.ensemble import IsolationForest
import numpy as np

# simple anomaly model (you can improve later)
model = IsolationForest(contamination=0.1, random_state=42)

def detect_anomaly(data: list):
    prediction = model.fit_predict(np.array(data))

    # -1 = anomaly
    return ["ANOMALY" if p == -1 else "NORMAL" for p in prediction]
