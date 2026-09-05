from de_utils.file_parser import read_csv


def test_read_csv():
    df = read_csv("data/sample_orders.csv")

    assert not df.empty
    assert "order_id" in df.columns
    assert "customer_name" in df.columns
