from pathlib import Path


def file_exists(file_path: str) -> bool:
    """
    Check whether a file exists.
    """
    return Path(file_path).is_file()
