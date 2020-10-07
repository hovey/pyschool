"""
Implements ISubscriber
"""

from abc import ABC, abstractmethod

import numpy as np


class ISubscriber(ABC):
    """ The Interface class for subscribers. """
    def __init__(self, **kwargs):
        """ The init method of the ISubscriber class. """
        super().__init__()

    @abstractmethod
    def update(self):
        """ The default callback method used by IPublisher interface.""" 
        pass

    @abstractmethod
    def serialize(self):
        """ An callback method alternative to the default 
        'update' method. """
        pass

    @property
    @abstractmethod
    def name(self):
        """ Returns the string name given to identify a class instance. """

    @property
    @abstractmethod
    def update_count(self):
        """ (int) Returns the number of times a subscriber has 
        been updated by a publisher.  Useful to know if this number
        grows large, may suggest the subscriber is over-subscribered.
        """
        pass

class SubscriberBase(ISubscriber):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        _kwargs = kwargs
        self._name = kwargs.get("name", "Unknown Name")
        self._update_count = 0
        print(f'SubscriberBase.__init__() for {self.name}')

    def serialize(self):
        print(f'SubscriberBase.serialize() for {self.name}')

    def update(self):
        self._update_count += 1
        print(f'SubscriberBase.update() for {self.name}')

    @property
    def name(self):
        return self._name

    @property
    def update_count(self):
        return self._update_count
