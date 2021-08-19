Feature: Publisher
  An entity that pushes messages

  Scenario: A Publisher is constructed
    Given A new Publisher

    Then The Publisher has no subscribers
    And The Publisher has a PublisherEvent

  Scenario: The Publisher subscribes a Subscriber
    Given A new Publisher
    And A new Subscriber named Annie

    When The Publisher subscribes Annie

    Then The Publisher has a Subscriber named Annie
