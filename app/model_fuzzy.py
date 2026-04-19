# model_fuzzy.py

# =========================
# 1. FUZZY MEMBERSHIP
# =========================

def housing_stress(h):
    """
    h: housing cost ratio (0–1)
    """
    if h <= 0.3:
        return 0.0
    elif h >= 0.6:
        return 1.0
    else:
        return (h - 0.3) / (0.6 - 0.3)


def labor_risk(e):
    """
    e: employment stability (0–1)
    """
    return 1.0 - e


def demographic_risk(f):
    """
    f: fertility rate
    """
    if f >= 2.1:
        return 0.0
    elif f <= 1.0:
        return 1.0
    else:
        return (2.1 - f) / (2.1 - 1.0)


# =========================
# 2. FUZZY AGGREGATION
# =========================

def calculate_strain(housing, employment, fertility):
    h_r = housing_stress(housing)
    l_r = labor_risk(employment)
    d_r = demographic_risk(fertility)

    # weighted base
    strain = 0.4 * h_r + 0.3 * l_r + 0.3 * d_r

    # interaction effect (cross-domain strain)
    interaction = h_r * l_r
    strain += 0.1 * interaction

    # clamp 0–1
    strain = max(0, min(1, strain))

    return strain, h_r, l_r, d_r


# =========================
# 3. WELFARE BUFFER
# =========================

def apply_welfare(strain, welfare):
    """
    welfare: 0–1 (buffer strength)
    """
    adjusted = strain * (1 - welfare)
    return max(0, min(1, adjusted))


# =========================
# 4. TRUST FUNCTION
# =========================

def calculate_trust(adjusted_strain):
    return 1.0 - adjusted_strain


# =========================
# 5. CLASSIFICATION
# =========================

def classify_risk(score):
    if score > 0.65:
        return "high"
    elif score > 0.35:
        return "medium"
    else:
        return "low"


# =========================
# 6. INTERPRETATION SUPPORT
# =========================

def extract_issues(h_r, l_r, d_r, welfare):
    issues = []

    if h_r > 0.5:
        issues.append("affordability stress")

    if l_r > 0.5:
        issues.append("livelihood insecurity")

    if d_r > 0.5:
        issues.append("demographic vulnerability")

    # welfare grading (fuzzy style)
    if welfare < 0.3:
        issues.append("weak social protection")
    elif welfare < 0.6:
        issues.append("moderate social protection")

    return issues


# =========================
# 7. POLICY MAPPING
# =========================

def policy_recommendation(issues):
    priority = []

    if "affordability stress" in issues:
        priority.append("improve housing access")

    if "livelihood insecurity" in issues:
        priority.append("enhance job stability")

    if "demographic vulnerability" in issues:
        priority.append("support family formation")

    if "weak social protection" in issues:
        priority.append("expand welfare system")

    return priority


# =========================
# 8. FULL PIPELINE (OPTIONAL)
# =========================

def run_model(housing, employment, fertility, welfare):
    strain, h_r, l_r, d_r = calculate_strain(housing, employment, fertility)
    adjusted = apply_welfare(strain, welfare)
    trust = calculate_trust(adjusted)
    risk_level = classify_risk(adjusted)

    issues = extract_issues(h_r, l_r, d_r, welfare)
    recommendations = policy_recommendation(issues)
    if risk_level == "high":
        interpretation = "High social risk driven by structural pressures."
    elif risk_level == "medium":
        interpretation = "Moderate structural pressure persists despite partial welfare buffering, indicating potential instability if conditions worsen."
    else:
        interpretation = "Relatively stable conditions."

    return {
        "risk_score": round(strain, 3),
        "adjusted_risk": round(adjusted, 3),
        "trust_score": round(trust, 3),
        "risk_level": risk_level,
        "key_issues": issues,
        "interpretation": interpretation,  # 🔥 THIS LINE
        "recommended_focus": recommendations
    }