"""Define the BattleshipMap class."""

from typing import List, Tuple

from pyschool.bdd.ship import Ship


class BattleshipMap:
    """A map on which ships are placed.

    Attributes:
        ships (List[Ship]): The ships on the map.
    """

    def __init__(self, board_size: int = 10):
        # Hardcoding this because it doesn't matter for this example
        # 5 ships, one of them at (0, 0), (0, 2)
        self.ships = [Ship(start=(5, 5), end=(8, 8)) for _ in range(4)]
        self.ships.insert(0, Ship(start=(0, 0), end=(1, 3)))

        self._game_over = False

    def guess(self, coordinate: Tuple[int, int]) -> bool:
        """Check that a ship is at the given coordinate and is hit.

        Arguments:
            coordinate (Tuple[int, int]): The guess against which to check
                if the ship has been hit.
        Returns:
            hit (bool): If True, a ship was hit. If False, a ship wasn't hit.
        """
        for ship in self.ships:
            if ship.guess(coordinate=coordinate):
                return True

        return False

    @property
    def game_over(self) -> bool:
        """bool: If True, the game is over. If False, the game is not over."""
        if self._game_over:
            return self._game_over

        self._game_over = all([ship.is_dead for ship in self.ships])

        return self._game_over
