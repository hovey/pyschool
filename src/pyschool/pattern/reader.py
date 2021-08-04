"""This module demonstrates the command line reading of .json and .yml file types.

Example:
> cd ~/pyschool/src/pyschool/pattern
> conda activate pyschoolenv
# either
> python reader.py data/input_example.json
# or
> python reader.py data/input_example.yml
"""

from pathlib import Path
import sys
import json
import yaml


def main(argv):

    engine_file = __file__
    print(f"Engine: {engine_file}.")

    has_database = False  # default, the database not yet populated from file input

    # path_file_in = Path(argv[0])
    path_file_in = Path(argv[0]).resolve()
    # file_stem = path_file_in.stem  # returns "input_example" from "input_example.json"
    file_type = path_file_in.suffix  # returns "json" from "input_example.json"

    if not path_file_in.is_file():
        raise OSError(f"File not found: {path_file_in}")

    file_type = path_file_in.suffix

    if file_type not in [".json", ".yml"]:
        raise TypeError("Only file types of .json or .yml are supported.")

    if file_type == ".json":
        with open(path_file_in) as fin:
            database = json.load(fin)
    else:  # then file type necessarily must be .yml
        with open(path_file_in, "r") as stream:
            database = yaml.safe_load(stream)

    print(f"Input: {path_file_in}")
    print("The first level key and value pairs follow:")
    for key, value in database.items():
        # for item in data:
        print(f"key is '{key}' -> value is '{value}'")

    has_database = True  # overwrite default False state, database now populated
    return has_database


if __name__ == "__main__":
    main(sys.argv[1:])
