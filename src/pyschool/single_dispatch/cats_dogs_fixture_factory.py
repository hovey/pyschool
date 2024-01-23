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
            db = yaml.safe_load(stream)  # overwrite empty dictionary

            if db.get("grayscale", False):
                # only a Cat type has a grayscale
                cc = Cat(
                    Trait(name=db["name"], language=db["language"]),
                    grayscale=db["grayscale"],
                )
                return cc
            elif db.get("red", False) and db.get("green") and db.get("blue"):
                # only a Dog has RGB values
                dd = Dog(
                    Trait(db["name"], language=db["language"]),
                    red=db["red"],
                    green=db["green"],
                    blue=db["blue"],
                )
                return dd
            else:
                raise ValueError(f"Unable to create a Dog or a Cat from spec {spec}.")

        except yaml.YAMLError as exc:
            print(exc)

    return None


@singledispatch
def paint(arg) -> None:
    """The generic form of a function to be overloaded."""
    _ = arg  # a no operation placeholder


# The overloaded functions
@paint.register
def _(x: Dog) -> None:
    """The paint function that operates on Dogs."""

    print(f"My name is {x.trait.name}")
    print(f"My language is {x.trait.language}")

    # This function makes calls to that are unique to the Dogs data structure.
    print(f"My colors are red: {x.red}, green: {x.green}, and blue: {x.blue}")


@paint.register
def _(x: Cat) -> None:
    """The paint function that operates on Cats."""

    print(f"My name is {x.trait.name}")
    print(f"My language is {x.trait.language}")

    # This function makes calls to that are unique to the Cats data structure.
    print(f"I have no colors, but my grayscale is {x.grayscale}")


# def test_factory_zoo(fido, selvester):
def test_factory_zoo(animals: tuple[Path, ...]) -> None:
    """Tests that both dogs and cats can be created from a generic
    animal.yml file."""

    # The client
    # A client orders from the Animal factory by providing two different
    # file specifications that consistent with the data type of objects the
    # factory can produce
    aa = [animal_factory(x) for x in animals]

    for a in aa:
        paint(a)

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
