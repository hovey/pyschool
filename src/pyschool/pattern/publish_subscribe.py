"""
The module implements the Publish-Subscribe pattern.

This is the `pubsub push` pattern implementation.  See references, below, for context.
The Publisher notifies Subscribers via a callback method.

Example:
    To come.

.. _Publish-Subscribe reference:
   https://github.com/hovey/pyschool/blob/f3a60800386c0416af4f129671ef1240cf75ff7b/pubsub/README.md
"""

from abc import ABC, abstractmethod
from typing import NamedTuple

# import numpy as np


class Subscriber(ABC):
    """The base class Subscriber for the Publish-Subscribe pattern.

    Classes should inherit from this base class to receive the
    subscribe mechanism of the publish-subscribe pattern.
    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def publication_callback(self, *, message: str = ""):
        """The callback method called by a Publisher.  Descendants must implement this
        method to inherit from `Subscriber`.

        Keyword Arguments:
            message (string): The publication as a message string from the publisher to
            the subscriber via the callback contract.  Defaults to `""` (empty string).
        """
        pass


class ConcreteSubscriber(Subscriber):
    """This class is included as an example of how Subscriber descendants
    could be implemented.
    """

    def __init__(self, *, name: str, verbose: bool = False):
        super().__init__()
        self.name = name
        self._verbose = verbose
        if verbose:
            print(f"ConcreteSubscriber {name} created.")

    def publication_callback(self, *, message: str) -> None:
        super().publication_callback(message=message)

        if self._verbose:
            print(f"-> Callback message: '{message}', received by {self.name}.")


class PublisherEvent(NamedTuple):
    subscribed: str = "subscribed event was triggered"
    unsubscribed: str = "unsubscribed event was triggered"
    publication: str = "Publication event was triggered."
    paused: str = "subscription was paused"
    resumed: str = "subscription was resumed"


class Publisher(ABC):
    """The base class Publisher for the Publish-Subscribe pattern.

    Classes should inherit from this base class to receive the
    publish mechanism of the publish-subscribe pattern.

    Attributes:
        _subscribers (dict[Subscriber: callback (str)]): Dictionary map with keys
            as Subscriber objects and values as the string callback methods
            implemented in the Subscriber descendant.  The callback string defaults
            to "update" if subscribers provide no callback method string.
    """

    def __init__(self):
        super().__init__()
        # self._subscribers = dict(Subscriber, bool)  # initialized as emtpy dictionary
        self._subscribers = dict()  # initialized as emtpy dictionary
        self.events = PublisherEvent()  # publisher establishes these event strings

    def subscribe(self, subscriber: Subscriber, active: bool = True) -> None:
        """Creates a subscription of the subscriber to a publisher.

        Arguments:
            subscriber (Subscriber): A subscriber of the publication.
            active (bool): If False, the subscriber's publications are paused.  If
                True, the subscriber's publications are resumed.  Defaults to True.
        """
        self._subscribers[subscriber] = active
        subscriber.publication_callback(message=self.events.subscribed)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        """Deletes a subscriber from a publisher's dictionary of subscribers.

        Arguments:
            subscriber (Subscriber): A subscriber of the publication.

        Raises:
            KeyError: if the subscriber is not in the publisher's dictionary of
                subscribers.
        """
        try:
            subscriber.publication_callback(message=self.events.unsubscribed)
            del self._subscribers[subscriber]
        except KeyError:
            print(f"Error: subscriber {subscriber} is unknown.")

    def publish(self, message: str = "") -> None:
        """Publishes a message (string) to subscribers via publish_callback function.

        This is the `push` implementation of the Publish-Subscribe pattern.
        """
        for subscriber, active in self._subscribers.items():
            if active:
                subscriber.publication_callback(message=message)

    def pause(self, subscriber: Subscriber) -> None:
        """Retains the connection between publisher and subscriber, but turns off
        notifications from the publisher to subscriber.  See also `resume` method.

        Arguments:
            subscriber (Subscriber): The subscriber for which updates should be
                paused until `resume` is used.

        Raises:
            KeyError: if the subscriber is not in the publisher's dictionary of
                subscribers.
        """
        try:
            self._subscribers[subscriber] = False  # subscription is paused
            subscriber.publication_callback(message=self.events.paused)
        except KeyError:
            print(f"Error: subscriber {subscriber} is unknown.")

    def resume(self, subscriber) -> None:
        """Retains the connection between publisher and subscriber, but turns on
        notifications from the publisher to subscriber.  See also `pause` method.

        Arguments:
            subscriber (Subscriber): The subscriber for which updates should be
                resumed until `pause` is used.

        Raises:
            KeyError: if the subscriber is not in the publisher's dictionary of subscribers.
        """
        try:
            self._subscribers[subscriber] = True  # subscription is resumed
            subscriber.publication_callback(message=self.events.resumed)
        except KeyError:
            print(f"Error: subscriber {subscriber} is unknown.")

    @property
    def subscribers(self) -> dict:
        """Returns the publisher's dictionary of current subscribers and their repective
        callbacks."""
        return self._subscribers
