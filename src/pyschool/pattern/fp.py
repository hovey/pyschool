# Functional Programming in Python
# Use immutable data
# Use filter, map, and reduce

from typing import NamedTuple

"""Introduction to Functional Programming in Python

References:
Dan Bader, Functional Programming in Python: Immutable Data Structures, Real Python,
30 Aug 2017.
Video 1: https://youtu.be/xJCPpDlk9_w
Six lectures in this series

Start with dictionaries, which are mutable.  Mutable data allows for side effects
(bugs and other unintended consequences) and prohibits concurrency.  Instead, prefer
tuples, which are immutable, to dictionaries, which are mutable.

Other disadvantages of dictionaries:
* Can add to dictionary with possible typos for the keys.
* The appearance of keys gets repetitve and creates noise around the values, which
  are the true items of interest.
"""

scientists_dict = [
    {"name": "Lovelace", "field": "math", "born": 1815, "nobel": False},
    {"name": "Noether", "field": "math", "born": 1882, "nobel": False},
    {"name": "Curie", "field": "physics", "born": 1867, "nodel_oops": True},
]

"""Also, the dict allows for bad keys to be used.
Example:
>>> import fp
>>> fp.scientists_dict
[{'name': 'Lovelace', 'field': 'math', 'born': 1815, 'nobel': False}, {'name': 'Noether', 'field': 'math', 'born': 1882, 'nobel': False}, {'name': 'Curie', 'field': 'physics', 'born': 1867, 'nodel_oops': True}]

Even if we get the key correct, we can still corrupt the value with the wrong type!
This creates a lurking bad value because dicts have no type checking on the values.
Example:
>>> s0_bad_value = dict(name="Lovelace", field="math", born="should be int, not string", nobel=False)
>>> s0_bad_value["born"]
'should be int, not string'
>>> type(s0_bad_value["born"])
<class 'str'>
Yuck!  The type should be an int, not a string, but dictionaries allowed us to
construct data with value type errors.


The functional alternative: NamedTuple

A sensible alternative to a dictionary is a NamedTuple, which is immutable, and can
enforce type checking.
"""


class Scientist(NamedTuple):
    name: str
    field: str
    born: int
    nobel: bool


"""
t = fp.Scientist()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __new__() missing 4 required positional arguments: 'name', 'field', 'born', and 'nobel'

Error checking upon construction, never construct a bad type (unlike dictionaries, which
can admit typos in the keys.)

>>> s0 = fp.Scientist(name="Lovelace", field="math", born="should be int, not string", nodel=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __new__() got an unexpected keyword argument 'nodel'
"""


s0 = Scientist(name="Lovelace", field="math", born=1815, nobel=False)
s1 = Scientist(name="Noether", field="math", born=1882, nobel=False)
s2 = Scientist(name="Curie", field="physics", born=1867, nobel=True)
s3 = Scientist(name="Youyou", field="chemisty", born=1930, nobel=True)
s4 = Scientist(name="Yonath", field="chemisty", born=1939, nobel=True)
s5 = Scientist(name="Rubin", field="astronomy", born=1928, nobel=False)
s6 = Scientist(name="Ride", field="physics", born=1951, nobel=False)

scientists = (s0, s1, s2, s3, s4, s5, s6)


"""
>>> fp.s0
Scientist(name='Lovelace', field='math', born=1815, nobel=False)
>>> fp.s1
Scientist(name='Noether', field='math', born=1882, nobel=False)

Video 2:  https://youtu.be/fkjjqyfN51c
Functional Programming in Python: The "filter()" Function
06 Sep 2017

filter: (function or None, iterable)
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true.  If function is None, return items that are true.

Return a new list that is filtered by if the Scientist won a Nobel prize.
>>> scientists_filtered = filter(lambda x: x.nobel is True, fp.scientists)
>>> type(scientists_filtered)
<class 'filter'>
>>> next(scientists_filtered)
Scientist(name='Curie', field='physics', born=1867, nobel=True)
>>> next(scientists_filtered)
Scientist(name='Youyou', field='chemisty', born=1930, nobel=True)
>>> next(scientists_filtered)
Scientist(name='Yonath', field='chemisty', born=1939, nobel=True)
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
(Scientist(name='Curie', field='physics', born=1867, nobel=True), Scientist(name='Youyou', field='chemisty', born=1930, nobel=True), Scientist(name='Yonath', field='chemisty', born=1939, nobel=True))

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

Finally, the magic of functional program, declarative functions chained together.
"""


def nobel_filter(x):
    return x.nobel is True


"""
>>> winners_functional = tuple(filter(fp.nobel_filter, fp.scientists))
>>> winners_functional
(Scientist(name='Curie', field='physics', born=1867, nobel=True), Scientist(name='Youyou', field='chemisty', born=1930, nobel=True), Scientist(name='Yonath', field='chemisty', born=1939, nobel=True))
"""


def physics_filter(x):
    return x.field == "physics"


"""
>>> physicists_functional
(Scientist(name='Curie', field='physics', born=1867, nobel=True), Scientist(name='Ride', field='physics', born=1951, nobel=False))
"""


def physics_nobel_filter(x):
    return physics_filter(x) and nobel_filter(x)


"""
>>> winners_physicists_functional = tuple(filter(fp.physics_nobel_filter, fp.scientists))
>>> winners_physicists_functional
(Scientist(name='Curie', field='physics', born=1867, nobel=True),)
"""
