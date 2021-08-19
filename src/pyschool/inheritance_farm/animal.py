# from abc import ABCMeta
import abc


class Animal:

    __metaclass__ = abc.ABCMeta

    def __init__(self, name):

        self.name = name

    @abc.abstractmethod
    def speak(self):
        print("I am an abstract animal.")

    def say_name(self):
        sentence = f"My name is {self.name}."
        print(sentence)


# Dog class
class Dog(Animal):
    def speak(self):
        print("Bark! Bark! I am a dog.")


# Goat class
class Goat(Animal):
    def speak(self):
        print("Baa! Baa! I am a goat.")
