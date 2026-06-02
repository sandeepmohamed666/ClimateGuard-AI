def explain_prediction(features, feature_names):
    """
    features = [values]
    feature_names = ["humidity", "temperature", "pressure", ...]
    """

    explanation = []

    for name, val in zip(feature_names, features):

        if name in ["humidity", "rainfall"]:
            direction = "↑ High" if val > 0.6 else "↓ Low"

        elif name in ["temperature"]:
            direction = "↑ High" if val > 35 else "↓ Normal"

        elif name in ["pressure"]:
            direction = "↓ Low (risk factor)" if val < 1005 else "↑ Normal"

        else:
            direction = "Normal"

        explanation.append({
            "feature": name,
            "value": float(val),
            "signal": direction
        })

    return explanation


def generate_ai_explanation(features, feature_names, prediction_label):
    """
    Generates human-readable explanation like ChatGPT style
    """

    humidity = None
    rainfall = None
    pressure = None
    temperature = None

    for name, val in zip(feature_names, features):
        if name == "humidity":
            humidity = val
        elif name == "rainfall":
            rainfall = val
        elif name == "pressure":
            pressure = val
        elif name == "temperature":
            temperature = val

    explanation = f"{prediction_label} risk is elevated because "

    reasons = []

    if rainfall and rainfall > 0.7:
        reasons.append("rainfall has increased continuously over the last few days")

    if pressure and pressure < 1005:
        reasons.append("atmospheric pressure is falling")

    if humidity and humidity > 0.7:
        reasons.append("humidity remains unusually high")

    if temperature and temperature > 35:
        reasons.append("temperature is above normal levels")

    if len(reasons) == 0:
        return f"{prediction_label} risk is normal with stable climate conditions."

    explanation += " while ".join(reasons) + "."

    return explanation