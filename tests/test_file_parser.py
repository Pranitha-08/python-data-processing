import pandas as pd
import pytest

from de_utils.file_parser import (
    read_csv,
    validate_columns,
    calculate_total_value,
    read_parquet,
    write_parquet,
)


def test_read_csv():
    df = read_csv("data/sample_orders.csv")

    assert not df.empty
    assert "order_id" in df.columns
    assert "customer_name" in df.columns


def test_validate_columns_success():
    df = pd.DataFrame(
        {
            "order_id": [1001],
            "quantity": [2],
            "price": [500],
        }
    )

    validate_columns(df, ["order_id", "quantity", "price"])


def test_validate_columns_missing_column():
    df = pd.DataFrame(
        {
            "order_id": [1001],
            "quantity": [2],
        }
    )

    with pytest.raises(ValueError):
        validate_columns(df, ["order_id", "quantity", "price"])


def test_calculate_total_value():
    df = pd.DataFrame(
        {
            "quantity": [2, 3],
            "price": [500, 100],
        }
    )

    result = calculate_total_value(df)

    assert result["total_value"].tolist() == [1000, 300]


def test_parquet_read_write(tmp_path):
    df = pd.DataFrame(
        {
            "order_id": [1001, 1002],
            "price": [500, 1000],
        }
    )

    parquet_file = tmp_path / "test_orders.parquet"

    write_parquet(df, parquet_file)
    result = read_parquet(parquet_file)

    assert result.equals(df)