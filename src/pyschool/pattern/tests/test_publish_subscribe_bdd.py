from pytest_bdd import scenario, given, when, then

from pyschool.pattern.publish_subscribe import (
    Publisher,
    PublisherEvent,
    ConcreteSubscriber,
)


@scenario("publisher.feature", "A Publisher is constructed")
def test_publisher_construction():
    pass


@scenario("publisher.feature", "The Publisher subscribes a Subscriber")
def test_publisher_subscribes_subscriber():
    pass


@scenario("subscriber.feature", "A Subscriber is constructed")
def test_subscriber_construction():
    pass


@given("A new Publisher", target_fixture="publisher")
def create_a_publisher():
    return Publisher()


@given("A new Subscriber named Annie", target_fixture="subscriber")
def create_a_subscriber_annie():
    return ConcreteSubscriber(name="Annie")


@when("The Publisher subscribes Annie")
def publisher_subscribes_annie(publisher, subscriber):
    publisher.subscribe(subscriber=subscriber)


@then("The Publisher has no subscribers")
def publisher_has_no_subscriber(publisher):
    assert len(publisher._subscribers) == 0


@then("The Publisher has a PublisherEvent")
def publisher_has_publisherevent(publisher):
    assert isinstance(publisher.events, PublisherEvent)


@then("The Publisher has a Subscriber named Annie")
def publisher_has_annie_subscriber(publisher):
    assert any([sub.name == "Annie" for sub in publisher._subscribers])


@then("The Subscriber is named Annie")
def subscriber_named_annie(subscriber):
    assert subscriber.name == "Annie"
