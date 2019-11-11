import time
import pandas as pd

from timeout.time_decorator import time_apply


def test_time_apply():
    df = pd.DataFrame({'number': [1, 0.5, 0.2, 2, 0.3]}, index=[0, 2, 4, 6, 8])
    expected_result = pd.Series([1, 0.5, 0.2, 2, 0.3], index=[0, 2, 4, 6, 8])

    @time_apply()
    def sleep_and_triple(row):
        number_ = row['number']

        time.sleep(number_)

        return number_ * 3

    result = df.apply(sleep_and_triple, axis=1)

    # Compare number with low precision (an exact match is not expected)
    pd.testing.assert_series_equal(result, expected_result, check_less_precise=1)
