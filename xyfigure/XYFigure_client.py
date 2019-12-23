#!/usr/bin/env python
# Client to create figures for Military Specification journal manuscript.
# To run from command line with Python3:
# [base_directory]: $ python XYFigure.py

import os
import sys
import json
# import numpy as np
# import matplotlib.pyplot as plt
# from abc import ABC
# from datetime import datetime
from XYFigure import XYFactory, XYModel, XYView


def main(argv):
    """Client to generate a XYFigure from an 'input.json' file.

    $ module load anaconda3
    $ python XYFigure_client.py <input_file>.json

    where <input_file>.json holds the database of XYFigure objects to create.
    """

    help_string = '$ python XYFigure_client.py  <input_file>.json'
    try:
        input_file = argv[0]
    except IndexError as error:
        print(f'Error: {error}.')
        print('check script pattern: ' + help_string)
        print('Abnormal script termination.')
        sys.exit('No input file specified.')
    home = os.getcwd()

    with open(input_file) as f:
        database = json.load(f)

    items = []  # cart of items is empty, fill from factory
    # factory = XYFactory()  # it's static!

    for item in database:
        kwargs = database[item]
        # i = factory.create(item, kwargs)  # it's static!
        folder = kwargs['folder']
        try:
            os.chdir(folder)
        except FileNotFoundError:
            print(f'Folder needed but not found: "{folder}"')
            val = input('Create folder? [y]es or [n]o : ')
            if val == 'y':
                os.mkdir(folder)
                print(f'Created folder: "{folder}"')
            else:
                print('Check accuracy of folders in database.')
                print('Abnormal script termination.')
                sys.exit('Folder misspecified.')
        i = XYFactory.create(item, **kwargs)
        if i:
            items.append(i)
        else:
            print('Item is None from factory, nothing added to Client items.')
        os.chdir(home)

    models = [i for i in items if isinstance(i, XYModel)]
    views = [i for i in items if isinstance(i, XYView)]

    for view in views:
        view.models = models  # register models with views
        view.figure()  # changes cwd to 'output'
        os.chdir(home)

    print('End of client execution.')

if __name__ == '__main__':
    main(sys.argv[1:])
