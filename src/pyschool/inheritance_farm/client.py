#!/usr/bin/env python
# client
# from animal import *
# from animal_factory import *
import animal_factory as af

af_instance = af.Animal_Factory()
animals = []  # collection of animals

animals.append(af_instance.create_animal("dog", "Sam"))
animals.append(af_instance.create_animal("dog", "Mambo"))
animals.append(af_instance.create_animal("goat", "Julia"))
animals.append(af_instance.create_animal("goat", "Lucy"))

for animal in animals:
    animal.speak()
    animal.say_name()
