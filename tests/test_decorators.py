from de_utils.decorators import measure_time


@measure_time
def sample_function():
    return "success"


def test_measure_time():
    result = sample_function()

    assert result == "success"
