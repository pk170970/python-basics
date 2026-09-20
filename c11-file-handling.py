# Why use with open(...)?
# This is best practice because:
# with open("demo.txt", "r", encoding="utf-8") as file:
#     pass

# it automatically closes the file
# it saves memory/resources
# it is safer

# Files are like containers for data. In Python, we open them, work with them, and then close them.

#creating a file
with open('myfile.html', 'w') as f:
    f.write('Hello world \n')

# it creates the file if don't exist
# it overwrites the file if exists  

# reading a file
with open('myfile.html', 'r') as f:
    data = f.read()
    print(data)

# appending file: add more content
with open('myfile.html', 'a') as f:
    f.write('this is added later \n')

# want to read line by line
with open('myfile.html', 'r') as file:
    for line in file:
        print(line)

# file which is missing
try:
    with open('missing.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')


# generic way to open a file with try except
try:
    file = open('myfile.ram','r')
    print(file.read())
except FileNotFoundError:
    print('file nhi mili')
finally:
    file.close()