# Bindings for Python

## Motivation

Why bind?

* A library, written in either C or C++, already exists.  The library is trusted, it should be reused *with* Python, not reinvented *in* Python.
* A particular part of a Python codebase is slow and could benefit from a C speed up.
* The Python test tools can test, and thus add value to, the C implementation.

## Introduction

* Marshalling
  * is the process of transforming memory into a data object for storage or transmission
  * is what Python bindings do when data moves from Python to C or C to Python
  * is required because Python and C sotre data differently
* Data types
  * All Python data are objects
  * C data types will be int, float, string, bool
  * C and C++ differ on how they store strings
* Mutation
  * In C, all parameters are pass-by-value.  Thus, a Python object passed to C is naturally immutable.

## Memory Management

### Python

In Python, there is no memory management.

```Python
a = 4
```

### C++

In C++, there is memory management.

```C++
int* p_int = (int*)malloc(sizeof(int));
```

## Getting Started

[Invoke](http://www.pyinvoke.org/) is used to build and test a Python binding.  It is
similar to `make` but uses Python instead of `Makefiles`.

```bash
> conda activate pyschoolenv
> python -m pip install invoke
```

Review the [tasks.py](tasks.py) file contents.

## References

* *[Extending Python with C or C++](https://docs.python.org/3/extending/extending.html)*
* [Python Bindings: Calling C or C++ from Python](https://realpython.com/python-bindings-overview/#calling-the-function)
* [Python Bindings Github Repo](https://github.com/realpython/materials/tree/master/python-bindings)
