"""The general Animal class, and the specific Animal descendants."""


import abc


class Animal:
    """The abstract Animal class."""

    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def speak(self):
        """A generic speak method."""
        print("I am an abstract animal.")

    def say_name(self):
        """A greeting that announces one's name."""
        sentence = f"My name is {self.name}."
        print(sentence)


class Dog(Animal):
    """A specific Dog type of animal."""

    def speak(self):
        print("Bark! Bark! I am a dog.")


class Goat(Animal):
    """A specific Goat type of animal."""

    def speak(self):
        print("Baa! Baa! I am a goat.")
