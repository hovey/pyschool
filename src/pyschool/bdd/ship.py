"""Define the Ship class."""

from typing import Tuple


class Ship:
    """An entity on the game board that can be hit or sunk.

    Attributes:
        is_dead (bool): If True, the ship is dead. If False, the ship is not
            dead.
        is_hit (bool): If True, the ship has been hit. If False, the ship has
            not been hit.

    Keyword Arguments:
        start (Tuple[int, int]): The start coordinate of the ship.
        end (Tuple[int, int]): The end coordinate of the ship. Not inclusive.
    """

    def __init__(self, start: Tuple[int, int], end: Tuple[int, int]):
        self._hit_map = {}
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                self._hit_map[(i, j)] = False

        self._is_dead = False
        self.is_hit = False

    def guess(self, coordinate: Tuple[int, int]) -> bool:
        """Check if the ship has been hit.

        Arguments:
            coordinate (Tuple[int, int]): The guess against which to check
                if the ship has been hit.

        Returns:
            is_hit (bool): If True, the ship was hit. If False, the ship wasn't
                hit.
        """
        is_hit = (coordinate in self._hit_map) and not (
            self._hit_map.get(coordinate, False)
        )
        if is_hit:
            self._hit_map[coordinate] = True
            self.is_hit = True

    @property
    def is_dead(self) -> bool:
        """bool: If True, the ship is dead. If False, the ship is not dead."""
        if self._is_dead:
            return self._is_dead

        self._is_dead = all([is_hit for is_hit in self._hit_map.values()])

        return self._is_dead
