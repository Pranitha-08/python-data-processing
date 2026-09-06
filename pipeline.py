from de_utils import (
    read_csv,
    validate_columns,
    calculate_total_value,
    get_logger,
    PipelineSession,
)


logger = get_logger("orders_pipeline")


def run_pipeline():
    session = PipelineSession("orders_pipeline")
    session.start()

    try:
        # Extract
        logger.info("Reading source data")
        df = read_csv("data/sample_orders.csv")

        # Validate
        logger.info("Validating columns")
        validate_columns(
            df,
            [
                "order_id",
                "customer_name",
                "product",
                "quantity",
                "price",
                "order_date",
            ],
        )

        # Transform
        logger.info("Calculating total order value")
        df = calculate_total_value(df)

        # Load
        logger.info("Saving processed data")
        df.to_csv("data/processed_orders.csv", index=False)

        logger.info("Pipeline completed successfully")
        print(df)

    except Exception:
        logger.exception("Pipeline failed")
        raise

    finally:
        session.end()


if __name__ == "__main__":
    run_pipeline()