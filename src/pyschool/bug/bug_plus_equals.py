import sys

import numpy as np


class Kinematics:
    def __init__(self, *, initial_position, initial_velocity):
        self._position = initial_position  # meters
        self._velocity = initial_velocity  # meters per second

    @property
    def position(self) -> float:
        return self._position

    @position.setter
    def position(self, val: float):
        self._position = val

    @property
    def velocity(self) -> float:
        return self._velocity

    @velocity.setter
    def velocity(self, val: float):
        self._velocity = val

    def update_shows_bug(self, *, delta_t: float):
        # Tries to combine the getter and setter for self.position
        # with the += operator, which will not work.
        self.position += self.velocity * delta_t

    def update_fixes_bug(self, *, delta_t: float):
        # Fixes the bug exibited in the 'update_shows_bug' method.
        self._position = self.velocity * delta_t + self.position


def main(argv):

    # after an elapsed time of 2 seconds, calucate the new position
    dt = 2.0  # seconds, elapsed time step

    # construct a Kinematics object
    k1 = Kinematics(initial_position=1000, initial_velocity=20)  # m and m/s
    k2 = Kinematics(initial_position=1000, initial_velocity=20)  # m and m/s

    # expected updated position is rate * time + initial_position
    # = (20 m/s) * (2 s) + 1000 m
    # = 40 m + 1000 m
    # = 1040 m

    k1.update_shows_bug(delta_t=dt)
    new_position_with_bug = k1.position
    assert new_position_with_bug == 1040  # m, fails

    k2.update_fixes_bug(delta_t=dt)
    new_position_without_bug = k2.position
    assert new_position_without_bug == 1040  # m, succeeds


if __name__ == "__main__":
    main(sys.argv[1:])
