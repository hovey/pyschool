Feature: Ship
  An entity on the game board that players try to hit.

  Scenario: A ship is hit
    Given A ship

    When The ship is hit

    Then The ship has been hit

  Scenario: A ship is missed
    Given A ship

    When The ship is missed

    Then The ship has been missed

  Scenario: A ship is killed
    Given A ship
    And The ship is nearly dead

    When The ship is hit

    Then The ship is dead
