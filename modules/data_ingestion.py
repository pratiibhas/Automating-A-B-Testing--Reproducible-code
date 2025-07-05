# data_ingestion/ingestion.py

import os
import pandas as pd

class DataIngestion:
    def __init__(self, path: str):
        self.path = path

    def _read_file(self, filepath: str) -> pd.DataFrame:
        ext = os.path.splitext(filepath)[-1].lower()
        try:
            if ext == '.csv':
                return pd.read_csv(filepath)
            elif ext in ['.xls', '.xlsx']:
                return pd.read_excel(filepath)
            else:
                raise ValueError(f"Unsupported file format: {ext}")
        except Exception as e:
            raise RuntimeError(f"Error reading {filepath}: {e}")

    def load(self) -> pd.DataFrame | dict[str, pd.DataFrame]:
        if os.path.isfile(self.path):
            return self._read_file(self.path)

        elif os.path.isdir(self.path):
            dataframes = {}
            for filename in os.listdir(self.path):
                full_path = os.path.join(self.path, filename)
                if os.path.isfile(full_path) and os.path.splitext(filename)[-1].lower() in ['.csv', '.xls', '.xlsx']:
                    try:
                        dataframes[filename] = self._read_file(full_path)
                    except Exception as e:
                        print(f"Skipping {filename}: {e}")
            return dataframes
        else:
            raise FileNotFoundError(f"Path not found: {self.path}")
