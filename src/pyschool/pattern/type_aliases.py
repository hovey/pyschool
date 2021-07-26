# A case for type aliases

# A nice way to review this file is simply to debug it an step
# through code and the comments in order.

from math import cos, sin, pi
from typing import NamedTuple

import pytest


def main():

    """Type hinting helps users avoid errors by indicating to the
    linter data types and some data structure.

    Consider a function that take a pair value in polar coordinates,
    (r, theta) for radial and angular, respectively, and returns a pair
    value in Cartesian coordinates (x, y), easting and northing,
    respectively.

    We enforce keyword-only style of parameters as well, shown by the
    parameters that follow the "*" in the function signature.

    Example 0:
    """

    def polar_to_cartesian_0(*, point: tuple[float, float]) -> tuple[float, float]:
        r, theta = point
        x = r * cos(theta)
        y = r * sin(theta)
        return x, y

    """Let's first test this function on (r, theta) = (1.0, pi/6.0), which should
    give (x, y) = (0.866, 0.5).
    """
    x0, y0 = polar_to_cartesian_0(point=(1.0, pi / 6.0))

    tol = 0.001  # tolerance, some small number

    assert x0 == pytest.approx(0.866, tol)
    assert y0 == pytest.approx(0.5, tol)

    """Now let's use type aliases to make function signature more precise.
    Above, the input and return parameters are identical, but there is
    a semantic difference between the two pairs, one is in polar coordinates
    and the other is in Cartesian coordinates, and that is useful to communicate.

    Example 1:

    We define two type aliases as follows:
    """
    PolarCoordinate = tuple[float, float]
    CartesianCoordinate = tuple[float, float]

    """Then we make a new and improved function that uses these type alises.
    Notice that the implementation remains unchanged.
    """

    def polar_to_cartesian_1(*, point: PolarCoordinate) -> CartesianCoordinate:
        r, theta = point
        x = r * cos(theta)
        y = r * sin(theta)
        return x, y

    x1, y1 = polar_to_cartesian_1(point=(1.0, pi / 6.0))

    assert x1 == pytest.approx(0.866, tol)
    assert y1 == pytest.approx(0.5, tol)

    """Benefits: A type aliase improves precision in the function parameter
    types and an explicit semantic to communicate input types and outputs types.

    This is a fine starting point, but it could allow position-type
    errors, for example, if the user interchanged positions (r, theta) with
    (theta, r).  Type hinting would not provide help finding this bug, since
    both r and theta are of the same type.

    Example 2:

    Finally, a more robust function implementation can be made with NamedTuples.
    First, define a NamedTuple:
    """

    class PolarTuple(NamedTuple):
        r: float  # radius
        theta: float  # angle, in radians

    class CartesianTuple(NamedTuple):
        x: float  # easting
        y: float  # northing

    """Now make use of these new constructions.  Notice how their use becomes
    very explicit, and order of the tuple, e.g, (r, theta) versus (theta, r)
    errors are now more difficult to make.
    """

    def polar_to_cartesian_2(*, point: PolarTuple) -> CartesianTuple:
        r, theta = point.r, point.theta
        x = r * cos(theta)
        y = r * sin(theta)
        return CartesianTuple(x=x, y=y)

    point_in = PolarTuple(r=1.0, theta=pi / 6.0)

    point_out = polar_to_cartesian_2(point=point_in)

    assert point_out.x == pytest.approx(0.866, tol)
    assert point_out.y == pytest.approx(0.5, tol)

    """So the NamedTuples example, compared to the type alias example, shows
    increased explicitness.

    The type alias pattern may be prefered over the NamedTuple pattern if users
    do not need to be explicit about the data structure being used, e.g.,
    not need to use the `.x` and `.y` accessors of the NamedTuple.
    """


if __name__ == "__main__":
    main()
