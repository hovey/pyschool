# for loop versus iterator (versus list comprehensions)
# https://medium.freecodecamp.org/python-list-comprehensions-vs-generator-expressions-cef70ccb49db
# Per https://www.quora.com/Why-are-list-comprehensions-faster-than-for-loops-in-Python,
# list comprehensions have better performance than for-loops when for-loops are used
# in conjunction with the append argument.

# globals
LIST_LEN = 6

# lists
# a collection of elements, elements can be any type, element do not need to be the same type
# use index to access a list element
list_from_for_loop = []
for x in range(LIST_LEN):
    list_from_for_loop.append(x ** 2)
print("List from a for loop:")
print(list_from_for_loop)

# list comprehension
# part of Python's functional programming, allows for list creation with
# less code than a for loop
list_from_comprehension = [x ** 2 for x in range(LIST_LEN)]
print("\nList from a comprehension:")
print(list_from_comprehension)

# check to see if any object is iterable using iter(),
# here we see a str object is iterable, but a bool object is not
print("\nTrue or False: a str object is iterable?")
print(hasattr(str, "__iter__"))

print("\nTrue or False: a bool object is iterable?")
print(hasattr(bool, "__iter__"))

print("\nTrue or False: a list_from_for_loop object is iterable?")
print(hasattr(list_from_for_loop, "__iter__"))

print("\nTrue or False: a list_from_comprehension object is iterable?")
print(hasattr(list_from_comprehension, "__iter__"))

a_list = ["a", 1, "1,", 50, "fifty"]
str_list = [item for item in a_list if isinstance(item, str)]
print("\nThis is str_list:")
print(str_list)

int_list = [item for item in a_list if isinstance(item, int)]
print("\nThis is int_list:")
print(int_list)
