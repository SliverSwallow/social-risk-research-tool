from pydantic import BaseModel
from typing import List

class InputData(BaseModel):
    housing_cost_ratio: float        # 0 → 1 (vd: 0.5 = 50% income)
    employment_stability: float      # 0 → 1 (1 = very stable)
    fertility_rate: float            # vd: 1.2 → 2.1
    welfare_level: float             # 0 → 1 (NEW)

class OutputData(BaseModel):
    risk_score: float
    adjusted_risk: float
    trust_score: float
    risk_level: str
    key_issues: List[str]
    interpretation: str
    recommended_focus: List[str]