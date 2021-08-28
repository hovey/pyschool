"""Test the efficiency of applying functions to list elements."""

import functools
import time


def timer(func):
    """Define a timer."""

    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        """Time the wrapped function."""
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        time_taken = toc - tic
        print(f"{func.__doc__} took {time_taken} seconds.")
        return value

    return timer_wrapper


@timer
def square_list_append():
    """Square list using a for loop."""
    tmp_list = range(10)
    squared_list = []
    for i in tmp_list:
        squared_list.append(i ** 2)
    return squared_list


@timer
def square_list_map():
    """Square list using map."""
    tmp_list = range(10)
    squared_list = list(map(lambda x: x ** 2, tmp_list))
    return squared_list


@timer
def square_list_comprehension_lambda():
    """Square list using list comprehension and lambda."""
    tmp_list = range(10)
    squared_list = [(lambda x: x ** 2)(i) for i in tmp_list]
    return squared_list


@timer
def square_list_alloc_append():
    """Square list using a preallocated append."""
    tmp_list = range(10)
    squared_list = []
    append_fn = squared_list.append

    for i in tmp_list:
        append_fn(i ** 2)

    return squared_list


@timer
def square_list_pure_comprehension():
    """Square list using pure list comprehension."""
    tmp_list = range(10)
    squared_list = [i ** 2 for i in tmp_list]
    return squared_list


@timer
def square_list_recursion():
    """Square list using recursion."""
    tmp_list = range(10)

    def list_square(lst):
        return [lst[0] ** 2] + list_square(lst[1:]) if lst else []

    squared_list = list_square(tmp_list)
    return squared_list


if __name__ == "__main__":
    v0 = square_list_append()
    v1 = square_list_map()
    v2 = square_list_comprehension_lambda()
    v3 = square_list_alloc_append()
    v4 = square_list_pure_comprehension()
    v5 = square_list_recursion()

    assert v0 == v1 == v2 == v3 == v4 == v5
