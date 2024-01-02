"""Recast OOP as FP with Python's single dispatch."""

from functools import singledispatch

from typing import NamedTuple


class Animal(NamedTuple):
    """A pseudo-abstract base class for Cat and Dog classes."""

    name: str
    id: int


class Cat(Animal):
    """A simple Cat that says 'meow'."""


class Dog(Animal):
    """A simple Dog that says 'bark'."""


@singledispatch
def speak(arg) -> None:
    """The generic form of the function to be overloaded."""
    _ = arg


# The overloaded functions
@speak.register
def _(x: Cat) -> None:
    "The Cat function is a little coy, compared with a Dog."
    print(f"Bonjour, you may call me {x.name}.")
    print("  Meow! Meow!. I am a cat.")


@speak.register
def _(x: Dog) -> None:
    """The Dog function is a little happier than a Cat."""
    print(f"Hola, nice to meet you, my name is {x.name}.")
    print("  Bark! Bark! I am a dog.")


# Client

a1 = Dog(name="Sam", id=1)
a2 = Dog(name="Mambo", id=2)
a3 = Cat(name="Julia", id=3)
a4 = Cat(name="Lucy", id=4)

animals = (a1, a2, a3, a4)

for animal in animals:
    speak(animal)
