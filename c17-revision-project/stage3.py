import time
import functools

def timed(func):
    @functools.wraps(func) #it preservs metadata like add.__name__ returns add, without this it retuns wrapper, then add__doc__ return add two numbers
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        response = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Function took: {end - start}')
        return response
    return wrapper

@timed
def add(first , second):
    """Add two numbers."""
    return first + second

print(add.__name__)
print(add.__doc__)

# what it does behind the scene is it creates a timed function and pass add into it.
# then add = timed(add) so now, add refers to the wrapper, add(2,3) is now wrapper(2,3)