def normalize_fertility(fertility_rate: float) -> float:
    # 2.1 = stable → 0 risk
    # 1.0 = high risk
    return max(0, min(1, (2.1 - fertility_rate) / 1.1))


def calculate_strain(housing, employment, fertility):
    housing_risk = housing
    labor_risk = 1 - employment
    demo_risk = normalize_fertility(fertility)

    # weighted average (simple MVP)
    strain = (housing_risk + labor_risk + demo_risk) / 3
    return strain, housing_risk, labor_risk, demo_risk


def apply_welfare(strain, welfare):
    # welfare = buffer
    adjusted = strain * (1 - welfare)
    return adjusted


def calculate_trust(adjusted_strain):
    return 1 - adjusted_strain


def classify_risk(score):
    if score > 0.7:
        return "high"
    elif score > 0.4:
        return "medium"
    else:
        return "low"