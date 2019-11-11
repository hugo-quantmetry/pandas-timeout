# -*- coding: utf-8 -*-

"""Main module."""

import time

import pandas as pd

from timeout.timeout_decorator import timeout
from timeout.time_decorator import time_apply


#@timeout(1.5, raise_error=True)
@timeout(1, replace_value='TimeOut')
def sleep_and_triple(row):
    number_ = row['number']

    time.sleep(number_)

    return number_ * 3


@timeout(1.5, raise_error=True)
def sleep_and_double(number_):
    time.sleep(number_)

    return number_ * 2


@time_apply()
def sleep_and_halve(row):
    number_ = row['number']

    time.sleep(number_)

    return number_ * 0.5


def run_timeout():
    df = pd.DataFrame({'number': [1, 0.5, 0.2, 2, 0.3]}, index=[0, 2, 4, 6, 8])

    df['result'] = df.apply(sleep_and_halve, axis=1)
    # df['result'] = df['number'].apply(sleep_and_double)
    # df['result'] = df.apply(sleep_and_triple, axis=1)

    print(df)


if __name__ == '__main__':
    run_timeout()
