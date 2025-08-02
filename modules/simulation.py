import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from scipy.stats import norm
from statsmodels.stats.proportion import proportions_ztest

def generate_synthetic_data_from(df, n_samples=1000, seed=42):
    np.random.seed(seed)
    synthetic = pd.DataFrame()

    for col in df.columns:
        non_null = df[col].dropna()
        if non_null.empty:
            print(f"⚠️ Skipping column '{col}' — no valid data.")
            continue

        if pd.api.types.is_numeric_dtype(df[col]):
            if df[col].nunique() < 20:
                synthetic[col] = np.random.choice(non_null.unique(), size=n_samples)
            else:
                synthetic[col] = np.random.normal(loc=non_null.mean(), scale=non_null.std(), size=n_samples)
        elif pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col]):
            synthetic[col] = np.random.choice(non_null.unique(), size=n_samples)
        else:
            print(f"⚠️ Skipping unsupported column '{col}' with dtype {df[col].dtype}") 
            # since there may be empty columns are present
            continue

    return synthetic


def simulate_ab_test(
    df,
    treatment_col: str,
    treatment_func,
    outcome_func,
    test_size=0.5,
    seed=42,
    show_plot=True
):
    """
    Simulates an A/B test on given data with Z-test for proportions.
    """

    np.random.seed(seed)
    df = df.copy()

    # Assign groups randomly
    df['group'] = np.random.choice(['control', 'treatment'], size=len(df), p=[1 - test_size, test_size])

    # Apply treatment logic (e.g., description_len changes)
    df[treatment_col] = df['group'].apply(treatment_func)

    # Simulate outcomes using user-defined function
    df['outcome'] = df.apply(outcome_func, axis=1).astype(int)

    # Group-wise conversion rates
    group_means = df.groupby('group')['outcome'].mean()
    print("\n📊 Outcome Rate by Group:")
    print(group_means)

    # Z-test for proportions
    control_success = df[df['group'] == 'control']['outcome'].sum()
    treatment_success = df[df['group'] == 'treatment']['outcome'].sum()
    control_n = (df['group'] == 'control').sum()
    treatment_n = (df['group'] == 'treatment').sum()

    counts = np.array([treatment_success, control_success])
    nobs = np.array([treatment_n, control_n])

    z_stat, p_value = proportions_ztest(count=counts, nobs=nobs)

    print("\n🔍 Z-Test Results:")
    print(f"Z-statistic: {z_stat:.4f}")
    print(f"P-value:     {p_value:.4f}")

    if p_value < 0.05:
        print("✅ Statistically significant difference between groups.")
    else:
        print("❌ No statistically significant difference between groups.")

    # Optional visualization
    if show_plot:
        sns.barplot(data=df, x='group', y='outcome')
        plt.title("Outcome Rate by Group")
        plt.ylabel("Booking Conversion Rate")
        plt.show()

    return df


def simulate_ab_test_logistics(
    df,
    treatment_col: str,
    treatment_func,
    outcome_func,
    test_size=0.5,
    seed=42,
    show_plot=True
):
    """
    Simulates an A/B test on given data.
    """

    np.random.seed(seed)
    df = df.copy()

    # Assign groups
    df['group'] = np.random.choice(['control', 'treatment'], size=len(df), p=[1 - test_size, test_size])

    # Apply treatment logic
    df[treatment_col] = df['group'].apply(treatment_func)

    # Simulate outcome
    df['outcome'] = df.apply(outcome_func, axis=1).astype(int)

    # Group-level conversion rates
    print("\n📊 Outcome Rate by Group:")
    print(df.groupby('group')['outcome'].mean())

    # Logistic Regression
    feature_cols = [col for col in df.columns if col not in ['group', 'outcome']]
    X = pd.get_dummies(df[feature_cols], drop_first=True)
    y = df['outcome']

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    print("\n📈 Logistic Regression Coefficients:")
    for name, coef in zip(X.columns, model.coef_[0]):
        print(f"{name}: {coef:.4f}")

    if show_plot:
        sns.barplot(data=df, x='group', y='outcome')
        plt.title("Outcome Rate by Group")
        plt.ylabel("Conversion Rate")
        plt.show()

    return df

