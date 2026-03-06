"""Risk scoring helpers."""


def probability_to_risk_score(probability: float) -> int:
    """Convert churn probability in [0,1] to a 0-100 integer score."""
    return int(round(probability * 100))


def risk_category_from_score(score: int) -> str:
    """Map risk score to Low/Medium/High buckets."""
    if score <= 30:
        return "Low Risk"
    if score <= 70:
        return "Medium Risk"
    return "High Risk"
