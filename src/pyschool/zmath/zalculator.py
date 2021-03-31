"""This module is the Zalculator service."""


class Zalculator:
    """The Zalcuator provide fundamental mathematical calculation.

    This module is used for testing of initial wheel file deployment, pyschool library
    imports, and pytest functionality."""

    def __init__(self):
        self.initialized = False
        print("The Zalculator is initialized.")
        self.initialized = True

    def add(self, x, y):
        """Returns the sum of two numbers x and y."""
        return x + y

    def subtract(self, x, y):
        """Returns the value of number x less number y."""
        return x - y
