[![black](https://github.com/hovey/pyschool/workflows/black/badge.svg)](https://github.com/hovey/pyschool/actions)
[![coverage](https://github.com/hovey/pyschool/workflows/coverage/badge.svg)](https://github.com/hovey/pyschool/actions)
[![codecov](https://codecov.io/gh/hovey/pyschool/branch/master/graph/badge.svg)](https://codecov.io/gh/hovey/pyschool)

# pyschool

The **pyschool** repository demonstrates

*Best Practices*, 
*Pythonic Practices*, and 
*Design Patterns* implemented in Python.

## Best Practices

* [D.R.Y. > W.E.T.](doc/dry.md)
* [Convention > Configuration](doc/convention.md)
* [Code Smell](doc/code_smell.md)
* Verb Smell
  * [Get and Set](doc/get_and_set.md)
  * [C.R.U.D.](doc/crud.md)
* [Client and Service](doc/client_service.md)
* Production
  * Style (with Black)
  * Test (with Pytest)
  * [Coverage](doc/coverage.md)
  * Continuous Integration (CI)
  * Deployment (with PyPI)
* Docstrings
* Object Oriented Programming (OOP)
  * Open-Closed Principle (OCP)
  * Separation of concern
  * Interface versus implementation
* Singleton versus Collections, part of [REST](https://restfulapi.net/resource-naming/)

## Pythonic Practices

* Iterator
* Decorator (of Python)
* List comprehension
* Error handling

## Patterns

* Adapter
* Singleton
* Decorator
* Factory
  * Static Factory Method
  * Builder
  * Abstract Factory
* Publish-Subscribe (aka "PubSub" and Observer)

## Examples

* Anatomy of a figure
* Animation
* Colors
* Element scale versus density
* Growth charts
* Imports
* Least squares
* Midpoint differentiation
* Oscillator
* Quartiles
* Scientific notation

## Toolbox

* VIM [macros](src/pyschool/vim_macros/example.py)

## Pythonic Patterns

### Attributes

* See the [`get_set` example](src/pyschool/get_set/README.md), which goes through a short code example, with evolution from bad, to better, to best implementations.  

### Client-Service

* To come.

### Decorators

* An [example](src/pyschool/decorator/logging_decorator.py) of a logging decorator pattern, which can help D.R.Y. out code (based on [this example](http://book.pythontips.com/en/latest/decorators.html#logging)).
* An [example](src/pyschool/decorator/decorators.py), using factorial, `tic-toc` timing convention, and [memoization](https://en.wikipedia.org/wiki/Memoization).
* See also [Real Python](https://realpython.com/primer-on-python-decorators/), [Wiki Python](https://wiki.python.org/moin/PythonDecorators), [Yasoob Khalid](http://book.pythontips.com/en/latest/decorators.html)

### Docstrings

* See [Google docstring format](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
* Nice [examples](https://gist.github.com/candlewill/fce04bb26d402288cd02f09bd4f5f562) of Google docstring format

### Error Checking (ask for forgiveness, not permission)

* See [examples](src/pyschool/errors/error_check.md).

### [Factory](src/pyschool/factory/README.md)

### [Publish-Subscribe](src/pyschool/pubsub/README.md) (aka Observer)

### Import

* When [importing modules](src/pyschool/importable/importable.md) from non-local directories.  Used often in client-service patterns.

### Inheritance

* A compact [example](src/pyschool/inheritance_farm/readme.txt), showing a verb astraction (e.g., `speak`) and inheritance of behavior, with a simple client-service architecture.
* [shapes](src/pyschool/super/shapes.py)

### Model, View, Controller (MVC)

* [shapes_mvc](src/pyschool/super/shapes_mvc.py)

### Unit Test

* An [example](tests/test_unittest.py), using the [unittest.mock](https://docs.python.org/3/library/unittest.mock.html#) library for testing in Python.
* [Real Python](https://realpython.com/python-mock-library/) article.  

Examples from `xyfigure_test.py`:

```bash
$ python xyfigure_test.py                      # for terse interaction,
$ python -m unittest xyfigure_test             # for default interaction,
$ python -m unittest -v xyfigure_test          # for higher verbosity, and

$ python -m unittest xyfigure_test.TestImageDiff.test_same  # e.g., to test the test_same() method
```

## Examples

### Conda

* virual environment (venv)

```bash
# from [Apollo/sibl] with all folders containin __init__.py file:
(base) conda create -n temp
(base) conda activate temp
(temp) conda install numpy scipy matplotlib
(temp) conda install pip
(temp) pip install -e .  # -e is development mode, if code updates, new pip install is not required
(temp) conda list
(temp) 
(temp) conda deactivate
(base) conda remove -n temp --all
# list all environments:
(base) conda info --envs
```

* also, pip virtual environment (venv)

```bash
(base) python -m venv fire
```

### Computation

* [Ordinary least squares](src/pyschool/least_squares/ols.py)
* Several examples in the `monkey_see` folder  

### Debugger

Example:  From `~/sibl/xyfigure/test` in VS Code, `Run | Open Configurations` and add to `launch.json` the following:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "/Users/Apollo/sibl/xyfigure/xyfigure.py",
            "args": ["signal_process_serialize.json"],
            "console": "integratedTerminal"
        }
    ]
}
```

### Production

Once the code base has sufficient development, and it is ready for production, use the following steps:

* TLC - timing, leaks, [coverage](https://github.com/marketplace/actions/coveralls-github-action)
* Test
  * Unit Test
  * Integration Test
* [Packaging/Distribution/PyPI](https://packaging.python.org/tutorials/packaging-projects/) (Build, Installer), and packaging [guide](https://packaging.python.org/guides/distributing-packages-using-setuptools/), and [distribution](https://pypi.org/) with PyPI.
* [Packaging and Distribution](https://conda.io/projects/conda-build/en/latest/) with Conda to create a [Conda Package](https://conda.io/projects/conda/en/latest/user-guide/concepts/packages.html).  Building conda packages [from scratch](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html).
* Client Use
  * Client [Installation](https://packaging.python.org/tutorials/installing-packages/)
  * Client Bug Reports (https://github.com/hovey/pyschool/issues)
  
  #### Production/Distribution Notes
  
```bash
# -----------------
# production server
# -----------------
$ cd ~/sibl/xyfigure
$ rm -r xyfigure.egg-info/
$ vim setup.py   # update setup.py, typically increment the version, located parent file README.md

# update server if necessary
$ python -m pip install --user --upgrade setuptools wheel
$ python -m pip install --user --upgrade twine

# build to the dist/ subdirectory
$ python setup.py sdist bdist_wheel

# assure the PyPI API token for the server is created on pypi.org and saved on the server at ~/.pypirc

# remove any old .gz and .whl files in dist/ subdirectory
$ cd dist/  #rm old .gz and old .whl
$ cd ../  # back to the ~/sibl/xyfigure directory

# deploy
$ python -m twine upload dist/*

# ------
# client
# ------
$ pip list
$ pip uninstall sibllib  # the old name
$ cd /nscratch/chovey/casco_sim/temp/
$ pip install --user xyfigure-0.0.4-py3-none-any.whl
$ pip list
```

## References

* [Effective-Python](https://hacktec.gitbooks.io/effective-python/content/en/Chapter1/Chapter1.html)
* [GitHub build badge](https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow#adding-a-workflow-status-badge-to-your-repository)
