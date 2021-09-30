from typing import Iterable, Iterator, NamedTuple, Tuple, Union


# Reference: recursive type hinting:
# https://stackoverflow.com/questions/53845024/defining-a-recursive-type-hint-in-python
# Garthoks = Union[Garthok, Iterable['Garthoks']]
# and
# Forward references:
# https://www.python.org/dev/peps/pep-0484/#forward-reference
# Quads = Union[Iterable["Quads"], tuple[Quad, ...]]  # support for recursive type hint
# Meshes = Union[Iterable["Meshes"], tuple[Mesh, ...]]
# Ints = Union[Iterable["Ints"], Tuple[int, ...]]
# Ints = Union[Iterable["Ints"], "tuple[int, ...]"]
NestedInts = Union[Tuple[int], Iterable["NestedInts"]]
# NestedInts = Union[Tuple[int], Iterable[Tuple[int, ...]]]


class Coordinate(NamedTuple):
    """Creates a coordinate as a (x, y) pair of floats."""

    x: float  # x-coordinate
    y: float  # y-coordinate


class Cell:
    def __init__(self, *, center: Coordinate, size: float):
        self.center = center
        self.size = size

        self.west = center.x - size / 2.0
        self.east = center.x + size / 2.0
        self.south = center.y - size / 2.0
        self.north = center.y + size / 2.0

        self.has_children = False

    def divide(self):
        center_west_x = (self.center.x + self.west) / 2.0
        center_east_x = (self.center.x + self.east) / 2.0

        center_south_y = (self.center.y + self.south) / 2.0
        center_north_y = (self.center.y + self.north) / 2.0

        divided_size = self.size / 2.0

        self.sw = Cell(
            center=Coordinate(x=center_west_x, y=center_south_y),
            size=divided_size,
        )
        self.nw = Cell(
            center=Coordinate(x=center_west_x, y=center_north_y),
            size=divided_size,
        )
        self.se = Cell(
            center=Coordinate(x=center_east_x, y=center_south_y),
            size=divided_size,
        )
        self.ne = Cell(
            center=Coordinate(x=center_east_x, y=center_north_y),
            size=divided_size,
        )

        self.has_children = True  # overwrite from False in __init__

        print("Finished cell division.")


class Tree:
    def __init__(self, *, cell: Cell, level: int):
        self.cell = cell
        self.level = level

    def levels(self):
        _result = Tree._levels(cell=self.cell, level=0)
        return _result

    def levels_flattened(self):
        _input = self.levels()
        _result = tuple(Tree._levels_flatten(nested=_input))
        return _result

    @staticmethod
    def _levels(*, cell: Cell, level: int) -> NestedInts:
        # formerly def _quad_levels(*, cell: Cell, level: int):
        if cell.has_children:
            return (
                Tree._levels(cell=cell.sw, level=level + 1),
                Tree._levels(cell=cell.nw, level=level + 1),
                Tree._levels(cell=cell.se, level=level + 1),
                Tree._levels(cell=cell.ne, level=level + 1),
            )
        else:
            return (level,)
        # return (level,)

    @staticmethod
    def _levels_flatten(nested: NestedInts) -> Iterator[int]:
        # formerly def _tuple_flatten(nested) -> Iterable[int]:
        for i in nested:
            yield from [i] if isinstance(i, int) else Tree._levels_flatten(i)


def main():
    ctr = Coordinate(x=0.0, y=0.0)
    cell = Cell(center=ctr, size=2.0)
    # The cell divides the first time
    cell.divide()
    tree = Tree(cell=cell, level=0)

    found = tree.levels()
    known = ((1,), (1,), (1,), (1,))
    assert found == known

    found = tree.levels_flattened()
    known = (1, 1, 1, 1)
    assert found == known

    # The cell divides again
    # cell.sw.divide()
    # cell.nw.divide()
    # cell.se.divide()
    cell.ne.divide()
    tree = Tree(cell=cell, level=0)

    found = tree.levels()
    known = ((1,), (1,), (1,), ((2,), (2,), (2,), (2,)))
    assert found == known

    found = tree.levels_flattened()
    known = (1, 1, 1, 2, 2, 2, 2)
    assert found == known

    print("End of main.")


if __name__ == "__main__":
    main()
