# This lesson demonstrates comparison of two lists to produce a third list
# containing True and False values to indicate presence of items in both
# of the original two lists.

# Skills: lists, list comprehension

# There are three students, Alice, Bob, Cali, enrolled in the
# Python course. The teacher of the course has a roster of the first names:
roster = ["Alice", "Bob", "Cali"]
print(f"The roster of students: {roster}")

# The teacher takes attendance, with the following students present:
attendance = ["Alice", "Cali"]
print(f"The students currently in attendance: {attendance}")

# The teacher compares the list of present students to the roster:
present = [item in attendance for item in roster]
print(f"The roster converted to a Boolean list: {present}")
