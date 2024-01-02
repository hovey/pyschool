"""This module creates animal objects."""

import animal as ani


class AnimalFactory:
    """Creates animal objects."""

    def create_animal(self, animal_type, name):
        """Creation method for animals."""

        # Use Pattern Matching, implemented in Python 3.10
        # https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching

        match animal_type:
            case "none":
                return ani.Animal(name)
            case "dog":
                return ani.Dog(name)
            case "goat":
                return ani.Goat(name)
            case _:
                print("error: unknown animal type.")
