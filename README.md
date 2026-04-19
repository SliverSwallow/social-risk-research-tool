# Social Risk Assessment Tool

## Overview

This project implements a simple model to assess social risk based on structural strain and welfare buffering.

It integrates:

* Housing cost pressure
* Employment stability
* Fertility rate
* Welfare level

## Features

* Risk score & trust estimation
* Interpretation layer
* Policy recommendations
* PDF report export

---

## Run the API

```bash
uvicorn app.main:app --reload --port 8001
```

Open:
http://127.0.0.1:8001/docs

---

## Example Input

```json
{
  "housing_cost_ratio": 0.6,
  "employment_stability": 0.5,
  "fertility_rate": 1.3,
  "welfare_level": 0.3
}
```

---

## Output

* Risk level
* Trust score
* Interpretation
* PDF report

---

## Status

MVP version
