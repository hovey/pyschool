"""
This module tests the Publish-Subscribe pattern.

Example:
    > conda activate pyschool-env
    > pytest src/pyschool/pattern/tests/test_publish_subscribe.py -rP
"""

# import pytest

from pyschool.pattern.publish_subscribe import Publisher, ConcreteSubscriber


def test_publisher_constructor():
    pub = Publisher()
    assert pub
    assert isinstance(pub, Publisher)


def test_publisher_init_empty_subscribers():
    pub = Publisher()
    subs = pub.subscribers
    assert isinstance(subs, dict)
    assert len(subs) == 0  # empty dictionary


def test_subscriber_constructor():
    sub = ConcreteSubscriber(name="Example Name", verbose=True)
    assert sub
    assert isinstance(sub, ConcreteSubscriber)


def test_pub_sub_scenario():
    """
    Example:
        > cd ~/codebase
        > conda activate pysnrl-env
        > pytest pysnrl/simulation/entity/test_publish_subscribe.py::test_pub_sub_scenario -rP
    """
    verbosity = True  # manual on/off switch for manual testing for now
    pub = Publisher()  # a single publisher of newspapers

    # A subscriber Annie
    annie = ConcreteSubscriber(name="Annie", verbose=verbosity)
    pub.subscribe(annie)

    # A subscriber Bobby
    bobby = ConcreteSubscriber(name="Bobby", verbose=verbosity)
    pub.subscribe(bobby)

    # Test that publisher's list of subscribers is Annie and Bobby
    assert all(
        [
            item in ["Annie", "Bobby"]
            for item in [subscriber.name for subscriber in pub.subscribers]
        ]
    )

    # Annie now ends her subscription.
    pub.unsubscribe(annie)

    # Test that publisher's list of subscribers is now just Bobby, not Annie
    assert all(
        [
            item in ["Bobby"] and item not in ["Annie"]
            for item in [subscriber.name for subscriber in pub.subscribers]
        ]
    )

    # Test if Annie unsubscribes a second time.  Publishers decline gracefully.
    pub.unsubscribe(annie)

    # A subscriber Cali
    cali = ConcreteSubscriber(name="Cali", verbose=verbosity)
    pub.subscribe(cali)

    # Subscriber test
    assert all(
        [
            item in ["Bobby", "Cali"]
            for item in [subscriber.name for subscriber in pub.subscribers]
        ]
    )

    # A subscriber Dalia
    dalia = ConcreteSubscriber(name="Dalia", verbose=verbosity)
    pub.subscribe(dalia)

    # Subscriber test
    assert all(
        [
            item in ["Bobby", "Cali", "Dalia"]
            for item in [subscriber.name for subscriber in pub.subscribers]
        ]
    )

    # Examine the publisher's current subscribers:
    if verbosity:
        subs = pub.subscribers
        for s in subs:
            print(f"{s.name} is a subscriber")

    # The publisher has a publication, so publish to subscribers.
    pub.publish(pub.events.publication)

    # Subscriber test, Cali stays a subscriber, just has a paused subscription
    assert all(
        [
            item in ["Bobby", "Cali", "Dalia"]
            for item in [subscriber.name for subscriber in pub.subscribers]
        ]
    )

    # Cali is going out of town, so pause her subscription.
    pub.pause(cali)

    # Confirm Cali does not receive publications during this pause time.
    pub.publish(pub.events.publication)

    # Annie tries to pause her subscription, even though she has already
    # unsubscribed twice!  Publishers decline gracefully.
    pub.pause(annie)

    # Cali returns home, so she resumes her subscription.
    pub.resume(cali)

    # Confirm Cali doees again receive publications.
    pub.publish(pub.events.publication)
