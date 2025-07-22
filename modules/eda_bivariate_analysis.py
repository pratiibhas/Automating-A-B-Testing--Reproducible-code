import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def bivariate_cat_cat(df, col1, col2):
    """
    Bivariate analysis between two categorical variables.
    Shows a crosstab and a stacked bar plot.
    """
    if not (df[col1].dtype == 'object' or pd.api.types.is_categorical_dtype(df[col1])):
        print(f"⚠️ '{col1}' is not categorical.")
        return
    if not (df[col2].dtype == 'object' or pd.api.types.is_categorical_dtype(df[col2])):
        print(f"⚠️ '{col2}' is not categorical.")
        return

    # Crosstab
    ct = pd.crosstab(df[col1], df[col2], normalize='index')
    print(f"\n🔢 Normalized Crosstab (% by {col1}):\n")
    print(ct.round(2))

    # Stacked bar plot
    ct.plot(kind='bar', stacked=True, figsize=(8, 4), colormap='viridis')
    plt.title(f"{col1} vs {col2} (Stacked %)")
    plt.ylabel("Proportion")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def bivariate_cat_num(df, cat_col, num_col):
    """
    Bivariate analysis between a categorical and a numeric variable.
    Shows boxplot and aggregated stats.
    """
    if not pd.api.types.is_numeric_dtype(df[num_col]):
        print(f"⚠️ '{num_col}' is not numeric.")
        return
    if not (df[cat_col].dtype == 'object' or pd.api.types.is_categorical_dtype(df[cat_col])):
        print(f"⚠️ '{cat_col}' is not categorical.")
        return

    # Aggregated statistics
    stats = df.groupby(cat_col)[num_col].describe().round(2)
    print(f"\n📊 Summary of '{num_col}' by '{cat_col}':\n")
    print(stats)

    # Boxplot
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=cat_col, y=num_col, data=df, palette="Set2")
    plt.title(f"{num_col} distribution by {cat_col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def bivariate_num_num(df, col1, col2):
    """
    Bivariate analysis between two numeric variables.
    Shows correlation and scatter plot.
    """
    if not pd.api.types.is_numeric_dtype(df[col1]):
        print(f"⚠️ '{col1}' is not numeric.")
        return
    if not pd.api.types.is_numeric_dtype(df[col2]):
        print(f"⚠️ '{col2}' is not numeric.")
        return

    # Correlation
    corr = df[[col1, col2]].corr().iloc[0, 1]
    print(f"\n🔗 Correlation between '{col1}' and '{col2}': {corr:.2f}")

    # Scatter plot
    plt.figure(figsize=(6, 5))
    sns.scatterplot(x=col1, y=col2, data=df, alpha=0.6)
    sns.regplot(x=col1, y=col2, data=df, scatter=False, color='red', line_kws={'linewidth': 1.5})
    plt.title(f"{col1} vs {col2} (Corr = {corr:.2f})")
    plt.tight_layout()
    plt.show()

def bivariate_analysis(df, col1, col2):
    if pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
        bivariate_num_num(df, col1, col2)
    elif pd.api.types.is_numeric_dtype(df[col1]) and not pd.api.types.is_numeric_dtype(df[col2]):
        bivariate_cat_num(df, col2, col1)
    elif not pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2]):
        bivariate_cat_num(df, col1, col2)
    else:
        bivariate_cat_cat(df, col1, col2)
