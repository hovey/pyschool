# ctypes_test.py
import ctypes
import sys
import pathlib

"""
From:
https://realpython.com/python-bindings-overview/#calling-the-function

This will work for cases when the shared library is in the same directory as your
Python script, but be careful when you attempt to load libraries that are from packages
other than your Python bindings. There are many details for loading libraries and
finding paths in the ctypes documentation that are platform and situation-specific.

NOTE: Many platform-specific issues can arise during library loading. It's best to
make incremental changes once you get an example working.

Now that you have the library loaded into Python, you can try calling it!

Source code reference:
https://github.com/realpython/materials/blob/master/python-bindings/ctypes_c_test.py
"""


# def print(x, y, answer):
#
#     print(f"..    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
#     print("..")


if __name__ == "__main__":

    libname = pathlib.Path().absolute()
    libname_str = str(libname)
    print(f"libname: {libname_str}")

    # load the shared library into ctypes
    if sys.platform.startswith("win"):
        c_lib = ctypes.CDLL(libname_str / "cmult.dll")
    else:
        c_lib = ctypes.CDLL(libname_str / "libcmult.so")

    # sample data
    x, y = 6, 2.3

    # This will not work:
    # answer = c_lib.cmult(x, y)

    # This produces a bad answer:
    answer = c_lib.cmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
    print()

    # You need to tell ctypes that the function returns a float
    c_lib.cmult.restype = ctypes.c_float
    answer = c_lib.cmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
    print()
