# from animal import *
import animal as ani


class Animal_Factory:
    def create_animal(self, animal_type, name):

        if animal_type == "none":

            return ani.Animal(name)

        elif animal_type == "dog":

            return ani.Dog(name)

        elif animal_type == "goat":

            return ani.Goat(name)

        else:

            print("error: unknown animal type.")
