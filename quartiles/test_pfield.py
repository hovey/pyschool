import os
import unittest
from quartiles import pfield as pf


class MyTestCase(unittest.TestCase):
    """
    This is the unittest of the pfield.py script.
    To test on command line:
    $ cd ~/pyschool
    $ python -m unittest -v quartiles/test_pfield.py
    """
    def test_input_folder_and_file(self):
        input_folder = 'quartiles/input'
        abs_path = os.path.join(os.getcwd(), input_folder)
        # print(f'Using absolute path: {abs_path}')
        # self.assertTrue(os.path.isdir(abs_path))
        # print(f'Searching for input folder: {input_folder}')

        # os.chdir(input_folder)
        os.chdir(abs_path)

        input_file = 'input.csv'  # scheme requirement
        # self.assertTrue(os.path.isfile(input_file)) # uncomment me
        self.assertFalse(os.path.isfile(input_file))  # planned fail for CI testing, delete me


    def test_constructor(self):
        pf_instance = pf.PostProcField('test_pfield')


    def test_quartiles(self):
        pf_instance = pf.PostProcField('test_pfield')
        a = [1, 2, 3, 4, 5]
        q = pf_instance.quartiles(a)
        # print('q = ' + str(q))
        self.assertEqual(q[0], 1)
        self.assertEqual(q[1], 2)
        self.assertEqual(q[2], 3)
        self.assertEqual(q[3], 4)
        self.assertEqual(q[4], 5)

        a = [20, 2, 7, 1, 34]
        q = pf_instance.quartiles(a)
        # print('q = ' + str(q))
        self.assertEqual(q[0], 1)
        self.assertEqual(q[1], 2)
        self.assertEqual(q[2], 7)
        self.assertEqual(q[3], 20)
        self.assertEqual(q[4], 34)

        # tests generated in Microsoft Excel
        a = [1, 2, 5, 5, 8, 9, 9, 10, 11, 11, 11, 13, 15, 17, 19, 20]
        q = pf_instance.quartiles(a)
        # print('q = ' + str(q))
        self.assertEqual(q[0], 1)
        self.assertEqual(q[1], 7.25)
        self.assertEqual(q[2], 10.5)
        self.assertEqual(q[3], 13.5)
        self.assertEqual(q[4], 20)

        # tests generated in Microsoft Excel
        a = [0.481595701, 0.194425009, 0.528469146, 0.430441936, 0.263365501, 0.420166117, 0.913818055, 0.827902698, 0.296218504, 0.958072785, 0.13239837]
        q = pf_instance.quartiles(a)
        # print('q = ' + str(q))
        tolerance = 0.000001
        self.assertLess(q[0] - 0.132398, tolerance)
        self.assertLess(q[1] - 0.279792, tolerance) 
        self.assertLess(q[2] - 0.430442, tolerance)
        self.assertLess(q[3] - 0.678186, tolerance)
        self.assertLess(q[4] - 0.958073, tolerance)


if __name__ == '__main__':
    unittest.main()

