# Dev

## Previous: [Configuration](configuration.md)

## Prior to work, verify *existing* unit tests pass

```bash
(zmathenv) [~/pyschool]$ pytest -v
```

Does this step show 100 percent of tests are `PASSED`?

* Yes: proceed to the next step; or, 
* No: do not proceed, your local machine is not yet properly configured.

For an overview of the `unittest` and `pytest` frameworks, see [Testing](../../testing/README.md).

## Create a feature

To implement your feature, create or update code in the `~/pyschool/zfolder/zmath` folder.

## Create unit tests

Tests should cover at least 80 percent of your code, preferably 100 
percent.  Documentation on code covers is to come.

In the `~/pyschool/zfolder/tests` folder, either add the the existing test file [`test_zalculator.py`](../tests/test_zalculator.py) or create your own test(s) with the `test_<my_file_name>.py` pattern.

Test your unit test files (or your updates to the existing `test_zalculator.py` file) using this (or similar for your file):

```bash
(zmathenv) [~/pyschool]$ pytest zfolder/ -v 
```

Does this step show 100 percent of tests are `PASSED`?

* Yes: proceed to the next step; or, 
* No: do not proceed, your tests do no yet pass.

## Check code style

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

## Test Coverage

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
    print("The Zalculator is initialized.")
```

We update that method as follows:
```python
def __init__(self):
    self.initialized = False
    print("The Zalculator is initialized.")
    self.initialized = True
```

Currently, there no test that exercises the print statement 
of the `__init__` function. So, in `test_zalculatory.py`, 
we add the following test:

```python
def test_initialize(self):
    zc = zcalc()
    self.assertTrue(zc.initialized)
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

## Push to repo branch

By pushing from your local the feature branch on the repository, you

* back up your work, and
* allow others to pull your branch so they too can see you code on their local machine

Repeat the steps on this page as necessary for continued development, or proceed to the next step.

## References

* [Real Python PEP8](https://realpython.com/python-pep8/) and comments on Black

## Next: [Propose](propose.md)