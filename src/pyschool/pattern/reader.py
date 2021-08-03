"""This module demonstrates the command line reading of .json and .yml file types.

Example:
> cd ~/pyschool/src/pyschool/pattern
> conda activate pyschoolenv
# either
> python reader.py -i data/input_example.json
# or
> python reader.py -i data/input_example.yml
"""

import argparse
from pathlib import Path
import sys


def main(argv):

    engine_file = __file__
    print(f"File name: {engine_file}.")

    # reference: https://www.golinuxcloud.com/python-argparse/
    parser = argparse.ArgumentParser()

    # reference:
    # https://docs.python.org/3/library/argparse.html#the-add-argument-method

    # default type is string
    parser.add_argument(
        "input_file",
        help="input file in .json or .yml format",
    )

    # verbosity
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )

    args = parser.parse_args()

    a = args.verbose
    b = args.input_file

    a = 4

    # if serialize:
    #     extension = ".png"  # ".pdf"  # or '.svg'
    #     bstring = Path(__file__).stem + extension
    #     # fig.savefig(bstring, bbox_inches="tight")
    #     fig.savefig(bstring, bbox_inches="tight", pad_inches=0)
    #     print(f"Serialized file to {bstring}")


if __name__ == "__main__":
    main(sys.argv[1:])
