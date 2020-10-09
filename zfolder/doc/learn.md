# Learn

## Previous: [Introduction](introduction.md)

## Introduction

Here is the workflow scenario:

* There is a master branch on the `pyschool/zfolder/` that holds items required to develop, test, and deploy the `zmath` package. 
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

Previous developers have created the existing repo  at `/pyschool/zfolder/` and populated it with the main service and tests, based on the [python package template](https://packaging.python.org/tutorials/packaging-projects/#creating-the-package-files) and a [recommended folder structure](https://godatadriven.com/blog/how-to-start-a-data-science-project-in-python/), as follows:

```bash
zfolder/ # a general folder checked into a repo, holds all zmath paraphernalia
│
│   # repo items #
├── zmath/ # maps to the zmath Python package
│   ├── __init__.py # makes the folder a package
│   └── zalculator.py # a service of the zmath package
├── data/
│   └── test-004-haversine.csv # for eventual use, placeholder for now
├── doc/
│   └── introduction.md
├── tests/
│   └── test_zalculator.py # tests the zmath package
├── .gitignore # marks setup.py objects as not for repo
├── LICENSE
├── README.md
├── setup.sh # creates the zmath conda environment
├── setup.py
│
│   # non-repo items, which will appear upon building a deployment #
├── build/ # a setup.py target, not for repo, subject to .gitignore
└── dist/ # a setup.py target, not for repo, subject to .gitignore
└── zmath.egg-info/ # a setup.py target, not for repo, subject to .gitignore
```

Also, previous developers have deployed the service to [PyPi](https://pypi.org/) as the `zmath` package (aka library), following their
[deployment steps](deployment.md).

## Next: [Configuration](configuration.md)