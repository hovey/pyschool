"""
Implements the ISubscriber interface
"""
from pubsub.isubscriber import SubscriberBase


class Lectiophile(SubscriberBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f"Lectiophile.__init__() for {self.name}")
