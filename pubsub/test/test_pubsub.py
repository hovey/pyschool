# unittest for the publish-subscribe mechanism

from unittest import TestCase, main

from pubsub.ipublisher import PublisherBase
from pubsub.isubscriber import SubscriberBase


class TestPubSub(TestCase):

    def test_same(self):
        # The most basic of unit tests, should always run true and quickly.  
        self.assertTrue(1) 

    def test_empty_dict_on_startup(self):
        # nyt is short for New York Times
        nyt = PublisherBase()
        self.assertFalse(bool(nyt.subscribers)) # bool False is empty dictionary

    def test_pub_sub(self):
        # wsj is short for Wall Street Journal
        wsj = PublisherBase()
        Alice = SubscriberBase()
        Bob = SubscriberBase()

        self.assertEqual(wsj.subscriber_count, 0)
        wsj.connect(Alice)
        wsj.connect(Alice) # service should disallow mutiplie registers, this just overwrites same key
        wsj.connect(Bob, "serialize")  # Bob's callback is serialize, not update
        self.assertEqual(wsj.subscriber_count, 2)

        self.assertEqual(Alice.update_count, 0) # b 0 updates prior is first state
        self.assertEqual(Bob.update_count, 0)

        wsj.publish()

        self.assertEqual(Alice.update_count, 1) #  1 update after first publication 
        self.assertEqual(Bob.update_count, 0)  # Bob's update count is still 0 since he had a serialize callback

        wsj.disconnect(Alice)  # reduce the number of subscribers by 1
        self.assertEqual(wsj.subscriber_count, 1)


if __name__ == '__main__':
    main()  # calls unittest.main()