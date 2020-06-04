"""
Implements View
"""
from pubsub.isubscriber import SubscriberBase


class View(SubscriberBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('View.__init__()')
        # _kwargs = kwargs

    def serialize(self):
        print('View.serialize()')

    def update(self, message):
        print('View.update()')