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
    def update(self):
        """ The default callback method used by IPublisher interface.""" 
        pass

    @property
    @abstractmethod
    def update_count(self):
        """ (int) Returns the number of times a subscriber has 
        been updated by a publisher.  Useful to know if this number
        grows large, may suggest the subscriber is over-subscribered.
        """
        pass

class SubscriberBase(ISubscriber):
    def __init__(self):
        super().__init__
        print('SubscriberBase.__init__()')
        self._update_count = 0

    def serialize(self):
        print('SubscriberBase.serialize()')

    def update(self):
        self._update_count += 1
        print('SubscriberBase.update()')

    @property
    def update_count(self):
        return self._update_count