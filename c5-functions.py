# write a function to print_order(name, chai_type) and call it multiple times
# for different customers
# def print_order(name, chai_type):
#     print(f"{name} ordered {chai_type}")

# print_order('ram', 'black tea')

#Scopes in python
# def print_chai():
#     chai_type = 'lemon' #enclosed scope inside a function, can't be use outside
#     print(chai_type)
#     def print_sugarAmount():
#         chai_type = 'ginger' #local scope
#         print(chai_type)
#     print_sugarAmount()


# chai_type = 'masala tea' #global scope
# print_chai()
# print(chai_type)




#Can we access variables which are present outside the function or in global scope from local context
# Yes using non local scope 

# eat_now = False

# def drink_water():
#     take_order = 'ram'
#     def drink_teal():
#         global eat_now
#         nonlocal take_order
#         take_order = 'shyam'
#         eat_now = 'bilota'
#         print(f"drink teal {take_order}")
#     drink_teal()
#     print(f"drink_water {take_order} ")
    

# drink_water()
# print(eat_now)


# Handling arguments in function 
# def greet(*names, **defaultWork):
#     print(f"My name is {names} and i do {defaultWork}")

# greet('ram', 'shyam', work='software development')

# def greet_again():
#     return 'hello', 'again' multiple parameters in return in the form of tuple

# print(type(greet_again()))



# Lamda, Pure and Impure functions 

# Normal functions
# def add(a,b):
#     return a+b
# print(add(2,3))

# lambda functions -> small anonymous function written in one line
# add = lambda a,b:a+b
# square = lambda x:x*x
# print(add(2,3))
# print(square(3))

# students = [("Ali", 78), ("Zen", 85), ("Sam", 92)]
# students.sort(key= lambda student: student[1], reverse=True) #key tells python what value to use for sorting
# print(students) #reverse will sort in descending order



# Problems for functions
# 1. Create a lambda that doubles a number.
double = lambda num: num * 2
print(double(2))


#2. Larger of two numbers
larger = lambda first_num, second_num: max(first_num, second_num)
print(larger(10, 7))

#3 Use map() and a lambda to square [2, 4, 6, 8].
num_list = [2, 4, 6, 8]
squaredList = list(map(lambda num: num * num, num_list))
print(squaredList)

# 4. Use filter() and a lambda to select names longer than four characters.
list_names = ['ram', 'mohan', 'ahtash', 'nishant', 'mahendra', 'pratyush']
list_max_four = list(filter(lambda name: len(name) > 4, list_names))
print(list_max_four)

#5. Sort products by price using lambda
data = [
    {'product': 'shirt', 'price': 30},
    {'product': 'pant', 'price': 90},
    {'product': 'kurta', 'price': 60}
]

data.sort(key= lambda item: item['price'], reverse= True)
# result = list(map(lambda items: items['price'], data))
# print(result)



# pure function 
def add_tax(price, tax_rate):
    return price + price * tax_rate

# this is pure as it uses only it's inputs 

#impure fucntions
count = 0
def totalCount(amount):
    global count
    count+=amount
    return count

totalCount(50)
print(count) # this is impure because it changes the global variable count


# There is lot of built in function and methods in python, check documentatoin
totalCount.__doc__ # this returns any kind of document or msg written on the starting 
# of the function 
totalCount.__name__ # this return the name of the function

