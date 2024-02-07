"""This module demonstrates a factory, which encapsulates RTTI and eliminates
the client-side RTTI burden.  The client need only to provide data structures
serialized to .yml files that can be built by the factory.  Python's built-in
single dispatch is used.  The factory uses 'match' (PEP 622 - Structural
Pattern Matching https://peps.python.org/pep-0622/) and therefore the module
requires Python 3.10 or greater.

cd ~/pyschool
source .venv/bin/activate.fish
cd src/pyschool/single_dispatch/
python cats_dogs_fixture_factory.py

Output:
My name is Fido.
My language is bark.
I have no grayscale, but my colors are red: 11, green: 22, and blue: 33.
My name is Sylvester.
My language is meow.
I have no colors, but my grayscale is 128.

References:

* Matt Wright, A Gentle Introduction to the Python Match Statement,
  https://www.wrighters.io/intro-to-python-match-statement/

"""

from functools import singledispatch
from pathlib import Path
from typing import NamedTuple

import pytest
import yaml


class Trait(NamedTuple):
    """A common trait to all animals, which have a name and a language."""

    name: str
    language: str


class Dog(NamedTuple):
    """The Dog type, which has unique data for red, blue, and green."""

    trait: Trait
    red: int
    green: int
    blue: int


class Cat(NamedTuple):
    """The Cat type, which has unique data for grayscale."""

    trait: Trait
    grayscale: int


@pytest.fixture
def fido() -> Path:
    """The Fido the dog yml file."""

    return Path(__file__).parent.joinpath("animal_fido.yml")


@pytest.fixture
def sylvester() -> Path:
    """The Selevester the cat yml file."""

    return Path(__file__).parent.joinpath("animal_sylvester.yml")


def animal_factory(spec: Path) -> Cat | Dog | None:
    """The animal factory, which returns either a Cat or a Dog"""

    # File IO, read in two yml files to create two databases
    with open(spec, "r", encoding="utf-8") as stream:
        try:
            db = yaml.safe_load(stream)

            # # Previous manner, without match of Python 3.10
            # # if db.get("grayscale", False):
            # if "grayscale" in db:
            #     # only a Cat type has a grayscale
            #     cc = Cat(
            #         Trait(name=db["name"], language=db["language"]),
            #         grayscale=db["grayscale"],
            #     )
            #     return cc
            # # elif db.get("red", False) and db.get("green") and db.get("blue"):
            # elif "red" in db and "green" in db and "blue" in db:
            #     # only a Dog has RGB values
            #     dd = Dog(
            #         Trait(db["name"], language=db["language"]),
            #         red=db["red"],
            #         green=db["green"],
            #         blue=db["blue"],
            #     )
            #     return dd
            # else:
            #     raise ValueError(f"Unable to create a Dog or a Cat from spec {spec}.")

            # New way, with match of Python 3.10
            match db:
                case {"grayscale": int(gg)}:  # only a Cat type has a grayscale
                    cc = Cat(
                        Trait(name=db["name"], language=db["language"]),
                        grayscale=gg,
                    )
                    return cc
                case {"red": int(rr), "green": int(gg), "blue": int(bb)}:
                    # only a Dog has RGB values
                    dd = Dog(
                        Trait(db["name"], language=db["language"]),
                        red=rr,
                        green=gg,
                        blue=bb,
                    )
                    return dd
                case _:
                    raise ValueError(
                        f"Unable to create a Cat or a Dog from spec {spec}."
                    )

        except yaml.YAMLError as exc:
            print(exc)

    return None


def name_and_trait(x: Cat | Dog) -> None:
    """Helper function to print item common to both a Cat and a Dog."""

    print(f"My name is {x.trait.name}.")
    print(f"My language is {x.trait.language}.")


@singledispatch
def paint(arg) -> None:
    """The generic form of a function to be overloaded."""
    _ = arg  # a no operation placeholder


# The overloaded functions
@paint.register
def _(x: Dog) -> None:
    """The paint function that operates on a Dog."""

    name_and_trait(x)

    # This function makes calls to that are unique to the Dog data structure.
    print(
        f"I have no grayscale, but my colors are red: {x.red}, green: {x.green}, and blue: {x.blue}.\n"
    )


@paint.register
def _(x: Cat) -> None:
    """The paint function that operates on a Cat."""

    name_and_trait(x)

    # This function makes calls to that are unique to the Cat data structure.
    print(f"I have no colors, but my grayscale is {x.grayscale}.\n")


# def test_factory_zoo(fido, selvester):
def test_factory_zoo(animals: tuple[Path, ...]) -> None:
    """Tests that both a Dog and a Cat can be created from a specific
    animal.yml file."""

    # The client
    # A client orders from the Animal factory by providing two different
    # file specifications that are consistent with the data type of objects the
    # factory can produce.
    aa = [animal_factory(x) for x in animals]

    for a in aa:
        paint(a)  # The magic of single dispatch occurs here!

    # manual tests
    assert isinstance(aa[0], Dog)  # is it a Dog
    assert not isinstance(aa[0], Cat)  # is it not a Cat

    assert not isinstance(aa[1], Dog)  # is it not a Dog
    assert isinstance(aa[1], Cat)  # is it a Cat


if __name__ == "__main__":
    p1 = Path(__file__).parent.joinpath("animal_fido.yml")
    p2 = Path(__file__).parent.joinpath("animal_sylvester.yml")
    items = tuple([p1, p2])
    # breakpoint()
    test_factory_zoo(items)
