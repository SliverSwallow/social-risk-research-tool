# 🌍 Social Risk Assessment Tool

From framework → model → application

A practical tool to understand how social pressure affects trust, stability, and decision-making.

---

## 💡 What is this project?

This project helps analyze real-world social problems such as:

- High cost of living  
- Job instability  
- Low fertility and demographic pressure  
- Declining trust in society  

It shows how these factors interact and influence social stability.

The goal is simple:

> Help people better understand social risk and support more informed decisions.

---

## 🧠 Why this matters

In many societies today, people feel increasing pressure:

- Living costs are rising  
- Jobs are less stable  
- Long-term planning becomes difficult  

These pressures do not exist separately — they interact and affect:

- Trust between individuals  
- Trust in institutions  
- Social cooperation  

This project explores that connection.

---

## 🔍 What this tool does

The model estimates:

- **Structural risk**  
  (housing, labor, demographic pressure)

- **Adjusted risk**  
  (after welfare support)

- **Trust score**  
  (how stable coordination is)

- **Risk classification**  
  (low / medium / high)

- **Policy-relevant interpretation**

- **Automated PDF reports**

---

## ⚙️ How it works

The model follows a simple logic:


Structural strain
↓
Trust erosion
↓
Coordination breakdown
↓
System response (e.g., protest or instability)


---

### Core domains

- **Housing** → affordability pressure  
- **Labor** → income stability  
- **Demography** → long-term sustainability  
- **Welfare** → system buffering  

---

### Pipeline


Input indicators
↓
Structural strain calculation
↓
Welfare adjustment
↓
Trust estimation
↓
Risk classification
↓
Interpretation + report


---

## 🚀 Features

- FastAPI-based REST API  
- Modular analytical pipeline  
- Lightweight fuzzy-enhanced logic  
- Human-readable interpretation layer  
- Exportable PDF reports  
- Research-ready structure  

---

## 📊 Example usage

### Request

```json
POST /analyze
{
  "housing_cost_ratio": 0.6,
  "employment_stability": 0.5,
  "fertility_rate": 1.3,
  "welfare_level": 0.3
}
```

## 📦 Installation
```bash
git clone https://github.com/SliverSwallow/social-risk-research-tool.git
cd social-risk-research-tool
pip install -r requirements.txt
```

## ▶️ Run the API
```bash
uvicorn app.main:app --reload --port 8001
```
Open:
http://127.0.0.1:8001/docs


## 🔬 Research background

This tool is part of a broader research direction:

- Structural strain
- Trust as a coordination outcome
- System response under pressure

It serves as:

A computational illustration
A bridge between theory and application
A prototype decision-support tool

## 🎯 Intended use
Policy exploration
NGO decision support
Social risk screening
Academic prototyping

## ⚠️ Limitations
Conceptual model (not fully empirically calibrated)
Simplified relationships
Not designed for precise prediction
## 🧩 Future work
Empirical calibration
Time-series modeling
Agent-based extensions
Dashboard / UI
## 🌍 Real-world example

A small village (Arenillas) in Spain offers free housing and jobs to attract families and address population decline.

This policy directly reduces structural strain in:

housing
labor
demographic stability

It illustrates how coordinated intervention can restore trust and social functioning.

## 👤 Author

Nguyen Thai Binh (Silver Swallow)
Independent Researcher – Computational Social Systems

## ❤️ Support this work

If you find this project meaningful, you can support my research:

☕ Buy me a coffee: https://buymeacoffee.com/sliverswallow

Your support helps me continue developing tools and ideas for a more cooperative and stable society.

## 📜 License

MIT License

## ⭐ Citation

If you use this work:

Nguyen, T. B. (2026). Social Risk Assessment Tool. GitHub repository.
