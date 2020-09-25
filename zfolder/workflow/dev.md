# Dev

## Set up local development environment

* Install [Visual Studio Code](https://code.visualstudio.com/)
* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
* Create a virtual environment called `zmathenv` and then activate that newly-created environment:

```bash 
(base) $ conda create --name zmathenv python=3.8 numpy matplotlib pytest flake8 black
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
(zmathenv) $
```

## Check out the master branch repository

## Create a feature branch

## Check existing unittests pass

```bash
(zmathenv) $ cd ~/pyschool
(zmathenv) $ python -m unittest -v
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

## Create new unittests to cover 100% of your code

In the `~/pyschool/zfolder/tests` folder, either add the the existing test file [`test_zalculator.py`](../tests/test_zalculator.py) or create your own test(s) with the `test_<my_file_name>.py` pattern.

Test your unittest files (or your updates to the existing `test_zalculator.py` file) using this (or similar for your file):

```bash
(zmathenv) $ cd ~/pyschool
(zmathenv) $ python -m unittest -v zfolder/tests/test_zalculator.py
```
which will show the unittests (this or similar):

```bash
test_add (zfolder.tests.test_zalculator.TestZalculator) ... ok
test_subtract (zfolder.tests.test_zalculator.TestZalculator) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Check all unittests pass

Finally, rerun all unit tests, and make sure you new unit tests appear in the global lise of unit tests, e.g., 

```bash
(zmathenv) [sparta ~/pyschool]$ python -m unittest -v
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

## Check dev and test code passes Black

## Push your code from local to repo feature branch

| Previous |  Next |
|----------|------:|
| [learn](learn.md) | [propose](propose.md) | 