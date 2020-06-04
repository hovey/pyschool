"""
Implements View
"""
from pubsub.isubscriber import ISubscriber


class View(ISubscriber):
    def __init__(self):
        super().__init__
        print('View.__init__()')

    def serialize(self):
        print('View.serialize()')
