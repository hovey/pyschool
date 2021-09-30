# Functional Programming in Python
# Use immutable data
# Use filter, map, and reduce

from typing import Dict, List, NamedTuple, Tuple

"""Introduction to Functional Programming in Python by Dan Bader of Real Python
Series of six videos: https://youtube.com/playlist?list=PLP8GkvaIxJP1z5bu4NX_bFrEInBkAgTMr

To use these tutorials, import the module into python, then perform the commented
commands to interact with the data.
$ cd ~/pyschool/src/pyschool/pattern
$ conda activate pyschool-env
$ python
>>> import pyschool.pattern.functional_programming as fp

--------------------------------------------------------------------
Video 1: Functional Programming in Python: Immutable Data Structures
30 Aug 2017
https://youtu.be/xJCPpDlk9_w

Motivation: A dictionaries can cause problems.  (A NamedTuple can avoid these problems.)

We start with dictionaries, which are mutable.  Mutable data allows for side effects
(bugs and other unintended consequences) and prohibits concurrency.

Instead of using dictionaries (which are mutable), prefer tuples (which are immutable).

Disadvantages of a dictionary:
* Allows mutability, which allows bugs to be introduced.
* Allows key errors.  Has no key checking.  We can create bad keys with typos.
* Allows value errors.  Has no value checking.  We can create bad values with typos.
"""

scientists_dict = [
    {"name": "Lovelace", "field": "math", "born": 1815, "nobel": False},
    {"name": "Noether", "field": "math", "born": 1882, "nobel": False},
    {"name": "Curie", "field": "physics", "born": 1867, "nodel_typo": True},
]

"""The third record in this dictionary contains a bad key called "nodel_typo".
Example:
>>> fp.scientists_dict
[{'name': 'Lovelace', 'field': 'math', 'born': 1815, 'nobel': False}, {'name': 'Noether', 'field': 'math', 'born': 1882, 'nobel': False}, {'name': 'Curie', 'field': 'physics', 'born': 1867, 'nodel_typo': True}]

Even if we get the key correct, we can still corrupt the value with the wrong type!
A bad value type creates a lurking bug because dicts lack type checking.
Example:
>>> s0_bad_value = dict(name="Lovelace", field="math", born="should be int, not string", nobel=False)
>>> s0_bad_value["born"]
'should be int, not string'
>>> type(s0_bad_value["born"])
<class 'str'>
Yuck!  The type should be an int, not a string, but dictionaries allowed us to
construct data with value type errors.

The functional alternative: NamedTuple

A NamedTuple is a sensible alternative to a dictionary.  Advantages of a NamedTuple:
* Immutable data.
* Required positional argument checking on construction.
* Key checking on construction.
* Type checking on key on construction.

We begin be defining a Scientist, and then creating a tuple of Scientists.
"""


class Scientist(NamedTuple):
    name: str
    field: str
    born: int
    nobel: bool


"""
>>> t = fp.Scientist()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __new__() missing 4 required positional arguments: 'name', 'field', 'born', and 'nobel'

Error checking upon construction, never construct a bad type (unlike dictionaries, which
can admit typos in the keys.)

>>> s0 = fp.Scientist(name="Lovelace", field="math", born="should be int, not string", nodel=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __new__() got an unexpected keyword argument 'nodel'

Here, the bad key "nodel" has been caught, but the bad value "should be int, not string"
was not caught.  To catch the bad value, rely on a good linter, such as flake8
(https://flake8.pycqa.org/en/latest/) or use the pylance language server for python.
Pylance uses pyright, which is Microsoft's static type checking tool.
(https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).
"""


s0 = Scientist(name="Lovelace", field="math", born=1815, nobel=False)
s1 = Scientist(name="Noether", field="math", born=1882, nobel=False)
s2 = Scientist(name="Curie", field="physics", born=1867, nobel=True)
s3 = Scientist(name="Youyou", field="chemistry", born=1930, nobel=True)
s4 = Scientist(name="Yonath", field="chemistry", born=1939, nobel=True)
s5 = Scientist(name="Rubin", field="astronomy", born=1928, nobel=False)
s6 = Scientist(name="Ride", field="physics", born=1951, nobel=False)

scientists = (s0, s1, s2, s3, s4, s5, s6)


"""
>>> fp.s0
Scientist(name="Lovelace", field="math", born=1815, nobel=False)
>>> fp.s1
Scientist(name="Noether", field="math", born=1882, nobel=False)

------------------------------------------------------------------
Video 2: Functional Programming in Python: The "filter()" Function
06 Sep 2017
https://youtu.be/fkjjqyfN51c

filter: (function or None, iterable)
filter(function or None, iterable) --> filter object (which is an iterable)

Given a function(item) and an iterable of items, filter returns an iterator yielding
those items of iterable for which function(item) is true.
If function is None, filter return the items that are true.

The filter function is often more efficient than a list comprehension, especially when
working on large data sets.  A list comprehension creates a new list, which requires
time to create and bloats memory requirements for the new list's storage.  In contrast,
the filter does not create a new list.  Rather, the filter function makes a simple
object that holds a reference to the original list and acts on it, which avoids list
duplication and thus requires less memory bloat.

Return a new list that is filtered by if the Scientist won a Nobel prize.
>>> scientists_filtered = filter(lambda x: x.nobel is True, fp.scientists)
>>> type(scientists_filtered)
<class 'filter'>
>>> next(scientists_filtered)
Scientist(name='Curie', field='physics', born=1867, nobel=True)
>>> next(scientists_filtered)
Scientist(name='Youyou', field='chemistry', born=1930, nobel=True)
>>> next(scientists_filtered)
Scientist(name='Yonath', field='chemistry', born=1939, nobel=True)
>>> next(scientists_filtered)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

Construct a new immutable subset from the original immutable set.
Connection to the language of vector spaces:
* This feels like a dot product projection operator.
* The new subset is a subspace of the source set, a bigger space.
* So "filter" feels like the "projection" operator on vector spaces.

>>> winners = tuple(filter(lambda x: x.nobel is True, fp.scientists))
>>> winners
(Scientist(name='Curie', field='physics', born=1867, nobel=True), Scientist(name='Youyou', field='chemistry', born=1930, nobel=True), Scientist(name='Yonath', field='chemistry', born=1939, nobel=True))

>>> physicists = tuple(filter(lambda x: x.field == "physics", fp.scientists))
>>> physicists
(Scientist(name='Curie', field='physics', born=1867, nobel=True), Scientist(name='Ride', field='physics', born=1951, nobel=False))

>>> for p in physicists:
...     print(p)
...
Scientist(name='Curie', field='physics', born=1867, nobel=True)
Scientist(name='Ride', field='physics', born=1951, nobel=False)

Finally, find all physicists that have also won a Nobel prize:
>>> winners_physicists = tuple(filter(lambda x: x.field == "physics" and x.nobel is True, fp.scientists))
>>> winners_physicists
(Scientist(name='Curie', field='physics', born=1867, nobel=True),)

Finally, the magic of functional program: declarative functions chained together.
This is composition of two or more functions.
"""


def nobel_filter(x: Scientist) -> bool:
    return x.nobel is True


"""
>>> winners_functional = tuple(filter(fp.nobel_filter, fp.scientists))
>>> winners_functional
(Scientist(name='Curie', field='physics', born=1867, nobel=True), Scientist(name='Youyou', field='chemistry', born=1930, nobel=True), Scientist(name='Yonath', field='chemistry', born=1939, nobel=True))
"""


def physics_filter(x: Scientist) -> bool:
    return x.field == "physics"


"""
>>> physicists_functional = tuple(filter(fp.physics_filter, fp.scientists))
>>> physicists_functional
(Scientist(name='Curie', field='physics', born=1867, nobel=True), Scientist(name='Ride', field='physics', born=1951, nobel=False))
"""


def physics_nobel_filter(x: Scientist) -> bool:
    return physics_filter(x) and nobel_filter(x)


"""
>>> winners_physicists_functional = tuple(filter(fp.physics_nobel_filter, fp.scientists))
>>> winners_physicists_functional
(Scientist(name='Curie', field='physics', born=1867, nobel=True),)

See also itertools.filterfalse() for the complementary function that returns elements
of iterable when the function returns false.
"""


"""
---------------------------------------------------------------
Video 3: Functional Programming in Python: The "map()" Function
13 Sep 2017
https://youtu.be/powVeMYKCSw

map: (func, *iterables)
map(func, iterable, ...) --> map object (which is an iterable)

Make an iterator that computes the function using arguments from each of the iterables.
Stops when the shortest iterable is exhausted.

The first argument to map is a function object. The function is passed without calling
the function itself, thus used without the parenthesis ( ) of the function.)

Takes tuples and shape them into new tuples.
Example: assemble the names and ages of each scientist.

See also https://realpython.com/python-map-function/
"""


def name(x: Scientist) -> str:
    return x.name


"""
>>> names = tuple(map(fp.name, fp.scientists))
>>> names
('Lovelace', 'Noether', 'Curie', 'Youyou', 'Yonath', 'Rubin', 'Ride')
"""


def age(x: Scientist) -> int:
    _year_example = 2017
    return _year_example - x.born


"""
>>> ages = tuple(map(fp.age, fp.scientists))
>>> ages
(202, 135, 150, 87, 78, 89, 66)
"""


def name_and_age(x: Scientist) -> Tuple[str, int]:
    return name(x), age(x)


"""
>>> names_and_ages = tuple(map(fp.name_and_age, fp.scientists))
>>> names_and_ages
(('Lovelace', 202), ('Noether', 135), ('Curie', 150), ('Youyou', 87), ('Yonath', 78), ('Rubin', 89), ('Ride', 66))

If the original data set, scientists, is viewed as a matrix, with each
row as a scientist instance, and each column as an attribute of a scientists, then
* `filter` has been used to select a subset of rows for all columns, and
* `map` has been used to select a subset of columns for all rows.

So far, we have examined functions that take one parameter.
For functions that take two or more parameters, include the same number of
iterable objects after the function in the parameter to map.
For example, to construct the difference of two tuples (e.g, difference or subtraction
optione).
>>> a = tuple(range(3))
>>> a
(0, 1, 2)
>>> b = tuple(reversed(range(3)))
>>> b
(2, 1, 0)
>>>
c = tuple(map(lambda x, y: x - y, a, b))
>>> c
(-2, 0, 2)
>>> d = tuple(map(lambda x, y: y - x, a, b))
>>> d
(2, 0, -2)
See also Built-In Functions of the Python Standard Library (PSL)
https://docs.python.org/3/library/functions.html
"""

"""
---------------------------------------------------------------
Video 4: Functional Programming in Python: The "reduce()" Function
20 Sep 2017
https://youtu.be/ZrZ6vJGiE8I

Need to import functools (starting in Python 3) to get the reduce function.
"""

from functools import reduce

"""
reduce: (function, sequence[, initial])
reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.

For example, reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) calculates
((((1 + 2) + 3) + 4) + 5).

If initial is present, it is placed before the items of the sequence in the
calculation, and serves as a default value when the sequence is empty.

We make use `ages` tuple:

>>> ages = tuple(map(fp.age, fp.scientists))
>>> ages
(202, 135, 150, 87, 78, 89, 66)
>>> init = 0
>>> ages_sum = reduce(lambda x, y: x + y, ages, init)
>>> ages_sum
807
"""

"""
The next example is a reshuffle (or reorganization) of the existing scientists tuple
into a new dictionary that holds the field of study as keys and the corresponding
names of the scientists as values.  We want this as our final result:

>>> names_by_field
{
    "math": ["Lovelace", "Noether"],
    "physics": ["Curie", "Ride"],
    "chemistry": ["Youyou", "Yonath"],
    "astronomy": ["Rubin"],
}
"""

"""
Hint 1: Create a reducer function
"""


def reducer(accumulator: Dict[str, List[str]], y: Scientist) -> Dict[str, List[str]]:
    accumulator[y.field].append(y.name)
    return accumulator


"""
>>> b = reduce(fp.reducer, fp.scientists, {"math": [], "physics": [], "chemistry": [], "astronomy": []})
>>> b
{'math': ['Lovelace', 'Noether'], 'physics': ['Curie', 'Ride'], 'chemistry': ['Youyou', 'Yonath'], 'astronomy': ['Rubin']}
"""

"""
But, the method above uses a dictionary that must be predefined by the user, and this
is a weak paradigm.  Better would be to have the initial conditions react to the data,
without this user intervention.   How can this be done?
Answer: use defaultdict
Exmaple:
>>> import collections
>>> dd = collections.defaultdict(list)
>>> dd
defaultdict(<class 'list'>, {})
"""


"""
>>> c = reduce(fp.reducer, fp.scientists, collections.defaultdict(list))
>>> c
defaultdict(<class 'list'>, {'math': ['Lovelace', 'Noether'], 'physics': ['Curie', 'Ride'], 'chemistry': ['Youyou', 'Yonath'], 'astronomy': ['Rubin']})
"""


"""
Hint 3:  Make it more functional, use tuples, and not dictionaries
>>> a = tuple(map(lambda x: x.field, fp.scientists))
>>> a
('math', 'math', 'physics', 'chemistry', 'chemistry', 'astronomy', 'physics')
"""
