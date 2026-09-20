# Create a list of five favorite foods. Replace the third item, add one item, and remove one item.

fav_foods = ['paneer', 'pizza', 'burger', 'chole bhature', 'veg biryani']
fav_foods[2] = 'veg burger'
fav_foods.append('pav bhaji')
fav_foods.remove('paneer')
print(f"favourite foods: {fav_foods}")

# Output: both will print [10,20,30,40]

# Largest number in the list
numbers = [12, 5, 89, 34, 2]
print(f"Largest number: {max(numbers)}")

# Create a tuple containing your name, age, and country. Unpack it into three variables and print them.
profile = ('Pratyush', 27, 'India')
name, age, country = profile
print(f"name: {name}, age:{age}, country: {country}")

# Why does this produce an error?
# tuples are immutable so it will throw error

# Convert this tuple into a list, add a new item, and convert it back into a tuple:
colors = ("red", "blue", "green")
colors_list = list(colors)
colors_list.append('YELLOW')
colors = tuple(colors_list)
print(colors)

# title, author, price, and available
dict_data = {
    'title': 'Harry potter',
    'author':'jk rowling',
    'price': 34,
    'available':True
}
dict_data['price'] = 56
dict_data['rating'] = 5
print(f"dict_data is {dict_data}")


# Write code that safely reads the "email" value from this dictionary:
user = {"name": "Sam"}
print(user.get('email', 'email not found'))

words = ["python", "ai", "python", "web", "ai", "python"]
words_set = {}
for item in words:
    if(item in words_set):
        words_set[item] = words_set[item] + 1
    else:
        words_set[item] = 1
print(words_set)

#remove duplicate
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
result = set(numbers)
print(result)


#Create
data = bytearray(b"hello")
data[0] = ord('H')
print(data.decode('utf-8'))

permissions = frozenset({'read', 'write'})
set_permission = {'a','b'}
newSet = {
    permissions : 'basic user',
    # set_permission:'ram'
}
print(newSet[permissions])
# print(newSet[set_permission]) will throw error


# Create a student marks program:
student = {
    "name": "Ravi",
    "marks": [78, 85, 92]
}
print(f"student name: {student['name']}")
total_marks = sum(student['marks'])
average_marks = total_marks / len(student['marks'])

student['passed'] = average_marks > 40
print(student)

# For stronger understanding, do not just make the code run. Explain beside each solution:

# Is the data ordered? -> in dic, data are presered in order
# Is it mutable? yes it is mutable
# Can it contain duplicates? keys must be unqiue but value can be duplicate
# How would you access its values? already done