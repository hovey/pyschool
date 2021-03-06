# Continuous Integration

## Build and Test

* Create the Python file with basic calculator functionality (add, subtract, multiply, divide) to `calculator.py`.
* Create a unit test called `test_calculator.py`.  Note:  The `test_...` format, e.g., `test_<module>.py`, is required for [Pytest](https://docs.pytest.org/en/latest/) to discover the unit tests.
* Verify that that the tests run correctly with `$python -m pytest`.
* Push the two `*.py` files to the GitHub repository.
* At the GitHub repository web interface, click the **Actions** tab, then **Set up a workflow yourself** button.
* The default `.yml` file will appear as `pyschool/.github/workflows/main.yml`.  Change the file name from `main.yml` to `calculator.yml`.  The contents prior to any modification appear as:

```yml
name: CI

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Run a one-line script
      run: echo Hello, world!
    - name: Run a multi-line script
      run: |
        echo Add other actions to build,
        echo test, and deploy your project.
```

* Click the **Start commit** button, select **Commit New File**.
* Update the `calculatory.yml` to appear as

```yml
name: CI test of calculator.py

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
    max-parallel: 2
    matrix:
      python-version: [3.6, 3.7]

    steps:
    - uses: actions/checkout@v2
    - name: Run a one-line script
      run: echo Hello, world!
    - name: Run a multi-line script
      run: |
        echo Add other actions to build,
        echo test, and deploy your project.
  - name: Set up Python ${{ matrix.python-version }}
    uses: actions/setup-python@v1
    with: 
      python-version: ${{ matrix.python-version }}
  - name: Install dependencies
    run: |
      python -m pip install --upgrade pip
      python -m pip install --user numpy scipy matplotlib
    - name: Test with unittest
      run: |
        python -m unittest
```

## Deploy

Next, deploy the package.  
* [example](https://packaging.python.org/tutorials/packaging-projects/)

## References

* GitHub Actions for Python [documentation](https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions)
* [PrajjawalBanati](https://github.com/PrajjawalBanati/Python-actions)
* [RealPython](https://realpython.com/python-continuous-integration/)
* [YouTube GitHub Actions with CI/CD](https://youtu.be/E1OunoCyuhY) by Nat Friedman (GitHub CEO), Jeremy Epling (GitHub Developer), and clients, on Aug 8, 2019.

