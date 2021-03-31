from unittest import TestCase, main

# from zfolder.zmath.zalculator import Zalculator as zcalc
# from zmath.zalculator import Zalculator as zcalc
# from zmath.code.zalculator import Zalculator as zcalc
from zmath.zalculator import Zalculator as zcalc


class TestZalculator(TestCase):
    """
    This is the unittest script.
    To test on command line:
    $ cd ~/pyschool
    either
    $ python -m unittest -v zmath/tests/test_zalculator.py
    or
    $ pytest zmath/tests/test_zalculator.py -v
    """

    def test_initialize(self):
        zc = zcalc()
        self.assertTrue(zc.initialized)

    def test_add(self):
        total = zcalc.add(self, 4, 5)
        self.assertEqual(total, 9)

    def test_subtract(self):
        total = zcalc.subtract(self, 10, 3)
        self.assertEqual(total, 7)


if __name__ == "__main__":
    main()  # calls unittest.test()
