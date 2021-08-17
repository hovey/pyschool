#!/usr/bin/env python3
"""Example of a simple Maybe functor"""

from typing import Any


class Just:
    """Holds a value."""

    def __init__(self, value):
        self.value = value

    def __call__(self) -> Any:
        """Return value wrapped by Just."""
        return self.value if not callable(self.value) else self.value()

    def fmap(self, f) -> Any:
        """Execute f on self.value."""
        return Just(f(self.value))

    def __repr__(self):
        """Repr method."""
        return f"Just({self.value})"


class Nothing:
    """Holds no value."""

    def __init(self, value):
        pass

    def __call__(self) -> Any:
        """Return None."""
        return None

    def fmap(self, f) -> Any:
        """Return Nothing."""
        return Nothing()

    def __repr__(self):
        """Repr method."""
        return "Nothing()"


class Maybe:
    """Maybe holds a value."""

    def __init__(self, value):
        self.value = Just(value) if value else Nothing()

    def __call__(self) -> Any:
        """Return value."""
        return self.value()

    def fmap(self, f) -> Any:
        """Execute f on self.value."""
        return Maybe(self.value.fmap(f))

    def __repr__(self):
        """Repr method."""
        return str(self.value)


if __name__ == "__main__":
    # If x
    value = [2, 3]
    maybe_value = Maybe(value)
    maybe_value = maybe_value.fmap(sum)  # Just(Just(5))
    print(maybe_value())  # 5

    # If not x
    value = None
    maybe_value = Maybe(value)
    maybe_value = maybe_value.fmap(sum)  # Just(Nothing())
    print(maybe_value())  # None
