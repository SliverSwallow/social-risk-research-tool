# Social Risk Assessment Tool

From framework → model → application

A coordination-based analytical tool for evaluating structural social risk and trust dynamics.

---

## 🔍 Overview

This repository provides a reference implementation of a coordination-based framework for **structural strain, trust erosion, and system response**.

Rather than treating trust as a psychological or cultural variable, this model interprets trust as an **emergent outcome of coordination under structural constraints**.

The tool translates theoretical insights into a computational pipeline, enabling structured analysis of social instability.

---

## 📄 Related Research

- *Structural Strain, Trust Erosion, and System Response* (Preprint)
- *Trust and the Modern State: A Coordination-Based Framework for System Stability*

---

## ⚙️ What this tool does

The model estimates:

- **Structural risk** (housing, labor, demographic pressure)
- **Adjusted risk** (after welfare buffering)
- **Trust score** (proxy for coordination effectiveness)
- **Risk classification and interpretation**
- **Policy-relevant insights**
- **Automated PDF reports**

---

## 🧠 Conceptual Foundation

The framework is based on a simple structural mechanism:


Structural strain
→ trust erosion
→ coordination breakdown
→ system response (protest / conflict)


Key domains:

- **Housing** → affordability constraints  
- **Labor** → income stability  
- **Demography** → system reproduction  
- **Welfare** → institutional buffering  

Trust is modeled as:

> A decreasing function of unmitigated structural strain.

---

## ⚙️ Model Pipeline


Input Indicators
↓
Structural Strain Calculation
↓
Welfare Adjustment
↓
Trust Estimation
↓
Risk Classification
↓
Interpretation + Policy Output
↓
PDF Report


---

## 🚀 Features

- FastAPI-based REST API  
- Modular analytical pipeline  
- Lightweight fuzzy-enhanced logic  
- Human-readable interpretation layer  
- Exportable PDF reports  
- Research-ready architecture  

---

## 📦 Installation

```bash
git clone https://github.com/SliverSwallow/social-risk-research-tool.git
cd social-risk-research-tool
pip install -r requirements.txt
▶️ Run the API
uvicorn app.main:app --reload --port 8001

Open:

http://127.0.0.1:8001/docs
📊 Example Usage
POST /analyze
{
  "housing_cost_ratio": 0.6,
  "employment_stability": 0.5,
  "fertility_rate": 1.3,
  "welfare_level": 0.3
}
📁 Project Structure
social-risk-research-tool/
├── app/
├── reports/
├── examples/
├── outputs/
├── README.md
└── requirements.txt
🔬 Research Context

This tool operationalizes a broader research program:

Paper 1 → Structural strain
Paper 2 → Trust as coordination outcome
Paper 3 → System response (protest / conflict)

It serves as:

A computational illustration
A bridge between theory and application
A prototype decision-support tool
🎯 Intended Use
Policy exploration
NGO decision support
Social risk screening
Academic prototyping
⚠️ Limitations
Conceptual model (not empirically calibrated)
Simplified relationships
Not designed for predictive accuracy
🧩 Future Work
Empirical calibration
Time-series modeling
Agent-based extensions
Dashboard / UI integration
👤 Author

Nguyen Thai Binh (Silver Swallow)
Independent Researcher – Computational Social Systems

📜 License

MIT License

⭐ Citation

If you use this work:

Nguyen, T. B. (2026). Social Risk Assessment Tool. GitHub repository.
