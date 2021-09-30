"""Test the Ship class."""

from pytest_bdd import scenario, given, when, then


from pyschool.bdd.ship import Ship


@scenario("ship.feature", "A ship is hit")
def test_ship_hit():
    pass


@scenario("ship.feature", "A ship is missed")
def test_ship_missed():
    pass


@scenario("ship.feature", "A ship is killed")
def test_ship_killed():
    pass


@given("A ship", target_fixture="ship")
def a_ship():
    return Ship(start=(0, 0), end=(1, 3))


@given("The ship is nearly dead")
def a_ship_is_nearly_dead(ship):
    ship._hit_map[(0, 1)] = True
    # ship._hit_map[(0, 2)] = True


@when("The ship is hit")
def the_ship_is_hit(ship):
    ship.guess((0, 0))


@when("The ship is missed")
def the_ship_is_missed(ship):
    ship.guess((10, 10))


@then("The ship has been hit")
def the_ship_has_been_hit(ship):
    assert ship._hit_map[(0, 0)]


@then("The ship has been missed")
def the_ship_has_been_missed(ship):
    assert not any(list(ship._hit_map.values()))


@then("The ship is dead")
def the_ship_is_dead(ship):
    assert not ship.is_dead
