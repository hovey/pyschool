import sys

import numpy as np


class Kinematics:
    def __init__(self, *, initial_position: np.ndarray, initial_velocity: np.ndarray):
        self._position = initial_position  # meters
        self._velocity = initial_velocity  # meters per second
        aa = 4

    @property
    def position(self) -> np.ndarray:
        return self._position

    @position.setter
    def position(self, val: np.ndarray):
        self._position = val

    @property
    def velocity(self) -> np.ndarray:
        return self._velocity

    @velocity.setter
    def velocity(self, val: np.ndarray):
        self._velocity = val

    def update_shows_bug(self, *, delta_t: float):
        # Tries to combine the getter and setter for self.position
        # with the += operator, which will not work.
        # Will cause this error:
        # Exception has occurred: _UFuncOutputCastingError
        # Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
        self.position += self.velocity * delta_t

    def update_fixes_bug(self, *, delta_t: float):
        # Fixes the bug exibited in the 'update_shows_bug' method.
        self._position = self.velocity * delta_t + self.position


def main(argv):

    # after an elapsed time of 2 seconds, calucate the new position
    dt = 2.0  # seconds, elapsed time step

    # construct a Kinematics object
    x0, y0 = 1000, 2000  # meters
    xdot0, ydot0 = 20, 30  # meters per second
    k1 = Kinematics(
        initial_position=np.array([x0, y0]), initial_velocity=np.array([xdot0, ydot0])
    )  # m and m/s
    k2 = Kinematics(
        initial_position=np.array([x0, y0]), initial_velocity=np.array([xdot0, ydot0])
    )  # m and m/s

    # expected updated position is rate * time + initial_position
    #
    # x-direction
    # = (20 m/s) * (2 s) + 1000 m
    # = 40 m + 1000 m
    # = 1040 m
    #
    # y-direction
    # = (30 m/s) * (2 s) + 2000 m
    # = 60 m + 2000 m
    # = 2060 m

    xf, yf = 1040, 2060  # meters

    k1.update_shows_bug(delta_t=dt)  # will trigger error
    new_position_with_bug = k1.position
    assert new_position_with_bug[0] == xf  # meters, succeeds
    assert new_position_with_bug[1] == yf  # meters, succeeds

    k2.update_fixes_bug(delta_t=dt)
    new_position_without_bug = k2.position
    assert new_position_without_bug[0] == xf  # meters, succeeds
    assert new_position_without_bug[1] == yf  # meters, succeeds
    aa = 4


if __name__ == "__main__":
    main(sys.argv[1:])
