import time
from functools import wraps
import signal


def time_apply():

    def decorator(func):

        def wrapper(*args, **kwargs):
            start = time.time()
            _ = func(*args, **kwargs)
            row_apply_time = time.time() - start

            return row_apply_time

        return wraps(func)(wrapper)

    return decorator
