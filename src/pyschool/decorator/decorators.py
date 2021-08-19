"""
This module demonstrates the use of decorators in Python3
"""

import time
import functools


def time_function(func):
    """
    This function wraps the decorator declaration and passes it the
    function to evaluate

    :param func: The function to time
    :type func: function

    :returns time_wrapper: The wrapped function
    """

    @functools.wraps(func)
    def time_wrapper(*args):
        """
        This function times how long it takes the passed function to
        run with the given arguments.

        :param args: The arguments to the function to time

        :returns result: The result of func(*args)
        """
        tic = time.time()
        result = func(*args)
        toc = time.time()

        print(f"{toc-tic} seconds for {args[1]}!")
        return result

    return time_wrapper


class Memoise(dict):
    """
    This class extends a python dictionary for memoisation
    """

    def __init__(self, func):
        """
        The init method of the Memoise class

        :param func: The function whose arguments and output to memoise
        :type func: function
        """
        self.func = func
        self.memo = {}

    @time_function
    def __call__(self, *args):
        """
        The call method of the Memoise class. Gets the dictionary entry
        associated with the key in args

        :param args: The ordered arguments to be fed to self.func

        :returns self[args]: The result of self.func(*args)
        """
        if not args in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]


@Memoise
def factorial(k):
    if k < 2:
        return 1
    return k * factorial(k - 1)


if __name__ == "__main__":
    val = 10

    print(
        f"\nThis script times how long it takes to run a recursive "
        + "function to calculate {val} factorial"
    )

    print(f"\nCalculating {val}! for the first time.")
    f1 = factorial(val)

    print(f"\nCalculating {val}! again. Should use the stored value.")
    f2 = factorial(val)
