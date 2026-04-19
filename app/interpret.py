def build_interpretation(risk_level, housing, labor, demo, welfare):
    issues = []

    if housing > 0.4:
        issues.append("affordability stress")

    if labor > 0.4:
        issues.append("livelihood insecurity")

    if demo > 0.4:
        issues.append("demographic vulnerability")

    if welfare < 0.4:
        issues.append("limited social protection")

    if risk_level == "high":
        message = "High social risk driven by combined structural pressures."
    elif risk_level == "medium":
        message = "Moderate structural pressure with potential instability."
    else:
        message = "Relatively stable conditions with manageable risk."

    return issues, message


def policy_recommendation(issues):
    mapping = {
        "affordability stress": "improve housing access",
        "livelihood insecurity": "enhance job stability",
        "demographic vulnerability": "support family formation",
        "limited social protection": "expand welfare support"
    }

    return [mapping[i] for i in issues if i in mapping]