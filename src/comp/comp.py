# The following list comprehension exercises will make use of the
# defined Human class.
import math


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for human in humans:
    if human.name.startswith('D'):
        a.append(human.name)


print(a)

# here is list comp method

print("Starts with D:")
a = [human.name for human in humans if human.name.startswith("D")]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []

for human in humans:
    if human.name.endswith('e'):
        b.append(human.name)
print(b)

# list comp method:

print("Ends with e:")
b = [human.name for human in humans if human.name.endswith("e")]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []

letters = ['C', 'D', 'E', 'F', 'G']
for human in humans:
    if human.name[0] in (letters):
        c.append(human.name)

print(c)

# list comp method:

print("Starts between C and G, inclusive:")
c = [human.name for human in humans if any(human.name.startswith(x) for x in "CDEFG")]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []

for human in humans:
    d.append(human.age + 10)

print(d)

# list comp method:

print("Ages plus 10:")
d = [human.age + 10 for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []

for human in humans:
    e.append(human.name + '-' + str(human.age))

print(e)

# list comp method:

print("Name hyphen age:")
e = [human.name + "-" + str(human.age) for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []

for human in humans:
    if human.age >= 27 and human.age <= 32:
        f.append((human.name, human.age))

print(f)

# list comp method:

print("Names and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if human.age in range(27, 33)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []

for human in humans:
    new_human = Human(human.name.upper(), human.age + 5)
    g.append(new_human)

print(g)

# list comp method:

print("All names uppercase:")
g = [Human(human.name.upper(), human.age + 5) for human in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = []

for human in humans:
    h.append(math.sqrt(human.age))

print(h)

# list comp method:

h = [math.sqrt(human.age) for human in humans]
print(h)
