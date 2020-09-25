import unittest
from .zmath import zalculator

class MyTestCase(unittest.TestCase):
    """
    This is the unittest script.
    To test on command line:
    $ cd ~/pyschool
    $ python -m unittest -v cont_integ/test_calculator.py
    """
    def test_add(self):
        total=zalculator.add(4,5)
        assert total==9
