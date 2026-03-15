def get_fraud_explanation(transaction):

    reasons = []

    if transaction["amount"] > 10000:
        reasons.append("High transaction amount")

    if transaction["hour"] < 5:
        reasons.append("Unusual time of transaction")

    if transaction["risk_score"] > 0.7:
        reasons.append("High model fraud probability")

    if len(reasons) == 0:
        reasons.append("Normal transaction behaviour")

    return reasons