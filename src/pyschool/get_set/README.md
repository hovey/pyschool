# Get and Set, the Pythonic Way

The use of `get` and `set` is demonstrated through several iterations of simple Python program that converts Celsius to Fahrenheit.

## Version 1

* `version1.py` is the main class definition.
* `version1_test_001.py` is the client test harness.
    * The client's use of the server's variable `temperature` is exposed through `c.temperature`, which is a brittle style, since it exposes the server's data to the client.
    * A better way for the client to interact with the server is through `get` and `set` functions.

## Version 2

* `verion2.py` is an updated version of `version1.py`, but with two additions: get/set methods and error checking:
    * Get/Set Methods
        * The local variable in `version1.py` called `temperature` is changed in `version2.py` to `_temperature`.
        * The leading underscore in the `_temperature` variable name is a convention to describe a private variable of a class.
        * In Python, private variables don't actually exist, so the  leading underscrore is just a convention.  
        * Clients can circumvent the `c.get_temperature()` API simply through `c._temperature`.
    * Error Checking
        * The set method will make sure the value being set is not below `-273.15` degrees Celsius, which is absolute zero Kelvin.
* `version2_test_001.py` is the client test harness.
    * Client code written to the previous server standard in `version1.py` with the `c.temperature` convention must now be rewritten to use either the get or the set methods, viz., `c.get_temperature()` and `c.set_temperature(new_value)`, which places significant rewrite burden on clients.  But, clients shouldn't be accessing server private data in the first place.
    * The addition of the `get` prefix and `set` prefix is verbose.  
    * Verbs (e.g., `get` and `set`), per [David Cheriton](https://en.wikipedia.org/wiki/David_Cheriton) are unnecessary, undesired, and pollute and bloat the API, and thus should be avoided.

## Version 3

* `version3.py` eliminates clutter in the API by eliminating `get` and `set` verbs through use of the `@property` construction.
* Note: the implementation here is better than what is published in the reference (see details below) because error checking is always used by virtue of server using its own `set` method in the constructor.

## References

* [Programiz.com](https://www.programiz.com/python-programming/property)  Note: the `__init__` constructor accesses the local variables `_temperature` directly, without use of the setter.  But not using setter on construction, the error checking is circumvented, which is fragile coding.  Instead, the constructor should have used the setter method.  So in summary are the `bad` and `good` methods:

```python
# BAD
def __init__(self, temperature = 0):
    self._temperature = temperature # avoids the setter, so avoids error checking, which is bad!

# GOOD
def __init__(self, temperature = 0):
    self.temperature = temperature  # uses the setter, which includes error checking, which is good!
```

* [Python 3 Docs](https://docs.python.org/3/library/functions.html#property)
   * This makes it possible to create read-only properties easily using `property()` as a [decorator](https://docs.python.org/3/glossary.html#term-decorator).

