# gen.py

# Reference, Generators in Python, Real Python 18 Jun 2020
# https://youtu.be/1t_NUJFh33Y


def f01():
    # a finite sequence with a generator
    numbers = [1, 2, 3]
    for n in numbers:
        yield n


"""Example
$ conda activate pyschool-env
$ cd src/pyschool/pattern
$ python
> import generators as gen
> g = gen.f01()
> type(g)  # returns <type 'generator'>
> next(g)  # returns 1
> next(g)  # returns 2
> next(g)  # returns 3
> next(g)  # returns StopIteration error, raised when Iterators are exhausted
"""


class f02:
    def __init__(self, *, size: int = 5):

        # create the comprehensions
        self.list_comp = [
            n ** 2 for n in range(size)
        ]  # list comprehension, uses square brackets [ ]

        self.gen_comp = (
            n ** 2 for n in range(size)
        )  # generator comprehension, uses parentheses ( )


"""Example
> f = gen.f02()
> type(f)  # returns <class 'generators.f02'>
> f.list_comp  # returns [0, 1, 4, 9, 16]
> f.gen_comp  # returns <generator object f02.__init__.<locals>.<genexpr> at 0x7fc757286480>

compare memory stores of list comprehension versus generator comprehension
> import sys
> big_num = 100000
> h = gen.f02(size=big_num)
> sys.getsizeof(h.list_comp)  # returns 824464 (over 824000 bytes for list comprehension)
> sys.getsizeof(h.gen_comp)  # returns 112 (just 112 bytes for generator comprehension)

compare speed of list comprehension versus generator comprehension
> import cProfile as cp
> cp.run('sum([n ** 2 for n in range(100000)])')
         5 function calls in 0.038 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.036    0.036    0.036    0.036 <string>:1(<listcomp>)
        1    0.001    0.001    0.038    0.038 <string>:1(<module>)
        1    0.000    0.000    0.038    0.038 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


> cp.run('sum((n ** 2 for n in range(100000)))')
         100005 function calls in 0.049 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   100001    0.039    0.000    0.039    0.000 <string>:1(<genexpr>)
        1    0.000    0.000    0.049    0.049 <string>:1(<module>)
        1    0.000    0.000    0.049    0.049 {built-in method builtins.exec}
        1    0.010    0.010    0.049    0.049 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

So the list comprehension took 38 ms to run, whereas the generator comprehension
took 49 ms to run.

Summary: There is a tradeoff in terms of memory versus speed.
Relative to the list comprehension, the generator comprehension:
* takes less memory, but
* requires a longer run time.
"""
