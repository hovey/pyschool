"""
This module defines the circle.Model class
"""

from model_base import Shape
import math


class Model(Shape):
    """
    The circle.Model class defines a circle
    """
    def __init__(self, **kwargs):
        """
        The init method of the circle.Model class

        Args:
            **kwargs (**dict): The config parameters of the circle
        """
        super().__init__(**kwargs)

    def area(self):
        """
        Calculates and returns the area of the circle

        Returns:
            area (float): The area of the shape
        """
        return math.pi * self._shape_params['radius']**2
