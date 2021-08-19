"""
This module defines the square.Model class
"""

from model_base import Shape


class Model(Shape):
    """
    The square.Model class defines a square
    """

    def __init__(self, **kwargs):
        """
        The init method of the square.Model class

        Args:
            **kwargs (**dict): The config parameters of the square
        """
        super().__init__(**kwargs)

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            area (float): The area of the shape
        """
        return self._shape_params["side_length"] ** 2
