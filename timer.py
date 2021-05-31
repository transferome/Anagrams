"""  Module  """
import functools
import time


def timer(func):
    """Print the runtime of a decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        """Wrapper for """
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


if __name__ == '__main__':
    pass
