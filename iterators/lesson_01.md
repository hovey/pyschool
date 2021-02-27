# Iterators

## Lesson

A Python iterator is an object with number of items that can be counted.
For example, a list containing the make of a three vehicles is an iterator
because it contains items that are countable.

```python
vehicle_types_list = ["Chevy", "Ford", "Chrysler"]
```

A common pattern is to traverse items such as lists.  In older languages, such as FORTRAN or C, traversal was done through and index, and can be done in Python with an index as well:

```python
# Before
print("The cars we have for sale today are:")
i = 0  # index
for i in range(0, len(vehicle_types_list)):
    print(f"  {vehicle_types_list[i]}")
    i += 1
```

A much better way to traverse lists in Python is with iterators.
Iterators make the come more readable and compact.

```python
# After
print("The cars we have for sale today are:")
for vehicle in vehicle_types_list:
    print(f"  {vehicle}")
```

## Practice

Try it on your own.  Copy paste the code below, 

```python
vehicle_types_list = ["Chevy", "Ford", "Chrysler"]

# Before
print("The cars we have for sale today are:")
i = 0  # index
for i in range(0, len(vehicle_types_list)):
    print(f"  {vehicle_types_list[i]}")
    i += 1

# After
print("The cars we have for sale today are:")
for vehicle in vehicle_types_list:
    print(f"  {vehicle}")
```

into a Python file of our own, or run the file in web service, such as [W3 Schools](https://www.w3schools.com/python/trypython.asp?filename=demo_default).

Additional reading on iterators:
* [Python Practice Book](https://anandology.com/python-practice-book/iterators.html#iterators)
* [Python Tutorial: Introduction to iterators](https://youtu.be/jHcSzgu9JLY)