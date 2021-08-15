"""This module tests the reader service.

To run
> conda activate pyschoolenv
> cd ~/pyschool
#
# pytest (without code coverage)
> pytest tests/test_reader.py -v
#
# pytest (with code coverage)
> pytest --cov=src/pyschool/pattern --cov-report term-missing
"""

import pytest

from pyschool.pattern import reader as rr


def test_input_file_not_found():

    argv = ["no_such_file.json"]

    with pytest.raises(OSError):
        _ = rr.main(argv)


def test_bad_input_file_type():

    argv = ["src/pyschool/pattern/data/input_example.csv"]

    with pytest.raises(TypeError):
        _ = rr.main(argv)


def test_argv_json():

    argv = ["src/pyschool/pattern/data/input_example.json"]
    assert rr.main(argv)


def test_argv_yml():

    argv = ["src/pyschool/pattern/data/input_example.yml"]
    assert rr.main(argv)
