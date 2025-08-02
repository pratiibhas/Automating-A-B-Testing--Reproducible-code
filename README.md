# 🧪 A/B Testing & Experimentation Framework 

## 📌 Overview

This project aims to build a **reusable, modular, and automated framework for A/B testing** using Python and real-world datasets. In any data-driven business — from e-commerce to travel to media — A/B testing is a critical tool for product and growth decisions.

Rather than treating every experiment as a one-off script, this project abstracts common components like data ingestion, preprocessing, feature typing, EDA, and statistical analysis into reusable modules.


---

## 🎯 Why This Project?

- ✅ A/B testing is essential but **repetitive**
- ⚠️ Most organizations have **scattered analysis code** for each experiment
- 📦 This framework aims to provide **clean, version-controlled, and reusable tools** for analysts and data scientists
-  ✅ **Efficiency & Consistency**: A/B testing workflows are often repetitive; this framework standardizes them.
- 📦 **Reusability**: Provides clean, version-controlled tools for analysts and data scientists.

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


## 🎯 Why This Project?

* ✅ **Efficiency & Consistency**: A/B testing workflows are often repetitive; this framework standardizes them.
* ⚠️ **Maintainability**: Eliminates scattered, ad-hoc scripts within organizations.
* 📦 **Reusability**: Provides clean, version-controlled tools for analysts and data scientists.

---

## 🛠️ Architecture & Components

Each module is designed to handle a specific stage of the experimentation lifecycle. Modules live in the `modules/` directory:

| Module                        | Purpose                                                                          |
| ----------------------------- | -------------------------------------------------------------------------------- |
| `data_ingestion.py`           | Load data from CSV files or directories and perform initial cleaning.            |
| `feature_types.py` (optional) | Automatically detect and classify categorical and numeric features.              |
| `eda_univariate_analysis.py`  | Generate univariate visualizations and summary statistics.                       |
| `eda_bivariate_analysis.py`   | Create bivariate plots between features and target metrics.                      |
| `simulation.py`               | Simulate A/B experiments and implement statistical tests (Z-test, t-test, etc.). |
| `notebook.py`                 | Unified interface to run experiments end-to-end within Jupyter Notebooks.        |



---

## 🚀 Getting Started

1. **Clone the repo**:

   ```bash
   git clone https://github.com/yourusername/AB-Testing-Framework.git
   cd AB-Testing-Framework
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run an example notebook**:

   ```bash
   jupyter lab notebooks/airbnb_experiment.ipynb
   ```

---


Workflow:

1. Ingest raw listing data via `data_ingestion.py`.
2. Engineer `description_length` feature.
3. Split data into control (short descriptions) and treatment (long descriptions).
4. Simulate outcomes with `simulation.py` using a custom `booking_outcome` function.
5. Perform statistical tests and visualize results.

---

## 🔍 Choosing the Right Statistical Test

| Test                     | Use Case                                                        | Key Assumptions                                                                   |
| ------------------------ | --------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Z-Test (Proportions)** | Comparing two large-sample proportions (e.g., conversion rates) | Sample size > 30 per group, independent observations                              |
| **t-Test (Means)**       | Comparing means of continuous outcomes (e.g., revenue)          | Normal distribution or large samples, equal variances (if using Student’s t-test) |
| **Mann-Whitney U**       | Non-parametric alternative to t-test                            | Independent observations, ordinal or continuous data                              |
| **Chi-Square Test**      | Association between two categorical variables                   | Expected frequency ≥5 in each cell                                                |
| **Fisher’s Exact**       | Proportions with small samples                                  | None (exact test)                                                                 |

> **In our Airbnb example**, we used a **Z-test** for comparing the booking proportions because:
>
> * Our simulated control and treatment groups each contain **several hundred** listings.
> * We are comparing **binary outcomes** (booked vs. not booked).

---

## 📈 Interpreting Results

* **Effect Size**: Absolute difference and relative lift between treatment and control.
* **P-Value**: Statistical significance of the observed difference.


---

## 🤝 Contributing

Contributions are welcome! To propose a feature or bug fix:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and push to your fork.
4. Open a Pull Request detailing your improvements.


---

**Happy Experimenting!** 🎉

