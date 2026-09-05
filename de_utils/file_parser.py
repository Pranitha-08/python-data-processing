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


def validate_columns(df: pd.DataFrame, required_columns: list[str]) -> None:
    """
    Validate that all required columns are present in the DataFrame.
    """
    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )