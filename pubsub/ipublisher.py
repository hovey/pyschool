"""
Implements IPublisher
"""

from abc import ABC, abstractmethod


class IPublisher(ABC):
    """ The Interface class for publishers in the publish-subscribe design pattern. """
    def __init__(self):
        """ The init method of the IPublisher class. """
        super().__init__()

    @abstractmethod
    def subscribe(self, ISubscriber, callback:str=None):
        """ 
        Connects the subscriber with the callback string, 
        which is the same as the subsriber's callback method. 

        If no callback is specified, then default callback 
        "update" is used.

        The ISubscriber interface requires implementation of 
        the "udpate" method.
        """
        pass

    @abstractmethod
    def unsubscribe(self, ISubscriber):
        """ 
        Disconnects the subscriber from the publisher's subscriber list. 
        """
        pass

    @abstractmethod
    def publish(self):
        """ Notifes subscribers through a subscriber's callback. """ 
        pass

    @property
    @abstractmethod
    def subscribers(self):
        """ Returns a dictionary of the subscribers and callbacks. """
        pass

    @property
    @abstractmethod
    def subscriber_count(self):
        """ (int) Returns the number of subscribers this publisher has.
        """
        pass

class PublisherBase(IPublisher):
    def __init__(self):
        super().__init__
        print('PublisherBase.__init__()')
        self._subscribers = dict()

    def subscribe(self, subscriber, callback:str=None):
        if callback == None:
            # callback = getattr(subscriber, 'update')
            callback = "update"
        self._subscribers[subscriber] = callback

    def unsubscribe(self, subscriber):
        del self._subscribers[subscriber]

    def publish(self):
        for subscriber, callback in self._subscribers.items():
            method = getattr(subscriber, callback)
            method()

    @property
    def subscribers(self):
        return self._subscribers

    @property
    def subscriber_count(self):
        return len(self._subscribers)
