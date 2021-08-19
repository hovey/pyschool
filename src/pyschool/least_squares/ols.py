#!/usr/bin/env python
import os
import sys
import numpy as np
from numpy.linalg import inv
from numpy.linalg import cond
from numpy.linalg import norm


def main(argv):

    help_string = "./ols.py <input_folder/>"

    try:
        input_folder = argv[0]
    except:
        print("Error: no input folder target specified.")
        print("Check script pattern: " + help_string)
        return  # early return because no target folder specified

    input_file = "input.csv"  # schema requirement

    print(f"Searching for input folder: {input_folder}")
    if os.path.isdir(input_folder):
        print("Success: folder exists.")
    else:
        print("Error: folder does not exist.")
        return  # early return because folder does not exist

    os.chdir(input_folder)
    print(f"Searching for input file: {input_folder}{input_file}")
    if os.path.isfile(input_file):
        print("Success: file exists.")
    else:
        print("Error: file does not exist.")
        return  # early return because file does not exist

    n_header_rows = 1  # number of header rows to be skipping when reading input

    input_table = np.genfromtxt(
        "input.csv", dtype="float", delimiter=",", skip_header=n_header_rows
    )

    print("Input data table:")
    print(input_table)

    x = input_table[:, 0]
    print(f"x = {x}")
    y = input_table[:, 1]
    print(f"y = {y}")
    b = input_table[:, 2]
    print(f"b = {b}")

    n = 2  # number of unknowns, harded coded in this ordinary least squares example
    print(f"Number of unknowns = {n}")

    m = len(x)
    print(f"Number of equations = {m}")

    if m == n:
        print("Problem is exactly constrained.")
    elif m > n:
        print("Problem is over-constrained, will perform ordinary least squares fit.")
    else:
        print(
            "Error: Problem is under-constained, rank is not sufficient for solution."
        )
        return  # early return because folder does not exist

    A = np.zeros((m, n))  # target left-hand-size matrix in Ax = b
    A[:, 0] = x
    A[:, 1] = y
    print(f"A matrix = {A}")

    A_star = np.dot(A.transpose(), A)
    print(f"A* = A^T A = {A_star}")

    b_star = np.dot(A.transpose(), b)
    print(f"b* = A^T b = {b_star}")

    x_star = np.dot(inv(A_star), b_star)
    print(f"x* = {x_star}")


if __name__ == "__main__":
    main(sys.argv[1:])
