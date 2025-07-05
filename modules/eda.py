import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(df, target_column=None, max_unique_for_categoricals=20, id_like_threshold=0.9):
    """
    Perform basic EDA and return two lists:
    - categorical columns
    - numerical columns (excluding ID-like)

    Parameters:
    - df: pandas DataFrame
    - target_column: optional, name of the target column for plotting
    - max_unique_for_categoricals: threshold to consider numeric columns as categoricals
    - id_like_threshold: threshold % of unique values to treat numeric column as ID-like
    """
    

    print("📊 Data Overview:")
    print(df.info())
    print("\n🧮 Summary Statistics:")
    print(df.describe(include='all'))
    print("\n🧱 Missing Values:")
    missing = df.isnull().sum()
    print(missing[missing > 0])

    # Detect numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Remove ID-like columns (very high cardinality)
    id_like_cols = [
        col for col in numeric_cols
        if df[col].nunique() / len(df) > id_like_threshold
    ]
    numeric_cols = [col for col in numeric_cols if col not in id_like_cols]
   
    # Detect categoricals
    object_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    low_cardinality_numeric = [
        col for col in df.select_dtypes(include=['int64', 'float64']).columns
        if df[col].nunique() <= max_unique_for_categoricals and col not in numeric_cols
    ]
    categorical_cols = object_cols + low_cardinality_numeric + id_like_cols
   
    # Remove duplicates
    categorical_cols = list(set(categorical_cols))
  

    print(f"\n🔢 Numerical columns (filtered): {numeric_cols}")
    print(f"🔤 Categorical columns (incl. ID-like): {categorical_cols}")

    return categorical_cols, numeric_cols
