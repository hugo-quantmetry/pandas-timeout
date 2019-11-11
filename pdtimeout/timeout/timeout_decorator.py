from functools import wraps
import signal

# from timeout.timeout_error import TimeoutError


def timeout(decorator_timeout=0.5, replace_value=None, raise_error=True, error_message='Time expired'):

    def decorator(func):

        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):

            timeout_in_seconds = decorator_timeout

            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, timeout_in_seconds)

            try:
                result = func(*args, **kwargs)
            except TimeoutError:
                if raise_error:
                    if hasattr(args[0], "name"):
                        raise TimeoutError(f"{error_message}. Index = {args[0].name}")
                    else:
                        raise TimeoutError(f"{error_message}.")

                result = replace_value

            finally:
                signal.alarm(0)

            return result

        return wraps(func)(wrapper)

    return decorator