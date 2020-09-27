# Learn

## Previous: [Introduction](introduction.md)

## Introduction

Here is the workflow scenario:

* There is a master branch on the `pyschool/zfolder/` that provides the `zmath` package. 
* The `zmath` package is a limited math service that implements functionality through the `Zalculator` class.  
  * This class is contained the [`zalculator.py`](../zmath/zalculator.py) file.  
  * This class currently provides clients of the `zmath` service with `add` and `subtract` functionality.
* Your job is to implement `divide` functionality, while your colleague implements the `multiply` functionality.  
* You and your colleague plan to use **branches** of the master repository.  
* In steps, you will
  * design the **interface**,
  * **implement** the functionality, 
  * **document** the source code, 
  * **unit test** the code, and finally
  * create a **pull request** to have your branch functionality merged with the main code branch.  

## Background

Previous developers have created the existing repo  at `/pyschool/zfolder/` and populated it with the main service and tests, based on the [python package template](https://packaging.python.org/tutorials/packaging-projects/#creating-the-package-files), as follows:

```bash
zfolder
├── LICENSE
├── README.md
├── zmath # maps to the zmath package
│   ├── __init__.py
│   └── zalculator.py
├── setup.py
└── tests
    └── test_zalculator.py
└── dist
    └── zmath-0.0.1-py3-none-any.whl
```

Also, previous developers have deployed the service to [PyPi](https://pypi.org/) as the `zmath` package (aka library), following their
[deployment steps](deployment.md).

## Next: [Configuration](configuration.md)