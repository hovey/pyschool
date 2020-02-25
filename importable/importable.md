# importable

## Definitions

* **module** a python file with a `.py` extension
* **package** a folder with modules inside of it

## Example

```python
import abc
```

## Search Order

* `sys.modules` which is a cache of all modules previously imported
* built in modules, which are pre-installed with Python and found in the Python Standard Library
* `sys.path` which is a list of directories, usually to include the current directory, which is search first
* If the module cannot be found, Python throws a `ModuleNotFoundError`

## Types of Imports

### Global Import

```python
import abc
```

The import can also be renamed as `something_else` as in

```python
import abc as something_else
```

This pattern is frequently seen, for example, in

```python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
```

### Scoped Import

To import a specific `xyz` module, subpackage, class, or function:

```python
from abc import xyz
```


## PEP 8 Style

* imports appear at the top of the file, after any module comments and docstrings, and are 
* grouped by 
  * standard library imports, which are Python's built-in modules
  * third-party imports, which are modules that are installed but do not belong to the current application
  * local imports, which are modules belonging to the current application
  * and separated into each  of the three groups by a single blank space
* ordered in alphabetical order to facilitate easy visual search as to whether or not a particular module or package is imported

For example
```python
"""
Initial docstring with imports to follow.
Here is a second docstring.
"""

# standard library imports
import datetime
import os

# third-party imports
import numpy as np
import matplotlib as mpl

# local imports
from local_module import local_class
from local_package import local_function
```

## Absolute versus Relative Imports

* [Real Python](https://realpython.com/absolute-vs-relative-python-imports/) discussion
* Absolute imports are preferred to relative imports, for the following reasons:
* Absolute imports
  * are clear and straightforward, 
  * remain valid even if the current location of the client that imports the module moves (relative imports can break and thus are much more fragile), 
  * recommended by PEP 8.

## Client imports of Server Modules

In the client-server paradigm, the clients can use *neither* absolute *nor* relative path imports because the client code (correctly and appropriately) sits completely outside and separate from the server code.  

For the client to include server modules, the client **must** know where the server is installed.  The client follows:

```python
import sys
sys.path.insert(0, '/path/to/server')
```
