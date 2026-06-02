def classify_risk(score):
    if score < 40:
        return "LOW RISK"
    elif score < 70:
        return "MEDIUM RISK"
    else:
        return "HIGH RISK"


def climate_risk_report(flood_score, heatwave_score):
    """
    Returns full climate risk report
    """

    # ensure scores are 0–100
    flood_score = max(0, min(100, flood_score))
    heatwave_score = max(0, min(100, heatwave_score))

    # overall risk (weighted average)
    overall_score = (0.6 * flood_score) + (0.4 * heatwave_score)

    return {
        "Flood Risk Score": f"{round(flood_score, 2)}/100",
        "Heatwave Risk Score": f"{round(heatwave_score, 2)}/100",
        "Overall Climate Risk Score": f"{round(overall_score, 2)}/100",
        "Flood Risk Level": classify_risk(flood_score),
        "Heatwave Risk Level": classify_risk(heatwave_score),
        "Overall Climate Risk Level": classify_risk(overall_score)
    }