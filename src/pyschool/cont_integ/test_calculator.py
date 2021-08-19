import unittest
from cont_integ import calculator


class MyTestCase(unittest.TestCase):
    """
    This is the unittest script.
    To test on command line:
    $ cd ~/pyschool
    $ python -m unittest -v cont_integ/test_calculator.py
    """

    def test_add(self):
        total = calculator.add(4, 5)
        assert total == 9

    def test_subtract(self):
        total = calculator.subtract(9, 5)
        assert total == 4

    def test_multiply(self):
        total = calculator.multiply(10, 3)
        assert total == 30

    def test_divide(self):
        total = calculator.divide(9, 3)
        assert total == 3
