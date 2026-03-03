def evaluate_rules(user, tasks):
    risk_score = 0
    explanation = []

    # Rule 1: Close deadline + large task
    for task in tasks:
        if task["deadline_days"] <= 3 and task["estimated_hours"] >= 4:
            risk_score += 1
            explanation.append("High workload close to deadline.")

    # Rule 2: Low confidence
    if user["confidence"] <= 2:
        risk_score += 1
        explanation.append("Low confidence level.")

    # Rule 3: High stress
    if user["stress"] >= 4:
        risk_score += 1
        explanation.append("High stress level.")

    # Rule 4: Low attendance
    if user["attendance_rate"] <= 0.6:
        risk_score += 1
        explanation.append("Low attendance rate.")

    # Determine risk level
    if risk_score <= 1:
        risk_level = "Low"
    elif risk_score == 2:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return risk_level, explanation