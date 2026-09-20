#Decorators are kind of wrappers created around a function to enhance/ provide more flexibitlity in functions.
# More good definaton: Decorators are functions which wraps another function and add exttra behaviour without changing the original funcition code.

def decorator_function(func):
    def wrapper():
        print('Starting...')
        func()
        print('Ending...')
    return wrapper

@decorator_function
def greet():
    print('hello')

greet() #original greet was replaced by wrapper. It runs before and after the original function, decorators are usedful for logging, validation and access control, caching, authentication, measure execution time


# If the original function accepts parameters, then wrapper must accept them too 
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print('before calling')
        result = func(*args, **kwargs)
        print('after calling')
        return result
    return wrapper


@logger_decorator
def logging(a,b):
    return a+b

print(logging(5,4))

# Decorators are higher order functions, which take input as fxn and return another function m 