Feature: BattleshipMap
  The map for battleship

  Scenario: A game starts
    Given A battleship board

    Then There are five ships

  Scenario: A call is right
    Given A battleship board

    When A correct hit is called

    Then A ship is hit

  Scenario: A call is wrong
    Given A battleship board

    When An incorrect hit is called

    Then No ship is hit

  Scenario: A ship is sunk
    Given A battleship board
    And A ship that is nearly dead

    When A correct hit is called

    Then The ship is sunk

  Scenario: All ships are sunk
    Given A battleship board
    And The game is nearly over
    And A ship that is nearly dead

    When A correct hit is called

    Then The game is over
