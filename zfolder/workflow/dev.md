# Dev

## Set up local development environment

* Install [Visual Studio Code](https://code.visualstudio.com/)
* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* Create a virtual environment called `zmathenv` and then activate that newly-created environment:

```bash 
(base) $ conda create --name zmathenv python=3.8 numpy matplotlib pytest pytest-cov flake8 black pylint
(base) $ conda activate zmathenv
(zmathenv) $
```

* [Connect](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh) to GitHub with ssh.
* Clone the repo:

```bash
(zmathenv) $ git@github.com:hovey/pyschool.git
```

* Install the existing `zmath` library in developer mode:

```bash
(zmathenv) $ cd ~/pyschool
(zmathenv) $ # to come, ask Anirudh on this step.
```

## Check out the master branch repository

To come.

## Create a feature branch

To come.

## Check existing unit tests pass on your local machine

```bash
(zmathenv) [~/pyschool]$ python -m unittest -v
```

which will show all the current unit tests (this or similar):

```bash
test_add (cont_integ.test_calculator.MyTestCase) ... ok
test_divide (cont_integ.test_calculator.MyTestCase) ... ok
test_multiply (cont_integ.test_calculator.MyTestCase) ... ok
test_subtract (cont_integ.test_calculator.MyTestCase) ... ok
test_empty_dict_on_startup (pubsub.test.test_pubsub.TestPubSub) ... PublisherBase.__init__() for The New York Times
Newspaper.__init__() for The New York Times
ok
test_pub_sub (pubsub.test.test_pubsub.TestPubSub) ... PublisherBase.__init__() for The Wall Street Journal
Newspaper.__init__() for The Wall Street Journal
SubscriberBase.__init__() for Alice Ackerman
Lectiophile.__init__() for Alice Ackerman
SubscriberBase.__init__() for Bob Beverly
Lectiophile.__init__() for Bob Beverly
SubscriberBase.update() for Alice Ackerman
SubscriberBase.serialize() for Bob Beverly
ok
test_same (pubsub.test.test_pubsub.TestPubSub) ... ok
test_constructor (quartiles.test_pfield.MyTestCase) ... ok
test_input_folder_and_file (quartiles.test_pfield.MyTestCase) ... ok
test_quartiles (quartiles.test_pfield.MyTestCase) ... ok
test_load_json (test_unittest.TestLoadJSON)
Test loading the data ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.008s
```

## Create new unit tests for code coverage and edge cases

Tests should cover at least 80 percent of your code, preferably 100 
percent.  Documentation on code covers is to come.

In the `~/pyschool/zfolder/tests` folder, either add the the existing test file [`test_zalculator.py`](../tests/test_zalculator.py) or create your own test(s) with the `test_<my_file_name>.py` pattern.

Test your unittest files (or your updates to the existing `test_zalculator.py` file) using this (or similar for your file):

```bash
(zmathenv) [~/pyschool]$ python -m unittest -v zfolder/tests/test_zalculator.py
```

which will show the unittests (this or similar):

```bash
test_add (zfolder.tests.test_zalculator.TestZalculator) ... ok
test_subtract (zfolder.tests.test_zalculator.TestZalculator) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Check all unit tests pass

Finally, rerun all unit tests, and make sure you new unit tests appear in the global lise of unit tests, e.g., 

```bash
(zmathenv) [~/pyschool]$ python -m unittest -v
test_add (cont_integ.test_calculator.MyTestCase) ... ok
test_divide (cont_integ.test_calculator.MyTestCase) ... ok
test_multiply (cont_integ.test_calculator.MyTestCase) ... ok
test_subtract (cont_integ.test_calculator.MyTestCase) ... ok
test_empty_dict_on_startup (pubsub.test.test_pubsub.TestPubSub) ... PublisherBase.__init__() for The New York Times
Newspaper.__init__() for The New York Times
ok
test_pub_sub (pubsub.test.test_pubsub.TestPubSub) ... PublisherBase.__init__() for The Wall Street Journal
Newspaper.__init__() for The Wall Street Journal
SubscriberBase.__init__() for Alice Ackerman
Lectiophile.__init__() for Alice Ackerman
SubscriberBase.__init__() for Bob Beverly
Lectiophile.__init__() for Bob Beverly
SubscriberBase.update() for Alice Ackerman
SubscriberBase.serialize() for Bob Beverly
ok
test_same (pubsub.test.test_pubsub.TestPubSub) ... ok
test_constructor (quartiles.test_pfield.MyTestCase) ... ok
test_input_folder_and_file (quartiles.test_pfield.MyTestCase) ... ok
test_quartiles (quartiles.test_pfield.MyTestCase) ... ok
test_load_json (test_unittest.TestLoadJSON)
Test loading the data ... ok
test_add (zfolder.tests.test_zalculator.TestZalculator) ... ok
test_subtract (zfolder.tests.test_zalculator.TestZalculator) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.009s

OK
```

## Check you code (both dev code and test code) passes Black

```bash
(zmathenv) [~/pyschool] $ black --check zfolder/
would reformat /Users/sparta/pyschool/zfolder/setup.py
would reformat /Users/sparta/pyschool/zfolder/tests/test_zalculator.py
Oh no! 💥 💔 💥
2 files would be reformatted, 4 files would be left unchanged.
```

Fix the formatting in any files that are indicated with "would reformat".  

You can have VS Code either auto-format with Black on save by 
adding the following lines to VS Code's `~/Library/Application Support/Code/User/settings.json` file:

```bash
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
```

Or, you can manually discover Black's changes, using this:

```bash
(zmathenv) [~/pyschool]$ black --diff  zfolder/setup.py
```

## Test just the `/pyschool/zfolder/zmath` directory

```bash
(zmathenv) [sparta ~/pyschool]$ pytest zfolder/tests/ -v
=============================================== test session starts ===============================================
platform darwin -- Python 3.8.5, pytest-6.0.2, py-1.9.0, pluggy-0.13.1 -- /opt/miniconda3/envs/zmathenv/bin/python
cachedir: .pytest_cache
rootdir: /Users/sparta/pyschool/zfolder
plugins: cov-2.10.1
collected 2 items                                                                                                 

zfolder/tests/test_zalculator.py::TestZalculator::test_add PASSED                                           [ 50%]
zfolder/tests/test_zalculator.py::TestZalculator::test_subtract PASSED                                      [100%]

================================================ 2 passed in 0.04s ================================================
```

## Test the entire `pyschool` directory

```bash
(zmathenv) [sparta ~/pyschool]$ pytest -v
=============================================== test session starts ===============================================
platform darwin -- Python 3.8.5, pytest-6.0.2, py-1.9.0, pluggy-0.13.1 -- /opt/miniconda3/envs/zmathenv/bin/python
cachedir: .pytest_cache
rootdir: /Users/sparta/pyschool
plugins: cov-2.10.1
collected 13 items                                                                                                

test_unittest.py::TestLoadJSON::test_load_json PASSED                                                       [  7%]
cont_integ/test_calculator.py::MyTestCase::test_add PASSED                                                  [ 15%]
cont_integ/test_calculator.py::MyTestCase::test_divide PASSED                                               [ 23%]
cont_integ/test_calculator.py::MyTestCase::test_multiply PASSED                                             [ 30%]
cont_integ/test_calculator.py::MyTestCase::test_subtract PASSED                                             [ 38%]
pubsub/test/test_pubsub.py::TestPubSub::test_empty_dict_on_startup PASSED                                   [ 46%]
pubsub/test/test_pubsub.py::TestPubSub::test_pub_sub PASSED                                                 [ 53%]
pubsub/test/test_pubsub.py::TestPubSub::test_same PASSED                                                    [ 61%]
quartiles/test_pfield.py::MyTestCase::test_constructor PASSED                                               [ 69%]
quartiles/test_pfield.py::MyTestCase::test_input_folder_and_file PASSED                                     [ 76%]
quartiles/test_pfield.py::MyTestCase::test_quartiles PASSED                                                 [ 84%]
zfolder/tests/test_zalculator.py::TestZalculator::test_add PASSED                                           [ 92%]
zfolder/tests/test_zalculator.py::TestZalculator::test_subtract PASSED                                      [100%]

=============================================== 13 passed in 0.45s ================================================
```

## Code Coverage with line numbers missing coverage

```bash
(zmathenv) [sparta ~/pyschool]$ pytest --cov=zfolder/zmath -v --cov-report term-missing
=============================================== test session starts ===============================================
platform darwin -- Python 3.8.5, pytest-6.0.2, py-1.9.0, pluggy-0.13.1 -- /opt/miniconda3/envs/zmathenv/bin/python
cachedir: .pytest_cache
rootdir: /Users/sparta/pyschool
plugins: cov-2.10.1
collected 13 items                                                                                                

test_unittest.py::TestLoadJSON::test_load_json PASSED                                                       [  7%]
cont_integ/test_calculator.py::MyTestCase::test_add PASSED                                                  [ 15%]
cont_integ/test_calculator.py::MyTestCase::test_divide PASSED                                               [ 23%]
cont_integ/test_calculator.py::MyTestCase::test_multiply PASSED                                             [ 30%]
cont_integ/test_calculator.py::MyTestCase::test_subtract PASSED                                             [ 38%]
pubsub/test/test_pubsub.py::TestPubSub::test_empty_dict_on_startup PASSED                                   [ 46%]
pubsub/test/test_pubsub.py::TestPubSub::test_pub_sub PASSED                                                 [ 53%]
pubsub/test/test_pubsub.py::TestPubSub::test_same PASSED                                                    [ 61%]
quartiles/test_pfield.py::MyTestCase::test_constructor PASSED                                               [ 69%]
quartiles/test_pfield.py::MyTestCase::test_input_folder_and_file PASSED                                     [ 76%]
quartiles/test_pfield.py::MyTestCase::test_quartiles PASSED                                                 [ 84%]
zfolder/tests/test_zalculator.py::TestZalculator::test_add PASSED                                           [ 92%]
zfolder/tests/test_zalculator.py::TestZalculator::test_subtract PASSED                                      [100%]

---------- coverage: platform darwin, python 3.8.5-final-0 -----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
zfolder/zmath/__init__.py         0      0   100%
zfolder/zmath/zalculator.py       7      1    86%   10
-----------------------------------------------------------
TOTAL                             7      1    86%


=============================================== 13 passed in 0.67s ================================================
```

Let zoom into that `Miss` in `zalculator.py`.  Line 9 and 10 of
`zalculator.py` are as follows:

```python
    def __init__(self):
        print("The Zalculator is initialized."
```

We update that method as follows:
```python
    def __init__(self):
        self.initialized = False
        print("The Zalculator is initialized.")
        self.initialized = True
```

Currently, there no test that exercises the print statement of the `__init__` function.
So, in `test_zalculatory.py`, we add the following test:

```python
    def __init__(self):
        self.initialized = False
        print("The Zalculator is initialized.")
        self.initialized = True
```

which tests coverage of that line.

```bash
(zmathenv) [sparta ~/pyschool]$ pytest --cov=zfolder/zmath -v --cov-report term-missing
=============================================== test session starts ===============================================
platform darwin -- Python 3.8.5, pytest-6.0.2, py-1.9.0, pluggy-0.13.1 -- /opt/miniconda3/envs/zmathenv/bin/python
cachedir: .pytest_cache
rootdir: /Users/sparta/pyschool
plugins: cov-2.10.1
collected 14 items                                                                                                

test_unittest.py::TestLoadJSON::test_load_json PASSED                                                       [  7%]
cont_integ/test_calculator.py::MyTestCase::test_add PASSED                                                  [ 14%]
cont_integ/test_calculator.py::MyTestCase::test_divide PASSED                                               [ 21%]
cont_integ/test_calculator.py::MyTestCase::test_multiply PASSED                                             [ 28%]
cont_integ/test_calculator.py::MyTestCase::test_subtract PASSED                                             [ 35%]
pubsub/test/test_pubsub.py::TestPubSub::test_empty_dict_on_startup PASSED                                   [ 42%]
pubsub/test/test_pubsub.py::TestPubSub::test_pub_sub PASSED                                                 [ 50%]
pubsub/test/test_pubsub.py::TestPubSub::test_same PASSED                                                    [ 57%]
quartiles/test_pfield.py::MyTestCase::test_constructor PASSED                                               [ 64%]
quartiles/test_pfield.py::MyTestCase::test_input_folder_and_file PASSED                                     [ 71%]
quartiles/test_pfield.py::MyTestCase::test_quartiles PASSED                                                 [ 78%]
zfolder/tests/test_zalculator.py::TestZalculator::test_add PASSED                                           [ 85%]
zfolder/tests/test_zalculator.py::TestZalculator::test_initialize PASSED                                    [ 92%]
zfolder/tests/test_zalculator.py::TestZalculator::test_subtract PASSED                                      [100%]

---------- coverage: platform darwin, python 3.8.5-final-0 -----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
zfolder/zmath/__init__.py         0      0   100%
zfolder/zmath/zalculator.py       9      0   100%
-----------------------------------------------------------
TOTAL                             9      0   100%


=============================================== 14 passed in 0.66s ================================================
```

## Push your code from local to repo feature branch

| Previous |  Next |
|----------|------:|
| [learn](learn.md) | [propose](propose.md) | 
