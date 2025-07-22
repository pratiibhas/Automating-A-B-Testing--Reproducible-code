import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

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

