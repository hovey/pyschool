"""
Implements ISubscriber
"""

from abc import ABC, abstractmethod

import numpy as np


class ISubscriber(ABC):
    """ The Interface class for subscribers. """
    def __init__(self):
        """ The init method of the ISubscriber class. """
        super().__init__()

    @abstractmethod
    def create(self):
        """ Update is CRUD-style callback that publishers will trigger. """
        pass

    @abstractmethod
    def read(self):
        """ Update is CRUD-style callback that publishers will trigger. """
        pass
