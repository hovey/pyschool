"""
Implements the IPublisher interface
"""
from pubsub.ipublisher import PublisherBase


class Newspaper(PublisherBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Newspaper.__init__() for {self.name}')
