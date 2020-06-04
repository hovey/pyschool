"""
Implements Model
"""
from pubsub.isubscriber import ISubscriber


class Model(ISubscriber):
    def __init__(self):
        super().__init__
        print('Model.__init__()')

    def serialize(self):
        print('Model.serialize()')
