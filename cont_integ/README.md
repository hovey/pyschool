# Continuous Integration

## Step-by-Step

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

    steps:
    - uses: actions/checkout@v2
    - name: Run a one-line script
      run: echo Hello, world!
    - name: Run a multi-line script
      run: |
        echo Add other actions to build,
        echo test, and deploy your project.
    - name: Test with Pytest
      run: |
		pip install pytest
        python -m pytest
```

## References

* [PrajjawalBanati](https://github.com/PrajjawalBanati/Python-actions)

