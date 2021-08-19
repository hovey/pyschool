"""Test the BattleshipMap class."""

from pytest_bdd import scenario, given, when, then


from pyschool.bdd.battleship import BattleshipMap


@scenario("battleship_map.feature", "A game starts")
def test_game_startup():
    pass


@scenario("battleship_map.feature", "A call is right")
def test_ship_hit():
    pass


@scenario("battleship_map.feature", "A call is wrong")
def test_ship_missed():
    pass


@scenario("battleship_map.feature", "A ship is sunk")
def test_ship_sunk():
    pass


@scenario("battleship_map.feature", "All ships are sunk")
def test_game_over():
    pass


@given("A battleship board", target_fixture="board")
def board():
    return BattleshipMap()


@given("A ship that is nearly dead")
def a_ship_is_nearly_dead(board):
    board.ships[0]._hit_map[(0, 1)] = True
    board.ships[0]._hit_map[(0, 2)] = True


@given("The game is nearly over")
def the_game_is_nearly_over(board):
    for ship in board.ships:
        ship.is_dead = True

    board.ships[0].is_dead = False


@when("A correct hit is called")
def correct_hit(board):
    board.guess(coordinate=(0, 0))


@when("An incorrect hit is called")
def incorrect_hit(board):
    board.guess(coordinate=(10, 10))


@then("There are five ships")
def there_are_five_ships(board):
    assert len(board.ships) == 5


@then("A ship is hit")
def ship_is_hit(board):
    board.ships[0].is_hit


@then("No ship is hit")
def no_ship_is_hit(board):
    assert any([ship.is_hit for ship in board.ships])


@then("The ship is sunk")
def the_ship_is_sunk(board):
    assert board.ships[0].is_sunk


@then("The game is over")
def the_game_is_over(board):
    assert board.game_over
