# modules/eda_plot.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_cat_few_categories(df, columns, max_categories=20):
    """
    Plots bar plots for selected categorical columns.

    Parameters:
    - df: pandas DataFrame
    - columns: list of categorical columns to plot
    - max_categories: maximum number of unique values to plot per column
    """
    for col in columns:
        if col not in df.columns:
            print(f"⚠️ Column '{col}' not found in DataFrame.")
            continue

        unique_vals = df[col].nunique()
        if unique_vals > max_categories:
            print(f"⚠️ Skipping '{col}' – {unique_vals} unique values (too many).")
            continue

        plt.figure(figsize=(8, 4))
        sns.countplot(y=col, data=df, order=df[col].value_counts().index)
        plt.title(f"Distribution of {col}")
        plt.xlabel("Count")
        plt.ylabel(col)
        plt.tight_layout()
        plt.show()


def plot_categoricals_top_n(df, columns, top_n=10, min_unique=15):
    """
    Plots top N categories for each high-cardinality categorical column.
    
    Parameters:
    - df: pandas DataFrame
    - columns: list of categorical columns to plot
    - top_n: number of top categories to show
    - min_unique: only plot columns with more than this number of unique values
    """
    for col in columns:
        if col not in df.columns:
            print(f"⚠️ Column '{col}' not found.")
            continue

        unique_vals = df[col].nunique()
        
        # Skip low cardinality columns
        if unique_vals <= min_unique:
            print(f"ℹ️ Skipping '{col}' (only {unique_vals} unique values).")
            continue

        # Group all but top N categories into "Other"
        top_vals = df[col].value_counts().nlargest(top_n).index
        data_to_plot = df[col].apply(lambda x: x if x in top_vals else 'Other')

        plt.figure(figsize=(8, 4))
        sns.countplot(y=data_to_plot, order=data_to_plot.value_counts().index)
        plt.title(f"Top {top_n} Categories in '{col}'")
        plt.xlabel("Count")
        plt.ylabel(col)
        plt.tight_layout()
        plt.show()

def univariate_numeric_analysis(df, columns=None, bins=30):
    """
    Performs univariate analysis for numeric columns.
    
    Parameters:
    - df: pandas DataFrame
    - columns: list of numeric column names to analyze. If None, all numeric columns are used.
    - bins: number of bins to use in histograms.
    """
    if columns is None:
        columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    for col in columns:
        if col not in df.columns:
            print(f"⚠️ Column '{col}' not found in DataFrame.")
            continue
        if not pd.api.types.is_numeric_dtype(df[col]):
            print(f"⚠️ Column '{col}' is not numeric.")
            continue
        
        print(f"\n📊 Analysis for: {col}")
        print(df[col].describe(percentiles=[0.01, 0.25, 0.5, 0.75, 0.99]))
        print(f"Skewness: {df[col].skew():.2f}")
        print(f"Kurtosis: {df[col].kurt():.2f}")

        # Plotting
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        sns.histplot(df[col].dropna(), bins=bins, kde=True, ax=axs[0], color='skyblue')
        axs[0].set_title(f'Histogram + KDE: {col}')
        axs[0].set_xlabel(col)

        sns.boxplot(x=df[col], ax=axs[1], color='lightgreen')
        axs[1].set_title(f'Boxplot: {col}')
        axs[1].set_xlabel(col)

        plt.tight_layout()
        plt.show()        
