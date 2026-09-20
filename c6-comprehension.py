#Comprehensions are concise way to create list, dict, objects, generators in python.

#List comprehension
menu = [
    'iced tea',
    'ginger tea',
    'iced lemon tea',
    'masala chai'
]

# From above, i need to filter out tea which contains ice 
        #  [expression for itemname  in iterable if condition]
iced_tea = [tea for tea in menu if "iced" in tea]
print(iced_tea)


# Set comprehensions -> similar to list
#  {expression for itemname  in iterable if condition}
menu2 = [
    'iced tea',
    'ginger tea',
    'ginger tea',
    'iced lemon tea',
    'iced lemon tea',
    'masala chai',
    'masala chai',
]
unique = {item for item in menu2}
print(unique)



#dictonary
tea_prices_inr = {
    'masala chai':12,
    'green tea':20,
    'lemon tea': 10
}
# convert into dollars 
tea_prices_dollar = {tea:price/80 for tea,price in tea_prices_inr.items()} #for all items, return tea and price/80
print(tea_prices_dollar)


#generators -> their syntax is just similar to list and dictornary, isntead of curly braces and brackets,
# we use paranthesis here , it is like a stream instead of passing whole thing once, it used one by one from memory
generator_data = [4,55,66,786,5,33,56]
sum_data = (item for item in generator_data if item > 40)
print(sum_data) # this returns alone as a location where value is stored, in terms of memory storage this
# comprehension is really good
sum_data_type = sum(item for item in generator_data if item > 40)
print(sum_data_type)







#Problems
# 1. Create a list of squares for even numbers from 1 to 20.
list_squares = [item*item for item in range(1,21)]
print(list_squares)

# 2. Conditionals
numbers = [3, 8, 11, 16, 21, 24]
result_data = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(result_data)


# 3. Nested list comprehension -> flatten this list
matrix = [[1, 2], [3, 4], [5, 6]]
result = [number for data in matrix for number in data]
print(result)


# 4. Dictionary comprehension
words = ["python", "java", "go"]
result_dict = {item:len(item) for item in words}
print(result_dict)

# 5. Dictornary filtering
scores = {"Alice": 85, "Bob": 42, "Charlie": 91, "David":  'sixty'}
scores_dict = {item:score for item,score in scores.items() if isinstance(score, (int,float)) and score >= 60}
print(scores_dict)

# Generator expression
# What Is a Generator?
# A generator produces values one at a time, only when needed. It does not create and store all values in memory at once.

numbers = (x * x for x in range(5))
print(numbers) #here it creates the generator object and store in memory so memory is return
print(next(numbers))  # 0
print(next(numbers))  # 1
print(next(numbers))  # 4

# Generators are useful when:

# You have a large amount of data.
# You do not need all values at the same time.
# You want to save memory.
# You want values to be calculated only when needed.
# large_numbers = (number * number for number in range(1_000_000))
# This does not immediately store one million squared numbers. It calculates each square as you request it.


# Below is generator functions 
def countdown(n):
    while n > 0:
        yield n
        n=n-1
# yield is used inside a generator function. It sends back one value at a time and pauses the function at that point.
numbers = countdown(5)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))