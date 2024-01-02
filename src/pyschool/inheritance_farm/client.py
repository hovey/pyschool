"""The client general entry point to exercise the OOP style of Animals."""
import animal_factory as af

af_instance = af.AnimalFactory()
animals = []  # collection of animals

animals.append(af_instance.create_animal("dog", "Sam"))
animals.append(af_instance.create_animal("dog", "Mambo"))
animals.append(af_instance.create_animal("goat", "Julia"))
animals.append(af_instance.create_animal("goat", "Lucy"))

for animal in animals:
    animal.speak()
    animal.say_name()
