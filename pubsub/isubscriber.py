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
    def serialize(self):
        """ Update is CRUD-style callback that publishers will trigger. """
        pass

    @abstractmethod
    def update(self, message):
        """ Update is CRUD-style callback that publishers will trigger. """
        pass

class SubscriberBase(ISubscriber):
    def __init__(self, **kwargs):
        super().__init__
        print('MVC_Base.__init__()')
        self._kwargs = kwargs

    def serialize(self):
        print('MVC_Base.serialize()')

    def update(self, message):
        print('MVC_Base.update()')

    @property
    def the_kwargs(self):
        return self._kwargs