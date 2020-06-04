"""
Implements Model
"""
from pubsub.isubscriber import SubscriberBase


class Model(SubscriberBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('Model.__init__()')
        # _kwargs = kwargs

    def serialize(self):
        print('Model.serialize()')

    def update(self, message):
        print('Model.update()')