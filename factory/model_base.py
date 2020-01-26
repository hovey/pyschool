"""
This module defines Shape, the abstract base class for the models
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    The Shape class is the abstract base class for all shapes

    Attributes:
        _shape_params (dict): The attributes representing the shape
    """
    def __init__(self,
                 **kwargs):
        """
        The init method of the Shape class

        Args:
            **kwargs (**dict): The kwargs defining the shape
        """
        self._shape_params = kwargs

    @abstractmethod
    def area(self):
        """
        Calculates and returns the area of the shape

        Returns:
            area (float): The area of the shape
        """
        pass
