from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("fibonacci_cy.pyx", language_level=3))
