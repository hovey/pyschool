"""
This module defines the client-side script for the factory code
"""

import sys
import json
from view import View


def main(args):
    file_loc = args[0]

    with open(file_loc) as fin:
        config = json.load(fin)

    view = View(config)
    view.area()


if __name__ == '__main__':
    main(sys.argv[1:])