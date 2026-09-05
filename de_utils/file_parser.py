import pandas as pd


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Read a CSV file and return it as a Pandas DataFrame.
    """
    return pd.read_csv(file_path)
