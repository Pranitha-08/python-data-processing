import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Read a CSV file and return it as a Pandas DataFrame.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"CSV file is empty: {file_path}")
