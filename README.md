# 🧪 A/B Testing & Experimentation Framework 

## 📌 Overview

This project aims to build a **reusable, modular, and automated framework for A/B testing** using Python and real-world datasets. In any data-driven business — from e-commerce to travel to media — A/B testing is a critical tool for product and growth decisions.

Rather than treating every experiment as a one-off script, this project abstracts common components like data ingestion, preprocessing, feature typing, EDA, and statistical analysis into reusable modules.


---

## 🎯 Why This Project?

- ✅ A/B testing is essential but **repetitive**
- ⚠️ Most organizations have **scattered analysis code** for each experiment
- 📦 This framework aims to provide **clean, version-controlled, and reusable tools** for analysts and data scientists

---

## 🛠️ How Are We Doing This?

The project is structured as a **modular pipeline** to ensure each part of the experimentation lifecycle is cleanly separated and reusable:

### 🔄 Modular Components:

| Module                             | Purpose                                                       |
|----------------------              |---------------------------------------------------------------|
| `data_ingestion.py`                | Load data from CSV files or entire directories                |
| `feature_types.py` (optional)      | Automatically detect and classify categorical & numeric features |
| `eda_univariate_analysis.py`       | Perform modular, non-intrusive EDA (user-controlled plotting) |
| `eda_bivariate_analysis.py`        | Optional visualizations driven by selected columns            |
| `simulate_ab_test.py`              |  Statistical testing module (t-tests, uplift, etc.)  |
| `notebook.py`                      | Unified interface to run experiments end-to-end     |

---

## 📊 Current Experiment: Airbnb Listings

We're applying this framework to Airbnb data in Sicily, Italy to test the hypothesis:

> _Does a longer listing description lead to higher booking likelihood?_

We'll simulate A/B conditions, engineer derived features (e.g., `description_length`), and statistically evaluate outcomes.

---




```
AB-Testing-Framework/
│
├── data/                         # Raw input files (Airbnb listings, etc.)
├── notebooks/                    # Jupyter notebooks for interactive analysis
├── modules/                      # Modular Python components
│   ├── __init__.py
│   ├── data_ingestion.py
│   ├── eda.py
│   ├──eda_uniavariate_analysis.py
|   ├──eda_biavariate_analysis.py
│   └── simulation.py           
├── README.md                     # This file
└── requirements.txt              # (Coming soon)
```
