# Infinite generators
# def infinite_generator():
#     count = 1
#     while True:
#         yield (f"Refill {count}")
#         count+=1

# result = infinite_generator() #it will keeping refilling or calling and while will keep running but as 
# we have used yield and range below, so it give for that much only

# for _ in range(5):
#     print(next(result))


# How can we send value to the generators
def send_generator():
    print('Welcome to sending something to yield')
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield

stall = send_generator() # this doesn't run the function body, only creates a generator obj so on print, we can see it.
next(stall) # this starts the generator and runs it until the first yield
# so when it reaches order = yield, it is a pause point. Generator stops here, it return the
# control to the caller. No value is assigned to order yet

# In python, yield is of two types,
# 1. yield value => this sends a value out of generator
# 2. value = yield => pause the generator, waits for caller to send the value back and 
# when resumed, the send value is assigned to order here 


stall.send('Msala tea') # with this line, generator resume from the pause yield
# then again we are writing order = yield inside while, so again it stops and waiting for
# from caller to send another value, so it is not fininshed yet. it is a infinite loop


def test_gen():
    yield 'testing generators'
    yield 'tesing 2 generators'

def calling_another_generators():
    # yield from send_generator()
    yield from test_gen() # yield from used to delete work to another generator

result = calling_another_generators()
for val in result: #for loop keeping calling next inside result until generator is finished
    print(val)

result.close()
# next gives one value from generator 
#  for loop automatically repeats next until no more values left 

for a in range(5):
    print(a)