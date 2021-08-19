Created: 2016-02-09
Updated: 2019-02-17

1. Get client into separate client.py code, get client.py to access animal.py
2. Abstract base class working (clients can't instantiate an ABC, e.g., animal)
3. Factory

basic template to demonstrate OOP in Python

sandbox
- area that small and tractable and can be used to demonstrate concepts
- not the "big" code

ABC - abstract base class
- all interface
- no implementation
- API, application program interface
- electrical outlet

animal
- dog
- goat

animal_factory (store)

client (farmer)

beauty of OOP
client (farmer) has a collection of animals, and asks them all to "speak"

API is just "speak()"

dog.speak() returns "bark"
goat.speak() returns "baa"

Other ideas:
FEA
client as graphics program
elements.draw()
elements themselves know how to draw themselves, the client need not know this.
