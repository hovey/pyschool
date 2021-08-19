"""
This module demonstrates how to do unit testing in python.
Run with

$ python -m unittest test_unittest.py

Alternatively,

$ python -m unittest 
runs all files that start with "test" in the current directory
"""

import unittest
from unittest.mock import patch, mock_open
import json


def load_json(file_loc):
    """
    This function loads the json file into a dictionary

    :param file_loc: The location of the json file
    :type file_loc: str

    :returns config: The configuration parameters from the json file
    :type config: dict
    """

    with open(file_loc, 'r') as fin:
        config = json.load(fin)

    return config


class TestLoadJSON(unittest.TestCase):
    """
    This class defines a unit test for ensuring that the JSON file is
    properly loaded by load_json
    """

    # patch makes a name temporarily point to another one. In this case,
    # when we use builtins.open, we instead call the patched function
    # mock_open. mock_open is passed the parameter read_data, which is
    # a string that can be read by the python function .read().
    # json.dumps converts the given dictionary to a JSON string
    # representation for use with read_data. 
    @patch('builtins.open',
           new_callable=mock_open,
           read_data=json.dumps(
                {
                    'spam': 'why do we use this?',
                    'eggs': 'but really',
                    'ham': {
                        'foo': 'This is more reasonable'
                    }
                }
           ))
    def test_load_json(self, mock_data):
        """
        Test loading the data
        """
        expected_output = {'spam': 'why do we use this?',
                           'eggs': 'but really',
                           'ham': {
                                'foo': 'This is more reasonable'
                           }
                          }

        # As we patched mock_open(read_data) for open(file_loc) earlier,
        # when load_json calls
        # with open(file_loc, 'r') as fin:
        #       config = json.load(fin)
        # it is actually doing
        # with patch('builtins.open', mock_open(read_data)) as m:
        #       with open(file_loc, 'r') as fin:
        #            config = json.load(fin)
        file_loc = 'this/is/a/dummy/location/data.json'
        actual_output = load_json(file_loc)

        # Make sure that we called open(file_loc, 'r')
        mock_data.assert_called_with(file_loc, 'r')

        # Make sure that the expected and actual outputs match
        self.assertEqual(expected_output, actual_output)
