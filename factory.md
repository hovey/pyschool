# Factory

## Introduction

The **Factory Pattern** is software design patterns used for object *creation*.
Use of a factory pattern: 
* [**D.R.Y.**](README.md#dry-it-out):  Centralizes the creation of objects, which makes code easier to understand.  In contrast, without the use of a factory pattern, object creation is spread throughout the code base, which can be difficult to debug and maintain.
* [**Client-service decoupling**](README.md#client-service-decoupling):  Decouples client from service.  The client gets to know *what* (service interface) is being created, but does not need to be concerned with the *how* or *where* (service implementation) of creation.  Thus, in the future, when the manner in which objects are created changes, only the service needs to react to the change; clients continue to work without modification.

There are two main categories of the Factory Pattern: (1) **Static Factory Method**, and (2) **Abstract Factory**.

## Static Factory Method
A static factory method is a singleton function that may or may not reside in a class.  Clients will pass a parameter to the factory method to indicate to the factory the type of object the client would like the factory to return.

## Abstract Factory
The abstract factory is a **collection** of factory methods, with each factory method creating a unique class of object.  

## Examples

* Creation of [shapes](super/shapes.py) with a dictionary.
* [Anirudh's factory](factory/) based on folders instead of dictionary creation.

### Dynamic Load of Module

```python
Reference:
# https://www.blog.pythonlibrary.org/2016/05/27/python-201-an-intro-to-importlib/
# https://airbrake.io/blog/python-exception-handling/importerror-and-modulenotfounderror

def module(module_name):
    """
    Checks if module can be imported from the module_name.
    If the module can be imported, it returns the module.
    If the module can't be imported, it returns None.

    Args:
        module_name (string): The name of the module to be imported.

    Returns:
        The _module or None.
    """
    try:
        _module_specification = ilu.find_spec(module_name)
        if _module_specification: 
            print(f'Module "{module_name}" is found and can be imported.')
            _module = ilu.module_from_spec(_module_specification)
            _module_specification.loader.exec_module(_module)
            return _module
    except ImportError as error:
        print(f'Error: Module "{module_name}" is not found.')
        print(error.__class__.__name__)
        return None
```

### Client-Use of Dynamic Module Load

```python
key = next(iter(process_dict))
value = process_dict[key]

process_module = module(f'{key}.process')
if process_module:
    process_object = getattr(process_module, 'Process')
    pobject = process_object(self._data, **value)
```

## References

* [Eckel](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html) B. Python 3 Patterns, Recipies, and Idioms.
* Kasampalis S. Mastering Python design patterns. Packt Publishing Ltd; 2015 Jan 28.
