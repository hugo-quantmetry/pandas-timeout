import time
import pandas as pd

from pdtimeout.timeout.timeout_decorator import timeout


def test_raise_timeout():
    
    @timeout(1.5, raise_error=True)
    def sleep_and_triple(row):
        number_ = row['number']

        time.sleep(number_)

        return number_ * 3
    
    df = pd.DataFrame({'number': [1, 0.5, 0.2, 2, 0.3]}, index=[0, 2, 4, 6, 8])
    error_index = 6

    try:
        df.apply(sleep_and_triple, axis=1)
    except TimeoutError as e:
        assert (e.args[1] == f"occurred at index {error_index}")
    else:
        print("A TimeOut error should have occured")
        assert False


def test_replace_value():
    df = pd.DataFrame({'number': [1, 0.5, 0.2, 2, 0.3]}, index=[0, 2, 4, 6, 8])
    
    expected_result = pd.Series(["TimeOut", 1.5, 0.6, "TimeOut", 0.9], index=[0, 2, 4, 6, 8])

    @timeout(0.9, replace_value="TimeOut")
    def sleep_and_triple(row):
        number_ = row['number']

        time.sleep(number_)

        return number_ * 3

    result = df.apply(sleep_and_triple, axis=1)

    pd.testing.assert_series_equal(result, expected_result)
