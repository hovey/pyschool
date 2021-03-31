# README

## Test Discovery

Comparison of test discovery of [`unittest`](https://docs.python.org/3/library/unittest.html) versus [`pytest`](https://docs.pytest.org/en/stable/): 
* Is a naming convention *pattern* supported by *framework*, *yes* or *no* (indicated with a period ".")?

Pattern | unittest | pytest
---|:---:|:---:
**Module** | |
`test*.py` | yes | .
`test_*.py` | yes | yes
`*_test.py` | . | yes
**Class** | |
Class descendant of `unittest`:</br>`<Class>(unittest.TestCase):` | yes | yes
Class method of a `unittest` class:</br>`test_*` | yes | yes
Class (*not* a descendant of `unittest`):</br>`Test*:` | . | yes
Class method (of a class *not* a `unittest` descendant):</br>`test_*` | . | yes
**Function** | |
`test_*` | . | yes
