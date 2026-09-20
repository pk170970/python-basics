import sys
print(sys.version)

#  python -m venv .venv    this can create a new virtual env
#  .\.venv\Scripts\activate this activates the environment
# above using venv is old way, new is using uv

# str = 'abc'
# str[0] = 'x'
# print(f"the str is {str}")

# names = ('ram', 'shyam')
# person1, person2 = names
# # names[0] = 'billa'
# print(person1 in names) # membership in python: checking whether element is present or not inside collection

# Swapping
# a,b = 1,2
# print(a,b)
# b,a = a,b
# print(a,b)

# List -> Mutable
# groceryList = ['tea', 'turmeric', 'suger', 'cardamom'];
# vegiesList = ['brinjal', 'tomato', 'onion']

# groceryList.extend(vegiesList) # merges vegies list into a grocery list
# print(f"total list is {groceryList}")

# print(groceryList.reverse())
# print(groceryList)


# Data types lesson
def show_type(name, value):
	print(f"{name}: {value} (type: {type(value).__name__})")


# 1. List: an ordered, changeable collection that allows duplicate values.
print("\n1. LIST")
fruits = ["apple", "banana", "apple"]
fruits[1] = "mango"  # Lists are mutable.
fruits.append("orange")
show_type("fruits", fruits)
print("First fruit:", fruits[0])


# 2. Tuple: an ordered, unchangeable collection that allows duplicates.
print("\n2. TUPLE")
coordinates = (10, 20, 10)
show_type("coordinates", coordinates)
print("Second coordinate:", coordinates[1])
# coordinates[0] = 99  # This raises TypeError because tuples are immutable.


# 3. Dictionary: a mutable collection of key-value pairs.
# Dictionary keys must be unique and hashable.
print("\n3. DICTIONARY")
student = {"name": "Asha", "age": 20, "subjects": ["Python", "Math"]}
student["age"] = 21
student["city"] = "Delhi"
del student['age']
show_type("student", student)
print("Student name:", student["name"])
print(f"we can use get for dictonary with fallback:  {student.get('ram', 'no ram')}")


# 4. Set: an unordered collection containing only unique values.
print("\n4. SET")
numbers = {1, 2, 2, 3, 4}
numbers.add(5)
show_type("numbers", numbers)
print("Union:", numbers | {4, 5, 6})
print("Intersection:", numbers & {2, 4, 6})


# 5. Frozen set: an immutable version of a set.
print("\n5. FROZENSET")
permissions = frozenset({"read", "write"})
show_type("permissions", permissions)
print("Has read permission:", "read" in permissions)
# permissions.add("delete")  # This raises AttributeError.


# 6. bytearray: a mutable sequence of integers from 0 through 255.
print("\n6. BYTEARRAY")
message = bytearray(b"cat")
message[0] = ord("h")
show_type("message", message)
print("Decoded message:", message.decode("ascii"))


# 7. Operator overloading: a class defines how operators work for its objects.
print("\n7. OPERATOR OVERLOADING")


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __repr__(self):
		return f"Point({self.x}, {self.y})"


point_a = Point(2, 3)
point_b = Point(4, 1)
print("point_a + point_b:", point_a + point_b)
print("Here, + is overloaded by Point.__add__().")
