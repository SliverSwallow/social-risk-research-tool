This repository provides a reference implementation of the coordination-based framework for structural strain, trust, and system response.

Related paper:
- Structural Strain, Trust Erosion, and System Response (Preprint)

Author: Nguyen Thai Binh (Silver Swallow)

# Social Risk Assessment Tool

A coordination-based analytical tool for evaluating structural social risk and trust dynamics under housing pressure, labor instability, demographic shifts, and welfare support.

---

## 📌 Overview

This project implements a **structural risk and trust framework** inspired by coordination-based state analysis.
Rather than treating trust as a psychological variable, the model interprets trust as an **emergent outcome of systemic strain and institutional buffering capacity**.

The tool provides:

* A quantitative **risk score**
* A **welfare-adjusted risk**
* A derived **trust indicator**
* Structured **interpretation and policy recommendations**
* Automatic **PDF report generation**

---

## 🧠 Conceptual Foundation

The model is grounded in the idea that:

> Social instability emerges when structural pressures exceed institutional buffering capacity.

Key dimensions:

* **Housing stress** → affordability pressure
* **Labor instability** → income uncertainty
* **Demographic strain** → fertility decline / aging risk
* **Welfare support** → system-level buffering mechanism

Trust is modeled as:

> A decreasing function of unmitigated structural strain.

---

## ⚙️ Model Pipeline

```
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
```

---

## 🚀 Features

* FastAPI-based REST API
* Modular analytical pipeline
* Lightweight fuzzy-enhanced logic (custom implementation)
* Human-readable interpretation layer
* Exportable PDF reports
* Research-ready structure

---

## 📦 Installation

```bash
git clone https://github.com/SilverSwallow/ngo-social-risk-tool.git
cd ngo-social-risk-tool
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn app.main:app --reload --port 8001
```

Open:

```
http://127.0.0.1:8001/docs
```

---

## 📊 Example Usage

### 1. Analyze Social Risk

**POST** `/analyze`

```json
{
  "housing_cost_ratio": 0.6,
  "employment_stability": 0.5,
  "fertility_rate": 1.3,
  "welfare_level": 0.3
}
```

**Response (example):**

```json
{
  "risk_score": 0.818,
  "adjusted_risk": 0.573,
  "trust_score": 0.427,
  "risk_level": "medium",
  "key_issues": [
    "affordability stress",
    "demographic vulnerability",
    "moderate social protection"
  ],
  "interpretation": "Moderate structural pressure persists despite partial welfare buffering, indicating potential instability if conditions worsen.",
  "recommended_focus": [
    "improve housing access",
    "support family formation"
  ]
}
```

---

### 2. Generate PDF Report

**POST** `/report/pdf`

Returns a downloadable structured report.

---

## 📁 Project Structure

```
ngo_social_risk_tool/
│
├── app/                # Core API and model logic
├── reports/            # PDF report generation
├── examples/           # Example inputs
├── outputs/            # Generated reports
├── README.md
└── requirements.txt
```

---

## 📄 Research Context

This tool supports the analytical framework developed in:

**"Trust and the Modern State: A Coordination-Based Framework for System Stability"**
(Preprint available on Zenodo)

The implementation serves as:

* A **computational illustration** of the framework
* A **policy exploration tool**
* A **bridge between theory and applied analysis**

---

## 🔬 Intended Use

* Policy exploration
* Social risk screening (NGO / research contexts)
* Academic prototyping
* Conceptual modeling of trust dynamics

---

## ⚠️ Limitations

* Not calibrated on real-world datasets (conceptual model)
* Simplified functional relationships
* Requires empirical validation for policy deployment

---

## 🧩 Future Work

* Empirical calibration with cross-country data
* Time-series dynamics
* Agent-based extensions
* Dashboard / frontend integration

---

## 👤 Author

**Silver Swallow**
Independent Researcher – Computational Social Systems

---

## 📜 License

(To be defined)

---

## ⭐ Citation (Suggested)

If you use this work:

```
Silver Swallow (2026). Social Risk Assessment Tool.
GitHub repository.
```
