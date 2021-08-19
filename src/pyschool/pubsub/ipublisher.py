"""
Implements IPublisher
"""

from abc import ABC, abstractmethod


class IPublisher(ABC):
    """The Interface class for publishers in the publish-subscribe design pattern."""

    def __init__(self, **kwargs):
        """The init method of the IPublisher class."""
        super().__init__()

    @abstractmethod
    def connect(self, ISubscriber, callback: str = None):
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
    def disconnect(self, ISubscriber):
        """
        Disconnects the subscriber from the publisher's subscriber list.
        """
        pass

    @abstractmethod
    def publish(self):
        """Notifes subscribers through a subscriber's callback."""
        pass

    @property
    @abstractmethod
    def name(self):
        """Returns the string name given to identify a class instance."""

    @property
    @abstractmethod
    def subscribers(self):
        """Returns a dictionary of the subscribers and callbacks."""
        pass

    @property
    @abstractmethod
    def subscriber_count(self):
        """(int) Returns the number of subscribers this publisher has."""
        pass


class PublisherBase(IPublisher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        _kwargs = kwargs
        self._name = kwargs.get("name", "Unknown Name")
        self._subscribers = dict()
        print(f"PublisherBase.__init__() for {self.name}")

    def connect(self, subscriber, callback: str = None):
        if callback == None:
            callback = "update"
        self._subscribers[subscriber] = callback

    def disconnect(self, subscriber):
        del self._subscribers[subscriber]

    def publish(self):
        for subscriber, callback in self._subscribers.items():
            method = getattr(subscriber, callback)
            method()

    @property
    def name(self):
        return self._name

    @property
    def subscribers(self):
        return self._subscribers

    @property
    def subscriber_count(self):
        return len(self._subscribers)
